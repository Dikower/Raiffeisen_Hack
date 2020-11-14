<script>
  // import { summa } from "./stores";
  import {summa} from '../../GooodsStores.js';
  export let name = "Name";
  export let info = "Info";
  export let price = 0;
  let quantity = 0;

  function addition() {
    summa.update((n) => n + price);
    quantity++;
  }
  function deletion() {
    if (quantity > 0) {
      summa.update((n) => n - price);
      quantity--;
    } else {
      alert("Problem");
    }
  }
</script>

<style>
  .Info {
    width: 60%;
    margin-left: 20px;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .Control {
    width: 40%;
  }
  .Price {
    display: flex;
    justify-content: flex-end;
    margin: 15px;
    font-weight: bold;
    font-size: 20px;
  }
  .Price nobr {
    color: #ff9e46;
  }

  .Control {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    /* background-color: orangered; */
    margin-bottom: 10px;
  }
  .ControlPanel {
    display: flex;
    /* background-color: orchid; */
    justify-content: space-around;
    align-items: center;
    height: 50px;
  }
  .amount {
    margin: 0;
  }
  .ControlPanel p {
    color: #ff9e46;
    font-size: 20px;
    font-weight: bold;
  }
  .ControlPanel p nobr {
    font-size: 15px;
    color: black;
  }
  .GoodsBox {
    background-color: white;
    margin: 10px;
    height: 100px;
    display: flex;
    justify-content: space-between;
    border-radius: 15px;
    min-width: 300px;
    width: 90%;
  }
  button {
    border-radius: 100%;
    border: 0;
    background-color: #f8f8f8;
    width: 40px;
    height: 40px;
    margin: 0;
  }
  button nobr {
    font-size: 20px;
    font-weight: bold;
    color: #ff9e46;
  }
  .Info .Name {
    font-weight: bold;
    font-size: 28px;
    height: 25%;
  }
  .Info .Art {
    font-weight: bold;
    font-size: 10px;
    color: #ababab;
  }
</style>

<div class="GoodsBox">
  <div class="Info">
    <p class="Name">{name}</p>
    <p class="Art">Арт. {info}</p>
  </div>

  <div class="Control">
    <div class="Price">
      {price}
      <nobr>₽</nobr>
    </div>
    <div class="ControlPanel">
      <button on:click={deletion} class="ButMin"><nobr>-</nobr></button>
      <p class="amount">
        {quantity}
        <nobr>шт</nobr>
      </p>

      <button on:click={addition} class="ButPl"><nobr>+</nobr></button>
    </div>
  </div>
</div>
