//  mygamelist.net/
import React, { Fragment } from 'react'
import GameCard from '../components/GameCard';


function HomePage(){
    const gamelist = [
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>]
    const category = 'Popular'

    const redirecionar = '/search/' +category;

    return <Fragment>
        <div className='main'>
            {/* Cada linha é uma categoria e deve conter 6 cards */}
            <a className='categoryLabel' href={redirecionar}>{category}</a>
            <div className='cardsDisplay'> 
                {gamelist}     
            </div>
        </div>
    </Fragment>
}

export default HomePage;