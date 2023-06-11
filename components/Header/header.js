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
                <div className={styled.search}>
                    <div className={styled.searchBar}>
                        <div className={styled.searchIcon}>
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                                <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                            </svg>
                        </div>

                        <input type='text' placeholder='Search Games'/>
                    </div>
                    <div className='searchResult'>

                    </div>
                </div>
                <div className={styled.divLogin}>
                    <div>
                        <button className={styled.linkBtn} onClick={() => [setButtonPopup(true), setCurrentForm('login')]}>
                            Login
                        </button>
                    </div>
                    <div>
                        <button className={`${styled.linkBtn} ${styled.singBtn}`} onClick={() => [setButtonPopup(true), setCurrentForm('register')]}>
                            SignUp
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