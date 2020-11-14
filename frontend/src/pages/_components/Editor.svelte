<script>
  import Card from "./GoodCard.svelte";
  let goods = Array(10).fill({});
</script>

<style>
  .goods-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-auto-flow: row;
    gap: 54px 0px;
    justify-content: center;
    
  }
</style>

<p>Editor</p>

<div class="goods-container">
  {#each goods as good}
    <Card {...good} />
  {/each}
</div>
