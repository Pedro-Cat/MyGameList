//  mygamelist.net/game/gameId
import React from 'react'
import GameCard from '../../components/GameCard'

function GamePage(){
   /* Isso é so pra, dependendo do valor dentro do botão, mudar a cor dele*/
    var buttonValue = 88;
    function getButtonColorClass(value) {
        if (value > 75) {
          return 'greenBtn';
        } else if (value >= 50 && value <= 75) {
          return 'yellowBtn';
        } else {
          return 'redBtn';
        }
      }      

    return (
        <div className='gamePage'>
            <div className='leftContainer'>
                <GameCard/>
                {/* esse botão deve adicionar o jogo a sua lista */}
                <button className='addBtn'>
                    Add Game
                </button>
            </div>

            <div className='middleContainer'>
                <h1 className='gameTitle'>Nome do Jogo</h1>

                <div className='divRating'>
                    <div className="metaScore">
                        <>
                            <button className={`metaBtn ${getButtonColorClass(buttonValue)}`}>
                                <b>{buttonValue}</b>
                            </button>
                        </>
                        <p><b>Metascore</b></p>
                    </div>
                    <div className='userScore'>
                        <div className='userValue'>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
                                <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>
                            </svg> 
                            <a>8.2</a>
                        </div>
                        <a><b>User score</b></a>
                    </div>
                </div>
                <div className='divInfo'>
                    <div className='genres'>
                        <b>Genre(s):</b> Ação FPS RPG...
                    </div>
                    <div className='publisher'>
                        <b>Publisher:</b>
                    </div>
                    <div className='launchDate'>
                        <b>Launch date:</b> 11/11/11
                    </div>
                    <div className='plataforms'>
                        <b>Plataforms:</b> PC, Playstation, Xbox...
                    </div>
                </div>
            </div>

            <div className='rightContainer'>
                <b>Summary:</b>  Powered by Capcom’s proprietary RE ENGINE, the Street Fighter 6 experience spans across three distinct game modes featuring World Tour, Fighting Ground and Battle Hub. Diverse Roster of 18 Fighters. Play legendary masters and new fan favorites like Ryu, Chun-Li, Luke, Jamie, Kimberly and more in this latest edition with each character featuring striking new redesigns and exhilarating cinematic specials. Street Fighter 6 offers a highly evolved combat system with three control types - Classic, Modern and Dynamic - allowing you to quickly play to your skill level. The new Real Time Commentary Feature adds all the hype of a competitive match as well as easy-to-understand explanations about your gameplay. The Drive Gauge is a new system to manage your resources. Use it wisely in order to claim victory.
            </div>
        </div>
    );
}

export default GamePage;