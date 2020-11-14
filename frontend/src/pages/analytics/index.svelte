<script>
  import Chart from "./_components/Chart.svelte";
  import InfoBar from "./_components/InfoBar.svelte";
  import InfoCard from "./_components/InfoCard.svelte";
</script>

<!-- routify:options index=3 -->
<Chart />
<InfoBar>lel</InfoBar>
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
