import styled from './Card.module.css';

function Card(props) {
  return <div className={styled.card}>{props.children}</div>;
}

export default Card;