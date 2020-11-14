<style>
  .bottom-container {
    background: #f8f8f8;
    border-radius: 20px 20px 0px 0px;
    padding: 21px 19px;
  }
  .title {
    font-weight: bold;
    font-size: 15px;
    margin-bottom: 19px;
  }
</style>

<div class="bottom-container">
  <div class="title">Подробная информация</div>
  <slot>
    <!-- optional fallback -->
  </slot>
</div>
