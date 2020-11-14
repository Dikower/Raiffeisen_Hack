<script>
  import BottomContainer from "../_components/BottomContainer.svelte";
  import GoodWideCard from "../_components/GoodWideCard.svelte";
  import Qr from "./_components/QR.svelte";
  import {summa} from '../GooodsStores.js';
  //   import bg from "../../../assets/images/anal-bg.svg";
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
</style>

<!-- routify:options index=3 -->
<div class="pay">
  <div class="pay-info">
    <h2>Сумма покупки</h2>
    <h1>{$summa}</h1>

    <Qr />
  </div>
  <BottomContainer>
    <GoodWideCard />
    <GoodWideCard />
    <GoodWideCard />
    <GoodWideCard />
    <GoodWideCard />
    <GoodWideCard />
    <GoodWideCard />
    <GoodWideCard />
  </BottomContainer>
</div>
