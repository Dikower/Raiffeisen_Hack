import { writable, get } from "svelte/store";
import { setContext } from "svelte";

export const apiUrl = "https://01d247bffb9a.ngrok.io/";
export const selfUrl = "/";

export let user = writable("");

export async function sendForm(login, username, password) {
  let json_response = await fetch(
    apiUrl + (login ? "users/token" : "users/create"),
    {
      method: "POST",
      credentials: "omit",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `username=${username}&password=${password}`,
    }
  ).then((res) => res.json());
  if (json_response.detail) {
    return login
      ? "Неправильная почта или пароль"
      : "Такая почта уже используется";
  }
  let { access_token, token_type } = json_response;
  user.set(access_token);
  setCookie("access_token", access_token, { samesite: "lax" });
}

function setCookie(name, value, options = {}) {
  options = {
    path: "/",
    ...options,
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie =
    encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

export function getCookie(name) {
  let matches = document.cookie.match(
    new RegExp(
      "(?:^|; )" +
        name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, "\\$1") +
        "=([^;]*)"
    )
  );
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function deleteCookie(name) {
  setCookie(name, "", {
    "max-age": -1,
  });
}

export function checkStoreAndCoockie() {
  if (get(user) === "") {
    let coockie_token = getCookie("access_token");
    if (coockie_token) {
      user.set(coockie_token);
    } else {
      return false;
    }
  }
  return true;
}

export async function authorizedRequest(apiPart, method, object) {
  if (!checkStoreAndCoockie()) {
    return [null, "Unauthorized"];
  }
  let json_response = await fetch(apiUrl + apiPart, {
    method: method,
    headers: new Headers({
      Accept: "application/json",
      Authorization: "Bearer " + get(user),
    }),
    body: JSON.stringify(object),
  }).then((res) => res.json());
  if (json_response.detail && json_response.detail === "Not authenticated") {
    return [null, "Unauthorized"];
  } else if (json_response.detail) {
    return [null, json_response.detail];
  }
  return [json_response, null];
}

export function clearStoreAndCookie() {
  user = "";
  deleteCookie("access_token");
}

// API part

// const cache = new Map();

export function getData(url) {
  const store = writable(new Promise(() => {}));
  const load = async () => {
    const response = fetch(url);
    const data = response.json();
    store.set(Promise.resolve(data));
  };
  load();
  return store;
}

/**
 *
 * @param {number} sum
 * @param {string} info
 */
export async function getQrCodeSrc(sum, info) {
  /**
   * @type {{code:string,qrId:string,payload:string,qrUrl:string}}
   */
  let json_response = await fetch(apiUrl + "transactions", {
    method: "POST",
    headers: new Headers({
      Accept: "application/json",
      Authorization: "Bearer " + get(user),
    }),
    body: JSON.stringify({
      sum,
      info,
    }),
  }).then((res) => res.json());

  return json_response.qrUrl;
}
