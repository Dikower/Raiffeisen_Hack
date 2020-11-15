<script>
    import { metatags } from '@roxi/routify';
    import { goto } from "@roxi/routify";
    metatags.title = 'My Routify app';
    metatags.description = 'Description coming soon...';
    function GoToPay() {
        $goto("../auth");
    }
</script>


<main>
    <div class="head">
        <h1>FetchMasters</h1>
        <h2><a href="../auth">Вход</a> <nobr>/</nobr> <a href="../auth">Регистрация</a></h2>
    </div>
    <div class="idea">
        <div class="text">
            <p id="idea_1">FetchMasters app</p>
            <p id="idea_2">Приложение для</p>
            <p id="idea_3">вашего бизнеса</p>
            <p id="idea_4">Система быстрых переводов для <br/>индивидуальных предпренемателей</p>
            <button on:click={GoToPay}>Получить бесплатно</button>
        </div>
        <img src="/images/MainIdeaImg.svg" alt="img">
    </div>
    <div class="problemsolution">
        <div class="problem">
            <h1>Проблемы</h1>
            <p>Большие комиссии с платежей</p>
            <p>Потеря аудитории без наличности</p>
            <p>Отсутствие информации о продажах</p>
        </div>
        <div class="solution">
            <h1>Решения</h1>
            <p>Минимальная комиссия от СБП</p>
            <p>Возможность оплаты через смартфон</p>
            <p>Мониторинг и аналитика транзакций</p>
        </div>
    </div>
    <div class="offer">
        <div class="field"></div>
        <div class="bigfield">
            <div class="que"><h1>Что мы предлагаем?</h1></div>
            <div class="fig">
                <div id="offer_1"><h1>2</h1><h2>Красивое число</h2></div>
                <div id="offer_2"><h1>~0%</h1><h2>Комиссия за использование</h2></div>
                <div id="offer_3"><h1>3</h1><h2>Красивое число</h2></div>
            </div>
            <div class="inf"><h2 id="inf_1">Решение для малого бизнеса, которое</h2><h2 id="inf_2">позволит сократить расходы</h2></div>
        </div>
        <div class="field"></div>
    </div>



    <div class="example">
        <h1><nobr>Умная касса</nobr> всегда под рукой</h1>
        <p>Простой редактор. Умная аналитика. Фокус на UX.</p>
        <p>Все для максимального повышения эффективности Вашего</p>
        <p>бизнеса</p>
        <button on:click={GoToPay}>Получить бесплатно</button>
    </div>
    <div class="footer"></div>
</main>

<style>
    main{
        max-width: 1440px;
        margin:auto;
    }
    div{
        width: 100%;
    }
    .head{   
        display: flex;
        justify-content: space-between;
    }
    .head a{
        color: black;
    }
    .head h1{
        margin-top: 10px;
        margin-left: 15px;
        font-weight: 750;
        color: #ff9e46;
    }
    .head h2{
        margin-right: 15px;
    }
    .head nobr{
        color: #ff9e46;
    }
    @media screen and (max-width: 500px) {
        .head{
            display: flex;
            flex-direction: column;
        }
        .head h2{
            margin-top: -30px;
            align-self: flex-end;
        }
    } 
    
    .idea{
        margin-top: 10vh;
        display: flex;
        height: 100vh;
    }
    .idea p{
        margin-left: 15%;
    }
    .idea img{
        height: 500px;
    }
    .idea #idea_1{
        color: #ff9e46;
        font-weight: 700;
        font-size: 40px; 
        margin-top: 80px;
    }
    .idea #idea_2{
        font-weight: 600;
        margin-top: -50px;
        font-size: 80px;
    }
    .idea #idea_3{
        font-weight: 600;
        margin-top: -110px;
        font-size: 80px;
    }
    .idea #idea_4{
        margin-top: -80px;
        font-weight: 600;
        font-size: 25px;
        color: gray;
    }
    .idea button{
        height: 75px;
        border-radius: 100px;
        background-color: black;
        color: white;
        font-size: 25px;
        width: 300px;
        margin-left: 20%;
        margin-top: 10px;
    }
    @media screen and (max-width: 1200px) {
        .idea{
            margin-top: 10px;
            display: flex;
            flex-direction: column-reverse;
            align-items: center;
            height: 100%;
        }
        .idea img{
            width: 100%;
        }
        .idea p{
            margin-left: 5%;
        }
        .idea button{
            margin-left: 10%;
        }
    } 
    @media screen and (max-width: 700px) {
        .idea #idea_1{
            color: #ff9e46;
            font-weight: 700;
            font-size: 30px; 
            margin-top: 80px;
        }
        .idea #idea_2{
            font-weight: 600;
            margin-top: -40px;
            font-size: 60px;
        }
        .idea #idea_3{
            font-weight: 600;
            margin-top: -80px;
            font-size: 60px;
        }
        .idea #idea_4{
            margin-top: -60px;
            font-weight: 600;
            font-size: 20px;
            color: gray;
        }
    }
  












    .problemsolution{
        display: flex;
        justify-content: space-between;
    }
    .problemsolution .solution{
        text-align: right;
        margin-right: 8%;
    }
    .problemsolution .problem{
        margin-left: 8%;
    }
    .problemsolution h1{
        color: #ff9e46;
        font-size: 50px;
        font-weight: 600;
    }
    .problemsolution p{
        font-size: 20px;
        margin-top: -15px;
        font-weight: 600;
        color: gray;
    }
    @media screen and (max-width: 900px) {
        .problemsolution{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
    } 

    .offer{
        display: flex;
        flex-direction: column;
        text-align: center;
        margin-top: 200px;
        color: white;
        background-image: url("/images/BackImgInd.svg");
        background-size: 100% 100%;
    }
    @media screen and (max-width: 900px) {
        .offer{
            display: flex;
            flex-direction: column;
            text-align: center;
            margin-top: -100px;
            color: white;
            background-image: url("/images/BackImgInd.svg");
            background-size: 100% 100%;
        }
    } 
    .offer .bigfield{
        background-color: #ff9e46;
        background-image: url("/images/MaskGroup.svg");
        border-radius: 30px;
    }
    .offer .fig{
        display: flex;
    }
    .offer .que h1{
        margin-top: 60px;
        font-size:50px;
    }
    .offer .fig h1{
        font-size:80px;
        font-weight: 800;
        margin-top: 0px;
        margin-bottom: -30px;
    }
    .offer h2{
        
    }
    
    .offer .inf #inf_1{
        margin-top: 40px;
    }
    .offer .inf #inf_2{
        margin-top: -15px;
        margin-bottom: 40px;
    }
    .offer .field{
        height: 200px;

    }

    .example{
        text-align: center;
        margin-top: 150px;
    }
    @media screen and (max-width: 900px) {
        .example{
            text-align: center;
            margin-top: -100px;
        }
    } 
    .example button{
        height: 75px;
        border-radius: 100px;
        border: 0;
        background-color: black;
        color: white;
        font-size: 25px;
        width: 300px;
        margin-top: 10px;
    }
    .example nobr{
        color: #ff9e46;
    }
    .example h1{
        font-size: 50px;
    }
    .example p{
        color: gray;
        font-size: 20px;
        margin-top: -15px;
    }
    .footer{
        height: 100px;
    }
</style>