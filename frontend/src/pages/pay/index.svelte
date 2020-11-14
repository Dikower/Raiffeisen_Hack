<script>
  import BottomContainer from "../_components/BottomContainer.svelte";
  import GoodWideCard from "../_components/GoodWideCard.svelte";
  import Qr from "./_components/QR.svelte";
  import { summa } from "../GooodsStores.js";
  import { finalpositions } from "../GooodsStores.js";
  import { onMount } from "svelte";
  import { getQrCodeSrc } from "../_api";
  import { get } from "svelte/store";

  let qrSrc = "";
  onMount(async () => {
    qrSrc = await getQrCodeSrc(get(summa), "HUI");
  });
</script>

<style>
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
  h2{
    color: white;
  }
  h1{
    margin-top: -20px;
    margin-bottom: 10px;
    font-size: 50px;
    color: white;
  }
</style>

<!-- routify:options index=3 -->
<div class="pay">
  <div class="pay-info">
    <h2>Сумма покупки</h2>
    <h1>{$summa}₽</h1>

    <Qr qrLink={qrSrc} />
  </div>
  <BottomContainer>
    <div class="Body">
      {#each $finalpositions as { name, info, price }}
        <GoodWideCard {name} {info} {price} />
      {/each}
    </div>
  </BottomContainer>
</div>
