//  mygamelist.net/search/searchId
import GameCard from "../../components/GameCard"

function SearchPage(){
    const searchinput = 'searchId'

    function handleClick() {
        const options = document.getElementById("options");
        if (options.style.display === "none") {
          options.style.display = "block";
        } else {
          options.style.display = "none";
        }
      }

    return(
        <div className="searchPage">
            <h1 className="searchInput">"{searchinput}"</h1> {/* Aqui deve ta o que foi pesquisado (nome/categoria do jogo), ou seja o searchId */}
            <div className="filters">
                <button id="plataformsBtn">Plataforms</button> {/*Filtros de pesquisa, me besiei nos que a gente considerou na criação do prototipo das paginas, não sei como funciona então deixei butões que não fazem nada */}
                <div id="options">
                    <p>PC</p>
                    <p>Playstation</p>
                    <p>Nintendo</p>
                    <p>Xbox</p>
                </div>
                <button id="plataformsBtn">Genre</button>
                <div id="options">
                    <p>Action</p>
                    <p>Fps</p>
                    <p>RPG...</p>
                </div>
            </div>
            <div className="cardsDisplay">
                <GameCard/> {/* Aqui vão ser um card para cada jogo que tenha um resultado para a pesquisa do usuário */}
                <GameCard/>
                <GameCard/>
                <GameCard/>
                <GameCard/>
                <GameCard/>
                <GameCard/>
                <GameCard/>
                <GameCard/>
            </div>
            <script src="./script"></script>
        </div>
    )
}

export default SearchPage;