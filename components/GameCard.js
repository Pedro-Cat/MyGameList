import placeholder from '../public/placeholder.jpg'
import Link from 'next/link'
import Card from './Card/card'
import Image from 'next/image'
import styled from './Card/Card.module.css'

const GameCard = () => {
    return(
      <Card>
        {/*crdNumber é a posição do jogo, coloquei 0 como padrão*/}
        <p className={styled.cardNumber}><i>#0</i></p>
        <Link href='/game/gameId'>
          <Image src={placeholder}/>
        </Link>
        <div><a>Game Title</a></div>
      </Card>
    )
}

export default GameCard;

