<script>
  import GoodWideCard from "../_components/GoodWideCard.svelte";

  let goods = [
    {
      main: "🍷Кола",
      sub: "Арт. 189650141",
      id: 123123123,
      price: 100,
      quantity: 1,
    },
  ];
</script>

<div>
  <div>cart</div>
  <div>reset</div>
</div>
<div><input type="text" /></div>
<div>
  <div>drinks</div>
  <div>huinks</div>
  <div>salads</div>
  <div>...</div>
</div>
<div>
  {#each goods as good (good.id)}
    <!-- content here -->
    <GoodWideCard {...good} editable />
  {:else}
    <!-- empty list -->
    <h2>Карзина пуста</h2>
  {/each}
</div>
