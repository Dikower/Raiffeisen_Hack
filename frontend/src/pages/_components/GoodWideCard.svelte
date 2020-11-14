<script>
  import { createEventDispatcher } from "svelte";

  import WideCard from "./WideCard.svelte";
  const dispatch = createEventDispatcher();

  export let main = "🍷Кола";
  export let sub = "Арт. 189650141";
  export let id = 123123123;
  export let price = 100;
  export let quantity = 1;

  export let editable = false;

  const onInc = () => dispatch("increase", id);
  const onDec = () => dispatch("decrease", id);
  const onClick = () => {
    console.log("clicked");
    dispatch("click", id);
  };
</script>

<style>
  .main {
    font-size: 20px;
    font-weight: 900;
  }

  .sub {
    font-size: 10px;
    color: #ababab;
  }

  .price,
  .quantity {
    font-weight: 900;
    font-size: 20px;
    text-align: right;
  }

  .price > span,
  .quantity {
    color: #ff9e46;
  }
  .quantity > span {
    color: black;
    font-weight: 700;
    font-size: 14px;
  }
</style>

<WideCard on:click={onClick}>
  <div>
    <div class="main" onclick>{main}</div>
    <div class="sub">{sub}</div>
  </div>
  <div>
    <div class="price">{price} <span>₽</span></div>
    {#if editable}
       div.button.decreas
    {/if}
    <div class="quantity">{quantity} <span>шт</span></div>
  </div>
</WideCard>
