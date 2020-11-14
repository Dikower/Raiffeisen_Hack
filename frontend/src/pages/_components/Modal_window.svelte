<script>
    import { fly, fade } from 'svelte/transition';
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
    export let modal = true;
    export let good;
    let new_data = {'id': good['id'], 'emoji': '', 'title': good['title'], 'price': good['price'], 'art': good['price']};
    let heading = 'Изменить товар';
    let title_placeholder = '';
    let price_placeholder = '';
    let art_placeholder = '';
    onMount(() => {
     if (good['id'] === 0) {
         title_placeholder = 'Название';
         price_placeholder = 'Цена';
         art_placeholder = 'Артикул';
         heading = 'Новая позиция'
     }
    });
function Update() {
let emoji;
switch (new_data['title']) {
case 'Пицца':
    emoji = '🍕';
    break;
case 'Мороженное':
    emoji = '🍦';
    break;
case 'Шаурма':
    emoji = '🌯';
    break;
case 'Пончики':
    emoji = '🍩';
    break;
case 'Вино':
    emoji = '🍷';
    break;
case 'Пиво':
    emoji = '🍺';
    break;
case 'Хот дог':
    emoji = '🌭';
    break;
case 'Лапша':
    emoji = '🥡';
    break;
default:
    emoji = '📦';
}
dispatch('update', {'data': {'id': new_data['id'], 'emoji': emoji, 'title': new_data['title'], 'price': new_data['price'], 'art': new_data['art']}});
modal = false;
}
</script>
<div class="component" transition:fade>
    <div class="window" transition:fly="{{ y: 200, duration: 1000 }}">
        <img src="/images/cross.svg" on:click={() => modal = false} class="close">
        <h1>{heading}</h1>
        <p class="emoji_box">{good['emoji']}</p>
        <input placeholder={title_placeholder} bind:value={new_data['title']}>
        <div class="small_input">
        <input placeholder={price_placeholder} bind:value={new_data['price']}>
            <img src="/images/Ruble.svg" alt="ruble" class="ruble_svg">
        </div>
        <div class="small_input">
        <input placeholder={art_placeholder} bind:value={new_data['art']}>
        </div>
        <button class="submit_button" on:click={Update}>Готово</button>
    </div>
</div>
<style>
    h1 {
        margin: 15px 0 5px 0;
        font-size: 30px;
    }
    input {
        border: 0;
        border-bottom: 2px solid #FF9E46;
        text-decoration: none;
        outline:none;
        width: 80%;
        border-radius: 0;
        color: #000000;
        font-family: 'Nunito', sans-serif;
        font-weight: bold;
    }
    .component {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(0, 0, 0, 0.2);
    }
    .window {
        position: fixed;
        width: 350px;
        height: 380px;
        box-shadow: 0 0 32px rgba(174, 174, 174, 0.25);
        border-radius: 13px;
        background-color: #ffffff;
        display: flex;
        align-items: center;
        flex-direction: column;
    }
    .close {
        position: absolute;
        top: 10px;
        right: 10px;
        width: 15px;
    }
    .close:hover {
        cursor: pointer;
    }
    .emoji_box {
        font-size: 50px;
        margin: 0;
    }
    .ruble_svg {
        width: 15px;
    }
    .small_input {
        width: 80%;
        display: flex;

    }
    .small_input input {
        width: 50%;
    }
    .submit_button {
        background: #FF9E46;
        border-radius: 20px;
        border: 0;
        width: 40%;
        font-family: 'Nunito', sans-serif;
        font-weight: bold;
        font-size: 18px;
        padding: 10px 20px;
        margin: 30px;
    }
</style>