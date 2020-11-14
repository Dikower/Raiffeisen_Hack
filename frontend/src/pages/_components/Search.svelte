<script>

</script>
<div class="component">
    <button class="search_button"></button>
    <input type="text" class="search_input">
</div>
<style>
    .component {
        width: auto;
        height: 60px;
        display: flex;
        background: #FFFFFF;
        border-radius: 30px;
        margin: 30px 60px;
        box-shadow: 0 0 32px rgba(174, 174, 174, 0.25);
        align-items: center;
    }
    .search_input {
        border: none;
        outline: none;
        -webkit-appearance: none;
        width: 100%;
        height: 100%;
        border-radius: 30px;
        background-color: transparent;
        margin: 0;
    }
    .search_button {
        height: 26px;
        width: 30px;
        border: none;
        background: transparent url("images/search.svg") no-repeat;
        margin: 0 0 0 20px;
    }
</style>