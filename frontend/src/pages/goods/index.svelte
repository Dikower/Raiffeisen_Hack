<script>
  import GoodsPosition from './_components/GoodsPosition.svelte'
  //import {summa} from './_components/stores.js';
  import {summa} from '../GooodsStores.js';
  import {goto} from '@roxi/routify';
  let positions = [
    { name: "Кола", info: "189650141", price: 20},
    { name: "Картошка", info: "102389011", price: 48},
    { name: "Сыр", info: "189650141", price: 20},
    { name: "Молоко", info: "102389011", price: 58},
    { name: "Хлеб", info: "189650141", price: 23},
    { name: "Булочка", info: "102389011", price: 88},
    { name: "Масло", info: "189650141", price: 120},
    { name: "Огурец", info: "102389011", price: 3}
  ]
  function GoToPay(){
    $goto("../pay");
  }
</script>

<main>

  <div class = "Header">
    <div class="HeaderSumUpd">
      <div class="Sum">
        <img src="/images/ShoppingCartGoods.svg" alt="Hehe">
        <h1>{$summa}<nobr>₽</nobr></h1>
      </div>
      <button class="Upd"></button>
    </div>
    <input type="search" name="q" placeholder="Поиск по сайту">
  </div>

  <div class = "Body">
    {#each positions as {name,info,price}}
      <GoodsPosition {name} {info} {price}/>
    {/each}
  </div>

  
  <div class="ToPay">
      <button on:click={GoToPay}></button>
  </div>
</main>

<style>
  main{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .Header{
    background-color: #f8f8f8;
    height: 150px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .Header .Sum{
    display: flex;
    margin-left: 5%;
  }
  .Header h1{
    margin-left: 10px;
  }
  .Header input{
    width: 90%;
    border-radius: 30px;
  }
  .Header .HeaderSumUpd{
    display: flex;
    justify-content: space-between;
    width: 100%;
  }
  .Header .HeaderSumUpd .Upd{
    border: 0;
    align-self: center;
    margin-right: 5%;
    margin-top: 20px;
    width: 50px;
    height: 50px;
    background-image: url(/images/TrashCanGoods.svg);
    background-size: 100% 100%;
  }
  .Header .HeaderSumUpd nobr{
    color: orange;
    font-size: 20px;
  }
  .Header .HeaderSumUpd img{
    margin-top: 20px;
    width: 50px;
    height: 50px;
  }
  .Body{
    background-color: #f8f8f8;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
  .ToPay{
    width: 100px;
    height: 100px;
    position: fixed;
    bottom:0px;
  }
  .ToPay button{
    background-image: url(/images/GoToPayGoods.svg);
    background-size: 100% 100%;
    border: 0;
    width: 100%;
    height: 100%;
  }
</style>