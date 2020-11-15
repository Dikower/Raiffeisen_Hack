<script>
  import { params } from "@roxi/routify";
  import { onMount } from "svelte";
  import { entryCode } from "../goodsStores";
  import { goto } from "@roxi/routify";

  onMount(() => {
    entryCode.set($params["cashier"]);
    localStorage.setItem("entryCode", $params["cashier"]);
    $goto("/goods");
  });
</script>
