<script>
  import WideCard from "../../_components/WideCard.svelte";
  export let id;
  export let time;
  export let info;
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
</style>

<WideCard>
  <div>
    <div class="sub">
      Последняя транзакия
      {new Date(time).toLocaleDateString()}
    </div>
    <div class="main">{info}</div>
  </div>
  <div class="sub">ID: {id}</div>
</WideCard>
