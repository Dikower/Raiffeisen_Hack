<script>
  import GoodsPosition from "./_components/GoodsPosition.svelte";
  import { fnTot } from "../_utils";
  import { goto } from "@roxi/routify";
  import { finalPositions, summa } from "../goodsStores.js";
  // import { positions } from "../GooodsStores.js";
  import Search from "../_components/Search.svelte";
  import { onMount } from "svelte";
  import { getAllCashierPositions } from "../_api";
  import { writable } from "svelte/store";

  let searchText = "";

  /**
   * @type {import("svelte/store").Writable<{name:string;code:string;price:number;quantity:number}[]>}
   */
  let dynamicPositions = null;

  onMount(async () => {
    dynamicPositions = writable((await getAllCashierPositions()).positions);
    // debugger
    console.log("Got dynamicPositions");
  });

  function GoToPay() {
    $goto("../pay");
  }

  function handleReset() {
    finalPositions.update((old) => old.map((o) => ({ ...o, quantity: 0 })));
  }

  $: filteredPositions =
    dynamicPositions && searchText
      ? $dynamicPositions.filter((p) =>
          p.name.toLowerCase().includes(searchText.toLowerCase())
        )
      : $dynamicPositions;

  $: formattedTotal = fnTot($summa);
</script>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    max-width: 900px;
    margin: auto;
  }

  .Sum {
    display: flex;
    margin-left: 5%;
  }
  h1 {
    margin-left: 10px;
  }

  .HeaderSumUpd {
    display: flex;
    justify-content: space-between;
    position: sticky;
    top: 0;
    background-image: linear-gradient(
      rgba(255, 255, 255, 1) 50%,
      rgba(255, 255, 255, 0)
    );
  }

  .HeaderSumUpd .Upd {
    border: 0;
    align-self: center;
    margin-right: 5%;
    margin-top: 20px;
    width: 50px;
    height: 50px;
    background-image: url(/images/TrashCanGoods.svg);
    background-size: 100% 100%;
  }
  .HeaderSumUpd nobr {
    color: orange;
    font-size: 20px;
  }
  .HeaderSumUpd img {
    margin-top: 20px;
    width: 50px;
    height: 50px;
  }
  .Body {
    background-color: #f8f8f8;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
  .ToPay {
    width: 100%;
    position: sticky;
    bottom: 1em;
    text-align: center;
  }
  .ToPay button {
    background-size: 100% 100%;
    height: 100%;
    border: none;
    background-color: transparent;
    margin: 0;
    padding: 0;
    cursor: pointer;
    opacity: 1;
    transition: opacity 0.3s ease;
  }

  .ToPay button:disabled {
    opacity: 0.4;
    filter: grayscale();
    cursor: default;
  }

  .ToPay button img {
    display: block;
  }
</style>

<main>
  <div class="HeaderSumUpd">
    <div class="Sum">
      <img src="/images/ShoppingCartGoods.svg" alt="Hehe" />
      <h1>{formattedTotal}</h1>
    </div>
    <button class="Upd" on:click={handleReset} />
  </div>
  <div class="input-wrapper">
    <Search bind:search_text={searchText} />
  </div>

  <div class="Body">
    {#if $dynamicPositions === null}
      <!-- content here -->
      loading
    {:else if Array.isArray($dynamicPositions)}
      {#each filteredPositions as { name, code, price }}
        <GoodsPosition {name} {code} {price} />
      {/each}
      <div class="ToPay">
        <button on:click={GoToPay} disabled={$summa === 0}>
          <img src="/images/GoToPayGoods.svg" alt="Оформить заказ" />
        </button>
      </div>
    {:else}
      <!-- else content here -->
      no positions
    {/if}
  </div>
</main>
