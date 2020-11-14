import { writable, get } from "svelte/store";
import { entryCode } from "./goodsStores";

export const apiUrl = "https://backend.sbp-kassa.online/";
export const selfUrl = "/";

export let accessToken = writable("");
accessToken.set(getCookie("access_token"));

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
  accessToken.set(access_token);
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

export function deleteCookie(name) {
  setCookie(name, "", {
    "max-age": -1,
  });
}

export function checkStoreAndCookie() {
  if (get(accessToken) === "") {
    let access_token = getCookie("access_token");
    if (access_token) {
      accessToken.set(access_token);
    } else {
      return false;
    }
  }
  return true;
}

export async function authorizedRequest(apiPart, method, object) {
  if (!checkStoreAndCookie()) {
    return [null, "Unauthorized"];
  }
  let json_response = await fetch(apiUrl + apiPart, {
    method: method,
    headers: new Headers({
      Accept: "application/json",
      Authorization: "Bearer " + get(accessToken),
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
  accessToken = "";
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
 * @param {string} path без "/" в начале
 * @param {"POST" | "GET" | "PUT" | "DELETE"} method
 * @param {any?} body
 */
export async function authFetch(path, method = "GET", body = undefined) {
  return await fetch(apiUrl + path, {
    method: method,
    headers: new Headers({
      Accept: "application/json",
      Authorization: "Bearer " + get(accessToken),
    }),
    body: body && JSON.stringify(body),
  }).then((res) => res.json());
}

/**
 *
 * @param {number} sum
 * @param {string} info
 * @returns {Promise<{code:string,qrId:string,payload:string,qrUrl:string}>}
 */
export function getQrCodeSrc(sum, info) {
  return fetch("transactions/", {
    method: "POST",
    body: JSON.stringify({
      sum,
      info,
      entry_code: get(entryCode),
    }),
  });
}

/**
 * Для владельца
 */
export function getAllPositions() {
  return authFetch("positions/all");
}

/**
 * Для кассира
 * @returns {Promise<{positions:[]}>}
 */
export function getAllCashierPositions() {
  return fetch(apiUrl + `catalogs/${get(entryCode)}`, {
    method: "GET",
    headers: new Headers({
      Accept: "application/json",
    }),
  }).then((res) => res.json());
}
