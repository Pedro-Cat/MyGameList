import React from 'react';
import styles from '../styles/Popup2.module.css';

function PopUp(props) {
    return (props.trigger) ? (
        <div className={styles.PopUp}>
            <div className={styles.PopupInner}>
               <button className={styles.CloseBtn} onClick={() => props.setTrigger(false)}>
                    X
                </button> 
               {props.children}
            </div>
        </div>
    ) : "";
}

export default PopUp;