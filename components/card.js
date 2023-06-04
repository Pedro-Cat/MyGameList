import classes from '../styles/Card.module.css';
import { useState } from 'react';

function Card(props) {

  return (
    <div className={classes.card}>{props.children}</div>
  );
}

export default Card;