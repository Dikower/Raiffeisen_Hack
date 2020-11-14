<script>
  import * as Pancake from "@sveltejs/pancake";
  let data = {
    name: "profit",
    data: [
      { x: 1, y: 0 },
      { x: 2, y: 1 },
      { x: 3, y: 4 },
      { x: 4, y: 1 },
    ],
  };

  let x1 = +Infinity;
  let x2 = -Infinity;
  let y1 = +Infinity;
  let y2 = -Infinity;

  data.data.forEach((d) => {
    if (d.x < x1) x1 = d.x;
    if (d.x > x2) x2 = d.x;
    if (d.y < y1) y1 = d.y;
    if (d.y > y2) y2 = d.y;
  });
</script>

<style>
  .chart {
    height: 60vh;
    padding: 3em 2em 2em 2em;
    /* width: 70vw; */
    margin: auto;
  }

  @media only screen and (max-width: 600px) {
    .chart {
      height: 30vh;
      width: 95vw;
      padding-right: 10px;
    }
  }

  input {
    font-size: inherit;
    font-family: inherit;
    padding: 0.5em;
  }

  .grid-line {
    position: relative;
    display: block;
  }

  .grid-line.horizontal {
    width: calc(100% + 2em);
    left: -2em;
    /* border-bottom: 1px dashed #ccc; */
  }

  .grid-line.vertical {
    /* width: calc(100% + 2em); */
    /* left: -2em; */
    border-left: 1px dashed rgba(255, 255, 255, 0.6);
    height: 100%;
  }

  .grid-line span {
    position: absolute;
    left: 0;
    bottom: 2px;
    font-family: sans-serif;
    font-size: 14px;
    color: white;
  }

  .x-label {
    position: absolute;
    width: 4em;
    left: -2em;
    bottom: -22px;
    font-family: sans-serif;
    font-size: 14px;
    color: white;
    text-align: center;
  }

  path.data {
    stroke: rgba(0, 0, 0, 0.2);
    stroke-linejoin: round;
    stroke-linecap: round;
    stroke-width: 1px;
    fill: none;
  }

  .highlight {
    stroke: white;
    fill: none;
    stroke-width: 2;
  }

  .annotation {
    position: absolute;
    white-space: nowrap;
    bottom: 1em;
    line-height: 1.2;
    background-color: rgba(255, 255, 255, 0.9);
    padding: 0.2em 0.4em;
    border-radius: 2px;
  }

  .annotation-point {
    position: absolute;
    width: 10px;
    height: 10px;
    background-color: white;
    border-radius: 50%;
    transform: translate(-50%, -50%);
  }

  .annotation strong {
    display: block;
    font-size: 20px;
  }

  .annotation span {
    display: block;
    font-size: 14px;
  }
</style>

<div class="chart">
  <Pancake.Chart {x1} {x2} {y1} {y2}>
    <Pancake.Grid horizontal count={5} let:value>
      <div class="grid-line horizontal"><span>{value}</span></div>
    </Pancake.Grid>

    <Pancake.Grid vertical count={5} let:value>
      <span class="x-label">{value}</span>
      <div class="grid-line vertical" />
    </Pancake.Grid>

    <Pancake.Svg>
      <Pancake.SvgLine data={data.data} let:d>
        <path class="highlight" {d} />
      </Pancake.SvgLine>
    </Pancake.Svg>
  </Pancake.Chart>
</div>
