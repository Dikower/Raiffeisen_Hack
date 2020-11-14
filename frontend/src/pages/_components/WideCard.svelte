<style>
  .wide-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ffffff;
    box-shadow: 0px 0px 14px rgba(219, 219, 219, 0.25);
    border-radius: 10px;
    margin-bottom: 19px;
    padding: 11px;
  }
</style>

<div class="wide-card" on:click>
  <slot>
    <!-- optional fallback -->
  </slot>
</div>
