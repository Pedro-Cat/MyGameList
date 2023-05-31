import placeholder from '../public/placeholder.jpg'
import Link from 'next/link'
import Card from './Card/card'
import Image from 'next/image'

const GameCard = () => {
    return(
      <Card>
        <Link href='/game/gameId'><Image src={placeholder}/></Link>
      </Card>
    )
}

export default GameCard;

