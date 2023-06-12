//  mygamelist.net/
import React, { Fragment } from 'react'
import GameCard from '../components/GameCard';

import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

function HomePage(){
    var settings = {
        dots: false,
        infinite: false,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 1,
        initialSlide: 0,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
              infinite: true,
              dots: true
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
              initialSlide: 2
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      };

    const gamelist = [
    <GameCard/>,
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
            <Slider {...settings}>
                {gamelist}    
            </Slider>
                 
            </div>
        </div>
    </Fragment>
}

export default HomePage;