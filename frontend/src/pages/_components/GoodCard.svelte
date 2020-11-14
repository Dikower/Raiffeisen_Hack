<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  export let thumbnail =
    "https://cdn.shopify.com/s/files/1/2848/4722/products/30f454700daacf066bd7cb2b476eab58_600x.jpg?v=1519595291";
  export let title = "Pizza";
  export let price = 123;
  export let id = 10101010;
  function handleClick() {
    dispatch("click", id);
  }
</script>

<style>
  .good-card {
    width: 173px;
    height: 173px;
    background-color: #fff;
    box-shadow: 0px 0px 32px rgba(174, 174, 174, 0.25);
    border-radius: 13px;
    text-align: center;
    font-weight: bold;
    cursor: pointer;
  }
  img {
    border-radius: inherit;
    padding: 1px;
    height: 115px;
    width: 100%;
    object-fit: cover;
    display: block;
  }
  .title {
    font-size: 30px;
    line-height: 30px;
  }
  .price {
    color: #ff9e46;
    font-size: 18px;
  }
</style>

<div class="good-card" on:click={handleClick}>
  <img src={thumbnail} alt={title} />
  <div class="info">
    <div class="title">{title}</div>
    <div class="price">{price}₽</div>
  </div>
</div>
