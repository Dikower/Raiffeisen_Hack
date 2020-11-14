<script>
  import WideCard from "../../_components/WideCard.svelte";

  export let main = "Нету";
  export let sub = "Нету";
  export let type = "percent"; // increase
  export let value = 10;

  function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
    var angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;

    return {
      x: centerX + radius * Math.cos(angleInRadians),
      y: centerY + radius * Math.sin(angleInRadians),
    };
  }

  function describeArc(x, y, radius, startAngle, endAngle) {
    var start = polarToCartesian(x, y, radius, endAngle);
    var end = polarToCartesian(x, y, radius, startAngle);

    var largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";

    var d = [
      "M",
      start.x,
      start.y,
      "A",
      radius,
      radius,
      0,
      largeArcFlag,
      0,
      end.x,
      end.y,
    ].join(" ");

    return d;
  }
</script>

<style>
  .increase {
    width: 46px;
    height: 46px;
    background-color: #ff9e46;
    color: white;
    border-radius: 50%;
    text-align: center;
    padding-top: 12px;
  }

  svg {
    display: block;
  }

  text,
  .increase {
    font-size: 16px;
    font-weight: 900;
  }

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
    <div class="main">{main}</div>
    <div class="sub">{sub}</div>
  </div>
  <div>
    {#if type === 'percent'}
      <!-- content here -->
      <!-- <div></div> -->
      <!-- {value}% -->
      <svg width="46" height="46" xmlns="http://www.w3.org/2000/svg">
        <path
          d={describeArc(23, 23, 19, 0, 180)}
          stroke="#FF9E46"
          stroke-linecap="round"
          fill="transparent"
          stroke-width="8" />
        <text y="28" x="23" text-anchor="middle">{value}%</text>
      </svg>
    {:else if type === 'increase'}
      <!-- else if content here -->
      <div class="increase">+{value}</div>
    {:else}
      <!-- else content here -->
    {/if}
  </div>
</WideCard>
