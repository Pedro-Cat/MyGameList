//  mygamelist.net/search/searchId
import React, { useState } from 'react';
import GameCard from "../../components/GameCard";

function SearchPage() {
  const searchInput = 'searchId';
  const [platform, setPlatform] = useState('');
  const [genre, setGenre] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    //Isso aqui armazena as variáveis, n acho q vão precisar disso mas ta ai
    if (platform !== '' && genre !== '') {
        console.log(platform, genre);
    } else if (platform !== '') {
        console.log(platform);
    } else if (genre !== '') {
        console.log(genre);
    }
  };

  const handlePlatformChange = (event) => {
    setPlatform(event.target.value);
  };

  const handleGenreChange = (event) => {
    setGenre(event.target.value);
  };

  return (
    <div className="searchPage">
      <h1 className="searchInput">"{searchInput}"</h1>
      <form className="filters" onSubmit={handleSubmit}>
        <select name="platforms" id="platform-id" value={platform} onChange={handlePlatformChange}>
          <option value="" disabled>Select Platform</option>
          <option value="PC">PC</option>
          <option value="PlayStation">PlayStation</option>
          <option value="Nintendo">Nintendo</option>
          <option value="Xbox">Xbox</option>
        </select>

        <select name="genres" id="genre-id" value={genre} onChange={handleGenreChange}>
          <option value="" disabled>Select Genre</option>
          <option value="Action">Action</option>
          <option value="FPS">FPS</option>
          <option value="RPG">RPG</option>
        </select>

        <input type="submit" name="submit" value="Apply filters" />
      </form>

      <div className='cardsSearch'>
        {/* Renderiza os cards em base nos resultados da busca */}
        <GameCard />
        <GameCard />
        <GameCard />
        <GameCard />
        <GameCard />
        <GameCard />
        <GameCard />
        <GameCard />
        <GameCard />
      </div>
    </div>
  );
}

export default SearchPage;
