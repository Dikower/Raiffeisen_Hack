<script>
  import { goto, url } from "@roxi/routify";
  import { getContext } from "svelte";
  import Input from "./_components/Input.svelte";
  import { user, sendForm, selfUrl } from "../_api";

  let apiUrl = getContext("apiUrl");
  let form;
  let email;
  let password;
  let errorMessage = null;
  let socialNetworks = {};
  $: showError = !!errorMessage;

  function validateForm() {
    if (!email.input.checkValidity() || email.value === "") {
      errorMessage = "Пожалуйста, укажите почту";
      return false;
    }
    if (password.value === "") {
      errorMessage = "Пожалуйста, укажите пароль";
      return false;
    }
    return true;
  }

  async function submit() {
    if (!validateForm()) return;
    showError = false;
    let error = await sendForm(true, email.value, password.value);
    if (error) {
      errorMessage = error;
      return;
    }
    $goto("/editor", {}, false);
  }
</script>

<style>
  .component {
    position: absolute;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: url("/images/auth_back.svg");
    background-size: cover;
  }

  .headings {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 0 20px 0;
  }
  .headings h2 {
    color: #FF9E46;
  }
  .p-wrapper a{
    color: #000000;
  }
  .headings h2 {
    margin: 0 20px;
  }
  .p-wrapper {
    border-right: 2px solid #000000;
  }
  .inputs-block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }

  .right-block {
    min-width: 250px;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }

  form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 350px;
    --plain-font-size: calc(
      16px + (20 - 16) * ((100vw - 300px) / (1440 - 300))
    );
  }

  .button-block {
    display: flex;
    justify-content: center;
  }

  button:active,
  button:focus,
  button:hover {
    outline: none;
  }

  .registration-p,
  .registration-a {
    --plain-font-size: calc(
      16px + (20 - 16) * ((100vw - 300px) / (1440 - 300))
    );
  }
  .p-wrapper {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    --plain-font-size: calc(
      16px + (20 - 16) * ((100vw - 300px) / (1440 - 300))
    );
  }

  ul {
    list-style: none;
    margin-left: 0;
    padding: 0;
  }

  button {
    padding: 2%;
    font-size: 16px;
    outline: none;
    border-radius: 0;
  }

  .social-link {
    text-decoration: none;
    color: #545454;
  }

  .social-link:hover {
    color: #1355ff;
  }

  .error-label {
    text-align: center;
    align-self: center;
    margin-bottom: 1%;
    opacity: 0;
    transition: opacity ease 0.5s;
    margin-top: 2%;
    --plain-font-size: calc(
      16px + (18 - 16) * ((100vw - 300px) / (1440 - 300))
    );
    color: red;
  }

  .showError {
    opacity: 1;
  }
  .round_button {
    width: 70px;
    height: 70px;
    border-radius: 70px;
    background: transparent url("/images/GoToPayGoods.svg");
    background-size: cover;
    border: 0;
    outline: none;
  }
  @media (min-width: 768px) {
    .headings h2, .p-wrapper a {
      font-size: 20px;
    }
  }
  @media (max-width: 768px) {
    .component {
      flex-direction: column;
    }

    .right-block {
      flex-direction: column;
    }

    .social-networks {
      margin-left: 0;
      margin-top: 5%;
    }

    ul {
      margin-block-start: 0.5em;
    }

    .error-label {
      text-align: right;
      align-self: flex-start;
    }

    form {
      width: 100%;
    }
    .headings h2, .p-wrapper a {
      font-size: 15px;
    }
  }
</style>

<svelte:head>
  <title>Вход</title>
</svelte:head>

<div class="component">
  <div class="headings">
  <div class="p-wrapper">
          <h2 class="registration-p">
            <a class="registration-a" href="./signup">РЕГИСТРАЦИЯ</a>
          </h2>
        </div><h2>АВТОРИЗАЦИЯ</h2>
  </div>
  <div class="right-block">
    <form bind:this={form}>
      <div class="inputs-block">
        <Input bind:this={email} placeholder="E-mail" name="username" type="email" />
        <Input
          bind:this={password}
          placeholder="Пароль"
          name="password"
          type="password" />
        <p class="error-label" class:showError>{errorMessage}</p>
      </div>
      <div class="button-block">
        <button type="button" class="round_button" on:click={submit}></button>
      </div>
    </form>
  </div>
</div>
