import { useState } from 'react';
import React from 'react';
import styles from '../styles/CardPopUp.module.css';
import PopUp from './popup'

function CardPopUp(props) {
    const [buttonPopup, setButtonPopup] = useState(false);

  return (
    <div className={styles.card}>
      <button className={styles.cardButton} onClick={() => setButtonPopup(true)}>
        {props.children}
      </button>
      {buttonPopup && (
        <PopUp trigger={buttonPopup} setTrigger={setButtonPopup}>
          <form className={styles.SearchBar}>
            <input className={styles.Input}
                type="text"
                placeholder="Search..."
            />
            <button className={styles.Button} type="submit">SELECT</button>
            </form>
        </PopUp>
      )}
    </div>
  );
}

export default CardPopUp;