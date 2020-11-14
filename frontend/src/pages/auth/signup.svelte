<script>
  import {user, sendForm, selfUrl} from "../_api.js";
  import {goto, url} from "@roxi/routify";
  import {getContext} from 'svelte';
  import Input from './_components/Input.svelte'

  let checked = false;

  let socialNetworks = {
    facebook: 'https://facebook.com',
    twitter: 'https://twitter.com',
    vkontakte: 'https://vk.com'
  };
  let apiUrl = getContext('apiUrl');
  let form;
  let name;
  let email;
  let password;
  let password2;
  let errorMessage = null;
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
    if (password2.value === "") {
      errorMessage = "Пожалуйста, повторите пароль";
      return false;
    }
    if (password.value !== password2.value) {
      errorMessage = "Пароли не совпадают";
      return false;
    }
    return true;
  }

  async function submit() {
    if (!validateForm()) return;
    showError = false;
    let error = await sendForm(false, email.value, password.value);
    if (error) {
      errorMessage = error;
      return;
    }
    $goto("/editor", {}, false);
  }
</script>

<svelte:head>
  <title>Регистрация</title>
</svelte:head>

<div class="component">
  <div class="headings">
  <h2>РЕГИСТРАЦИЯ</h2>
   <div class="p-wrapper"><h2 class="registration-p"><a class="registration-a" href='./signin'>АВТОРИЗАЦИЯ</a></h2>
        </div>
  </div>
  <div class="right-block">
    <form bind:this={form}>
      <div class="inputs-block">
        <Input bind:this={email} placeholder="E-mail" name="username" type="email"/>
        <Input bind:this={password} placeholder="Пароль" name="password" type="password"/>
        <Input bind:this={password2} placeholder="Подтверждение пароля" name="password" type="password"/>
      </div>
      <p class="error-label" class:showError>{errorMessage}</p>
      <div class="button-block">
        <button type="button" class="round_button" on:click={submit}></button>
      </div>
    </form>
  </div>
</div>

<style>

  .text-login01 {
    cursor: pointer;
    margin-right: 3%;
    margin-left: 3%;
    font-family: "Helvetica Norm";
    text-align: center;
    align-self: center;
  }

  .component {
    position: absolute;
    width: 100%;
    height: 100%;
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
    border-left: 2px solid #000000;
  }
  .inputs-block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 150px;
  }

  .right-block {
    min-width: 250px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 300px;
    width: 350px;
  }

  .button-block {
    display: flex;
    justify-content: center;
  }

  button {
    font-size: 16px;
    padding: 2%;
    outline: none;
    border-radius: 0;
  }

  button:active, button:focus, button:hover {
    outline: none;
    border-radius: 0;
  }

  .registration-p, .registration-a {
    --plain-font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1440 - 300)));
  }


  .registration-p {
    /*margin-left: 20px;*/
    /*margin-top: 5px;*/
  }

  ul {
    list-style: none;
    margin-left: 0;
    padding: 0;
  }

  .error-label {
    text-align: center;
    align-self: center;
    margin-bottom: 1%;
    opacity: 0;
    transition: opacity ease 0.5s;
    --plain-font-size: calc(16px + (18 - 16) * ((100vw - 300px) / (1440 - 300)));
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
  .round_button:hover {
    outline: none;
    border: 0;
    background-color: transparent;
    cursor: pointer;
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
