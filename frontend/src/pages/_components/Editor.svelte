<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital@1&display=swap" rel="stylesheet">
<script>
  import Modal_window from "./Modal_window.svelte";
  let modal = false;
  import Card from "./GoodCard.svelte";
  import Search from "./Search.svelte"
  let chosen_good;
  let goods = [{'id': 0, 'emoji': '💡', 'title': '', 'price': '', 'art': ''},
    {'id': 1, 'emoji': '🍕', 'title': 'Пицца', 'price': 123, 'art': '123:32'}, {
    'id': 2,
    'emoji': '🍦',
    'title': 'Мороженное',
    'price': 50,
    'art':'123:33'
  }];
  function Update_goods(event) {
    let obj = event.detail.data;
    if (obj['id'] === 0) {
      console.log(obj);
      goods.push({'id': goods.length, 'emoji': obj['emoji'], 'title': obj['title'], 'price': obj['price'], 'art': obj['art']});
    } else {
      goods[obj['id']]['emoji'] = obj['emoji'];
      goods[obj['id']]['title'] = obj['title'];
      goods[obj['id']]['price'] = obj['price'];
      goods[obj['id']]['art'] = obj['art'];
    }
  }
</script>

<style>
  h1 {
    text-align: center;
    margin: 30px;
  }
  .component {
    width: 100%;
    height: 100%;
    font-family: 'Nunito', sans-serif;
  }
  .goods-container {
    margin: auto;
    display: flex;
    justify-content: left;
    align-items: center;
    flex-wrap: wrap;
  }
</style>
<div class="component">
  <h1>Редактор</h1>
  <Search/>
<div class="goods-container">
  {#each goods as good}
    <Card good={good} on:click="{() => {chosen_good = good; modal = true;}}"/>
  {/each}
  {#if modal}
  <Modal_window good={chosen_good} bind:modal={modal} on:update={Update_goods}/>
  {/if}
</div>
</div>

