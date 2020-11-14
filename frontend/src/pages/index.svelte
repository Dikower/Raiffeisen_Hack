<script>
    import { metatags } from '@roxi/routify'
    metatags.title = 'My Routify app'
    metatags.description = 'Description coming soon...'
</script>


<main>
    <div class="head">
        <h1>FetchMasters</h1>
        <h2>Вход <nobr>/</nobr> Регистрация</h2>
    </div>
    <div class="idea">
        <div class="text">
            <p id="idea_1">FetchMasters app</p>
            <p id="idea_2">Приложение для</p>
            <p id="idea_3">вашего бизнеса</p>
            <p id="idea_4">Система быстрых переводов для индивидуальных предпренемателей</p>
        </div>
        <img src="/images/MainIdeaImg.svg" alt="img">
    </div>
    <div class="problem">

    </div>
    <div class="solution">

    </div>
    <div class="example">

    </div>
</main>

<style>
    div{
        width: 100%;
    }
    .head{   
        display: flex;
        justify-content: space-between;
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
        display: flex;
        height: 500px;
    }
    .idea p{
        margin-left: 15px;
    }
    .idea img{
        height: 500px;
    }
    .idea #idea_1{
        color: #ff9e46;
        font-weight: 700;
        font-size: 40px;
    }
    .idea #idea_2{
        font-weight: 500;
        margin-top: -50px;
        font-size: 80px;
    }
    .idea #idea_3{
        font-weight: 500;
        margin-top: -100px;
        font-size: 80px;
    }
    .idea #idea_4{
        margin-top: -60px;
        font-weight: 600;
        font-size: 25px;
        color: gray;
    }

    .problem{
        background-color:hotpink;
        height: 200px;
    }
    .solution{
        background-color: indianred;
        height: 200px;
    }
    .example{
        background-color: indigo;
        height: 200px;
    }
</style>