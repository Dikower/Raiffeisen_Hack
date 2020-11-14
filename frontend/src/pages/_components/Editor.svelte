<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital@1&display=swap" rel="stylesheet">
<script>
  let goods = [{'ind': 0, 'id': '', 'emoji': '💡', 'name': '', 'price': '', 'code': '', 'tag': ''}];
  let api_url = 'https://301706e8534b.ngrok.io/';
  import { getCookie } from "../_api.js";
  let search_text = '';
  import Modal_window from "./Modal_window.svelte";
  let modal = false;
  import Card from "./GoodCard.svelte";
  import Search from "./Search.svelte"
  let chosen_good;
  // let goods = [{'ind': 0, 'emoji': '💡', 'name': '', 'price': '', 'code': ''},
  //   {'ind': 1, 'emoji': '🍕', 'name': 'Пицца', 'price': 123, 'code': '123:32'}, {
  //   'ind': 2,
  //   'emoji': '🍦',
  //   'name': 'Мороженное',
  //   'price': 50,
  //   'code':'123:33'
  // }]
  async function Update_goods(event) {
    let obj = event.detail.data;
    if (obj['ind'] === 0) {
      goods.push({'ind': goods.length, 'id': '', 'emoji': obj['emoji'], 'name': obj['name'], 'price': obj['price'], 'code': obj['code'], 'tag': ''});
      const json_response = await Authorised_fetch_sec('positions/create', 'Post',
              {'emoji': obj['emoji'], 'name': obj['name'], 'price': Number(obj['price']), 'code': obj['code'], 'tag': ''});
      console.log(goods);
      goods[goods.length-1]['id'] = json_response['id'];
      console.log(goods);
    } else {
      goods[obj['ind']]['emoji'] = obj['emoji'];
      goods[obj['ind']]['name'] = obj['name'];
      goods[obj['ind']]['price'] = obj['price'];
      goods[obj['ind']]['code'] = obj['code'];
      const json_response = await Authorised_fetch_sec('positions/edit', 'Put',
              {'id': obj['id'], 'emoji': obj['emoji'], 'name': obj['name'], 'price': Number(obj['price']), 'code': obj['code'], 'tag': ''})
    }
  }
  import { onMount } from 'svelte';
  onMount(async () => {
    const json_response = await Authorised_fetch_get('positions/all', 'Get');
    goods = goods.concat(json_response);
    let counter = 0;
    goods.forEach((el) => {
      el['ind'] = counter;
      counter++;
    });
    console.log(goods);
  });
  async function Authorised_fetch_sec(path, method, obj) {
   return await fetch(api_url + path, {
      method: method,
      headers: new Headers({
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + getCookie('access_token'),
      }),
     body: JSON.stringify(obj)
    }).then(res => res.json());
  }
  async function Authorised_fetch_get(path) {
   return await fetch(api_url + path, {
      method: 'Get',
      headers: new Headers({
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + getCookie('access_token'),
      }),
    }).then(res => res.json());
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
  <Search bind:search_text={search_text}/>
<div class="goods-container">
   {#each goods as good}
    {#if search_text === '' || (search_text.length <= good['name'].length && good['name'].slice(0, search_text.length) === search_text) || good['ind']===0 }
    <Card good={good} on:click="{() => {chosen_good = good; modal = true}}"/>
      {/if}
  {/each}
  {#if modal}
  <Modal_window good={chosen_good} bind:modal={modal} on:update={Update_goods}/>
  {/if}
</div>
</div>


