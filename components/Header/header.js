import React from 'react'
import Link from 'next/link'
import Image from 'next/image'
import { useState } from 'react'

import logo from '../../public/logo.png'
import PopUp from '../Popup/popup'
import styled from './Header.module.css'
import { Login } from '../Login/Login'
import { Register } from '../Login/Register'

const Header = (props) => {
    const [buttonPopup, setButtonPopup] = useState(false);
    const [currentForm, setCurrentForm] = useState('login');

    const toggleForm = (formName) => {
        setCurrentForm(formName);
    };
    
    return(
        <nav className={styled.divNav}>
            <div className={styled.divHeader}>
                <div className={styled.divLogo}>
                    <Link href={"/"}>
                        <h1>
                            <Image 
                                src={logo} 
                                width={310}
                                height={45.8}
                            />
                        </h1>
                    </Link>
                </div>
                <div className={styled.divLogin}>
                    <div>
                        <button className={styled.linkBtn} onClick={() => [setButtonPopup(true), setCurrentForm('login')]}>
                            Login
                        </button>
                    </div>
                    <div>
                        <button className={`${styled.linkBtn} ${styled.singBtn}`} onClick={() => [setButtonPopup(true), setCurrentForm('register')]}>
                            SingUp
                        </button>
                    </div>
                </div>
            </div>

            <PopUp trigger={buttonPopup} setTrigger={setButtonPopup}>
            {
                currentForm === "login" ? <Login onFormSwitch={toggleForm}/> : <Register onFormSwitch={toggleForm}/>
            }
            </PopUp>
        </nav>
    );
};

export default Header;