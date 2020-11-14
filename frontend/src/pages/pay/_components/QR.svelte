<script>
  export let qrLink =
    "https://lh3.googleusercontent.com/proxy/SKD5-3tPCWvx_29g6TfNIPpzDFORidE3NDdUOZhdApRh0o68j2GQh_CKDHsYmjApf0nq67t6OyIjcMQhXJZB1UuZlT6VAp-YHnQ_jGgzPit9dpq6WV8f_AA";
</script>

<style>
  div {
    width: 190px;
    height: 190px;
    background-color: white;
    border-radius: 20px;
    padding: 10px;
    display: inline-block;
  }
  img {
    max-width: 100%;
    max-height: 100%;
  }
</style>

<div>
  <img
    src={qrLink || 'https://media1.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif'}
    alt="QR-код для оплаты" />
</div>
