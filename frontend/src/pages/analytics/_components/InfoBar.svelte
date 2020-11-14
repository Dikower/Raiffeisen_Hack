<script>
  export let data = [
    {
      main: "No",
      sub: "info",
    },
  ];
</script>

<style>
  .info-bar {
    background: rgba(161, 161, 161, 0.4);
    border-radius: 20px;
    padding: 10px;
    display: inline-block;
    color: white;
  }

  .info-bar__item {
      text-align: center;
  }

  .main {
    font-weight: 900;
    font-size: 30px;
  }

  .sub {
    font-size: 10px;
  }
</style>

<div class="info-bar">
  {#each data as item}
    <div class="info-bar__item" >
        <div class="main">{item.main}</div>
        <div class="sub">{item.sub}</div>
    </div>
  {/each}
</div>
