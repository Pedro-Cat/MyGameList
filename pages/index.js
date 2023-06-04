//  mygamelist.net/
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

import React, { Fragment } from 'react'
import GameCard from '../components/GameCard';
import Slider from 'react-slick';


function HomePage(){
    const settings = {
        dots: false,
        infinite: false,
        speed: 100,
        slidesToShow: 5,
        slidesToScroll: 1,
    };

    const gamelist = [
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>,
    <GameCard/>]

    return <Fragment>
        <div className='main'>
            <p className='categoryLabel'>Populares</p>
            <div className='GameSlider'> 
                <Slider {...settings}>
                    {gamelist}
                </Slider>          
            </div>
        </div>
    </Fragment>
}

export default HomePage;