<script>
  import BottomContainer from "../_components/BottomContainer.svelte";
  import GoodWideCard from "../_components/GoodWideCard.svelte";
  import Qr from "./_components/QR.svelte";
  import { summa } from "../goodsStores.js";
  import { finalPositions } from "../goodsStores.js";
  import { onMount } from "svelte";
  import { getQrCodeSrc } from "../_api";
  import { get } from "svelte/store";
  import { fnTot } from "../_utils";
  import { goto } from "@roxi/routify";

  let qrSrc = "";
  onMount(async () => {
    qrSrc = await getQrCodeSrc(get(summa), `Оплата чека на ${get(summa)} рублей`);
  });
  $: formattedTotal = fnTot($summa);
</script>

<style>
  .nav-back {
    position: absolute;
    top: 20px;
    left: 20px;
    padding: 0.5em;
    cursor: pointer;
  }
  .nav-back img {
    display: block;
  }
  .pay {
    background-color: #ff9e46;
    background-image: url("/images/anal-bg.svg");
    background-size: cover;
    height: 100vh;
  }
  .pay-info {
    height: 60vh;
    text-align: center;
    padding: 16px;
    /* display: inline-block; */
  }
  h2 {
    color: white;
  }
  h1 {
    margin-top: -20px;
    margin-bottom: 10px;
    font-size: 50px;
    color: white;
  }
</style>

<!-- routify:options index=3 -->
<div class="pay">
  <div class="nav-back" on:click={() => $goto('/goods')}>
    <img src="/images/arrow-left.svg" alt="Назад" />
  </div>

  <div class="pay-info">
    <h2>Сумма покупки</h2>
    <h1>{formattedTotal}</h1>

    <Qr qrLink={qrSrc} />
  </div>
  <BottomContainer>
    <div class="Body">
      {#each $finalPositions as { name, code, price, quantity }}
        <GoodWideCard {name} {code} {price} {quantity} />
      {/each}
    </div>
  </BottomContainer>
</div>
