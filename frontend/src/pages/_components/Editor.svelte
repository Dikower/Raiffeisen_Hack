<script>
  import {
    apiUrl,
    getCookie,
    deleteCookie,
    getAllPositions,
    authFetch,
  } from "../_api.js";
  import { goto, url } from "@roxi/routify";
  import Card from "./GoodCard.svelte";
  import Search from "./Search.svelte";
  import Modal_window from "./Modal_window.svelte";
  import { onMount } from "svelte";

  let goods = [];

  let search_text = "";
  let modal = false;
  let chosen_good;

  let personalEditCode = authFetch("users/profile").then(
    (r) => r.catalog.entry_code
  );

  async function Update_goods(event) {
    let obj = event.detail.data;
    if (obj["ind"] === 0) {
      goods.push({
        ind: goods.length,
        id: "",
        emoji: obj["emoji"],
        name: obj["name"],
        price: obj["price"],
        code: obj["code"],
        tag: "",
      });
      const json_response = await authFetch("positions/create", "POST", {
        emoji: obj["emoji"],
        name: obj["name"],
        price: Number(obj["price"]),
        code: obj["code"],
        tag: "",
      });
      goods[goods.length - 1]["id"] = json_response["id"];
    } else {
      goods[obj["ind"]]["emoji"] = obj["emoji"];
      goods[obj["ind"]]["name"] = obj["name"];
      goods[obj["ind"]]["price"] = obj["price"];
      goods[obj["ind"]]["code"] = obj["code"];
      await authFetch("positions/edit", "PUT", {
        id: obj["id"],
        emoji: obj["emoji"],
        name: obj["name"],
        price: Number(obj["price"]),
        code: obj["code"],
        tag: "",
      });
    }
  }

  onMount(async () => {
    const json_response = await getAllPositions();
    goods = goods.concat(json_response);
    let counter = 0;
    goods.forEach((el) => {
      el["ind"] = counter;
      counter++;
    });
    console.log(goods);
  });
</script>

<style>
  h1 {
    text-align: center;
    margin: 30px;
  }
  .component {
    width: 100%;
    height: 100%;
    font-family: "Nunito", sans-serif;
  }
  .logout {
    position: absolute;
    top: 5px;
    right: 10px;
    border-radius: 10px;
    background: transparent;
    border: 0;
    font-weight: bold;
  }
  .logout:hover {
    cursor: pointer;
  }
  .goods-container {
    margin: auto;
    display: flex;
    justify-content: left;
    align-items: center;
    flex-wrap: wrap;
  }
</style>

<link rel="preconnect" href="https://fonts.gstatic.com" />
<link
  href="https://fonts.googleapis.com/css2?family=Nunito:ital@1&display=swap"
  rel="stylesheet" />
<div class="component">
  <div>
    Номер Вашего каталога
    {#await personalEditCode}
      <!-- promise is pending -->
    {:then code}
      <!-- promise was fulfilled -->
      {code}
    {/await}
  </div>
  <button
    class="logout"
    on:click={() => {
      deleteCookie('access_token');
      $goto($url('../auth/signup'), {}, false);
    }}>Выйти</button>
  <h1>Редактор</h1>
  <Search bind:search_text />
  <div class="goods-container">
    {#each goods as good}
      {#if search_text === '' || (search_text.length <= good['name'].length && good['name'].slice(0, search_text.length) === search_text) || good['ind'] === 0}
        <Card
          {good}
          on:click={() => {
            chosen_good = good;
            modal = true;
          }} />
      {/if}
    {/each}
    {#if modal}
      <Modal_window good={chosen_good} bind:modal on:update={Update_goods} />
    {/if}
  </div>
</div>
