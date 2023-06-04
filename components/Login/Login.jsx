import React, { useState } from "react";
import styles from './Login.module.css';

export const Login = (props) => {
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (def) => {
        def.preventDefault();
        //Isso pega os dados enviados, como n tenho pra onde enviar deixei so como um print
        console.log(userName);
        console.log(password);
    }

    return(
        <div className={styles.formContainer}>
            <form className={styles.loginForm} onSubmit={handleSubmit}>
                <label htmlFor="username">Nome de Usuário</label>
                <input value={userName} onChange={(def) => setUserName(def.target.value)} name="username" id="username" placeholder="Nome de Usuário" required/>

                <label htmlFor="password">Senha</label>
                <input value={password} onChange={(def) => setPassword(def.target.value)} type="password" placeholder="**********" id="password" name="password" required/>

                <button type="submit">Log In</button>
            </form>

            <button className={styles.linkBtn} onClick={() => props.onFormSwitch('register')}>Não possui uma conta? Registre-se</button>
        </div>
    )    
}