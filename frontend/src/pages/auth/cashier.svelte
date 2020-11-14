<script>
  import { goto } from "@roxi/routify";
  import { entryCode } from "../goodsStores";

  let number = null;
  function handleSubmit() {
    entryCode.set(number);
    localStorage.setItem("entryCode", number);
    $goto("/goods");
  }
</script>

<h1>Вход в каталог</h1>
<p>Введите номер каталога, его можно получить у ИП</p>
<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={number} />
  <input type="submit" value="Войти" />
</form>
