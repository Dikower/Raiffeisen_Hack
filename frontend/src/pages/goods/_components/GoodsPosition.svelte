<script>
  import { summa } from "../../goodsStores.js";
  import { finalPositions } from "../../goodsStores.js";
  export let name = "Name";
  export let code = "i did not get an info";
  export let price = 0;

  function addition() {
    summa.update((n) => n + price);
    /**
     * @type {any[]}
     */
    const newPostitions = JSON.parse(JSON.stringify($finalPositions));
    let index = newPostitions.findIndex((p) => p.code === code);
    if (index === -1) {
      console.log("creating");
      newPostitions.push({ name, code, price, quantity: 1 });
    } else {
      console.log("increasing");
      newPostitions[index].quantity += 1;
    }
    finalPositions.set(newPostitions);
    console.log({ $finalPositions });
  }
  function deletion() {
    summa.update((n) => n - price);
    /**
     * @type {any[]}
     */
    let newPostitions = JSON.parse(JSON.stringify($finalPositions));
    let index = newPostitions.findIndex((p) => p.code === code);
    if (index === -1) {
    } else if (newPostitions[index].quantity === 1) {
      console.log("deleting");
      newPostitions.splice(index, 1);
    } else {
      console.log("decreasing");
      newPostitions[index].quantity -= 1;
    }
    finalPositions.set(newPostitions);
  }

  $: quantity =
    ($finalPositions.find((p) => p.code === code) || {}).quantity || 0;
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
    cursor: pointer;
  }
  button:disabled {
    cursor: default;
    filter: grayscale();
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
    <p class="Art">Арт. {code}</p>
  </div>

  <div class="Control">
    <div class="Price">
      {price}
      <nobr>₽</nobr>
    </div>
    <div class="ControlPanel">
      <button
        on:click={deletion}
        disabled={quantity === 0}
        class="ButMin"><nobr>-</nobr></button>
      <p class="amount">
        {quantity}
        <nobr>шт</nobr>
      </p>

      <button on:click={addition} class="ButPl"><nobr>+</nobr></button>
    </div>
  </div>
</div>
