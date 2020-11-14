<script>
  import BottomContainer from "../_components/BottomContainer.svelte";

  import Chart from "./_components/Chart.svelte";
  import InfoBar from "./_components/InfoBar.svelte";
  import InfoCard from "./_components/InfoCard.svelte";

  //   import bg from "../../../assets/images/anal-bg.svg";
</script>

<style>
  .anal {
    background-color: #ff9e46;
    background-image: url("/images/anal-bg.svg");
    background-size: cover;
  }

  .anal > div {
    margin: auto;
    max-width: 900px;
  }
</style>

<!-- routify:options index=3 -->
<div class="anal">
  <div>
    <Chart />
    <div style="text-align: center;margin-bottom: 17px;">
      <InfoBar>lel</InfoBar>
    </div>
    <BottomContainer>
      <InfoCard
        main="Прирост выручки"
        sub="Посмотрите количество прибыли за год"
        type="percent"
        value={75} />
      <InfoCard
        main="Новые заказы"
        sub="Посмотрите количество новых заказов за год"
        type="increase"
        value={140} />
      <InfoCard
        main="Новые заказы"
        sub="Посмотрите количество новых заказов за год"
        type="increase"
        value={140} />
      <InfoCard
        main="Новые заказы"
        sub="Посмотрите количество новых заказов за год"
        type="increase"
        value={140} />
      <InfoCard
        main="Новые заказы"
        sub="Посмотрите количество новых заказов за год"
        type="increase"
        value={140} />
    </BottomContainer>
  </div>
</div>
