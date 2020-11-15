<script>
  import {
    apiUrl,
    getCookie,
    deleteCookie,
    getAllPositions,
    authFetch,
  } from "../_api.js";
  import { fade } from "svelte/transition"
  import { goto, url } from "@roxi/routify";
  import Card from "./GoodCard.svelte";
  import Search from "./Search.svelte";
  import Modal_window from "./Modal_window.svelte";
  import { onMount } from "svelte";

  let goods = [{ id: "", emoji: "💡", name: "", price: "", code: "", tag: "" }];

  let search_text = "";
  let modal = false;
  let text_visibility = false;
  let chosen_good;

  let personalEditCode = authFetch("users/profile").then(
    (r) => r.catalog.entry_code
  );

  function Copy() {
    let text = document.getElementsByClassName('hidden_href')[0];
    text.select();
    document.execCommand('copy');
    text_visibility = true;
    setTimeout(() => text_visibility = false, 1500)
  }

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
  });
</script>

<style>
  h1 {
    text-align: center;
  }
  .component {
    width: 100%;
    height: 100%;
    font-family: "Nunito", sans-serif;
  }
  .current_catalog {
    box-shadow: 0 0 32px rgba(174, 174, 174, 0.25);
    width: 200px;
    border-radius: 20px;
    padding: 10px 20px;
    margin: 10px;
  }
  .current_catalog:hover {
    cursor: pointer;
  }
  .current_catalog_text {
    position: absolute;
    top: 60px;
    left: 30px;
    margin: 0;
    font-size: 12px;
  }
  .hidden_href {
    position: absolute;
    top: -50px;
    opacity: 0;
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
  .title_block {
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 0 30px 0;
  }
  .arrow {
    width: 30px;
    height: 30px;
    margin: 0 10px;
  }
  .arrow:hover {
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
  <div class='current_catalog' on:click={Copy}>
    Ваш каталог
    {#await personalEditCode}
      <!-- promise is pending -->
    {:then code}
      <!-- promise was fulfilled -->
      {code}
      <input class="hidden_href" value="{window.location.href.split('editor')[0]}auth/{code}">
    {/await}
  </div>
  {#if text_visibility}
  <p class="current_catalog_text" transition:fade>Скопировано!</p>
    {/if}
  <button
    class="logout"
    on:click={() => {
      deleteCookie('access_token');
      $goto($url('../auth/signup'), {}, false);
    }}>Выйти</button>
  <div class="title_block">
  <h1>Редактор</h1>
    <svg class="arrow" on:click={() => $goto('../analytics')}>
    <line x1="0" y1="30" x2="15" y2="15" stroke="#FF9E46" stroke-width="2"></line>
    <line x1="0" y1="0" x2="15" y2="15" stroke="#FF9E46" stroke-width="2" stroke-linecap="round"></line>
  </svg>
  </div>
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
