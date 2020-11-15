<script>
    import { TabsTransition } from "@roxi/routify/decorators";
    import { writable } from 'svelte/store'
    let width = writable();
</script>
<div class="window" bind:offsetWidth={$width}>
<slot decorator={TabsTransition} scoped={{width}}/>
</div>
<style>
    .window {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
</style>