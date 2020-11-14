<script>
  import WideCard from "../../_components/WideCard.svelte";

  export let main = "🍷Кола";
  export let sub = "Арт. 189650141";
  export let price = 100;
  export let quantity = 1;
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

<WideCard>
  <div>
    <div class="main">{main}</div>
    <div class="sub">{sub}</div>
  </div>
  <div>
    <div class="price">{price} <span>₽</span></div>
    <div class="quantity">{quantity} <span>шт</span></div>
  </div>
</WideCard>
