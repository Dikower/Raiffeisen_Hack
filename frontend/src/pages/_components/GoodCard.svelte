<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  export let thumbnail =
    "https://cdn.shopify.com/s/files/1/2848/4722/products/30f454700daacf066bd7cb2b476eab58_600x.jpg?v=1519595291";
  export let good = {};
  function handleClick() {
    dispatch("click", good['id']);
  }
</script>

<style>
  .good-card {
    width: 170px;
    height: 170px;
    background-color: #fff;
    box-shadow: 0 0 32px rgba(174, 174, 174, 0.25);
    border-radius: 13px;
    text-align: center;
    font-weight: bold;
    cursor: pointer;
    margin: 30px;
  }
  .new_good_svg {
    height: 60px;
    width: 60px;
    margin: 55px;
  }
  .emoji_box {
    font-size: 55px;
    margin: 10px;
  }
  .title {
    font-size: 20px;
    line-height: 30px;
  }
  .price {
    color: #ff9e46;
    font-size: 18px;
  }
</style>
<svelte:head>
  <meta charset="UTF-8">
</svelte:head>
<div class="good-card" on:click={handleClick}>
  {#if good['id'] === 0}
    <img src="/images/plus.svg" class="new_good_svg" alt="new_good">
    {:else}
    <p class="emoji_box">{good['emoji']}</p>
  <div class="info">
    <div class="title">{good['title']}</div>
    <div class="price">{good['price']}₽</div>
  </div>
  {/if}
</div>
