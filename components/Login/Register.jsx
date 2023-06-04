import React, { useState } from "react";
import styles from './Login.module.css';

export const Register = (props) => {
    const [userName, setUserName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (def) => {
        def.preventDefault();
        //Isso pega os dados enviados, como n tenho pra onde enviar deixei so como um print
        console.log(userName);
        console.log(email);
        console.log(password);
    }

    return(
        <div className={styles.formContainer}>
            <form className={styles.registerForm} onSubmit={handleSubmit}>
                <label htmlFor="username">Nome de Usuário</label>
                <input value={userName} onChange={(def) => setUserName(def.target.value)} name="username" id="username" placeholder="Nome de Usuário" required/>

                <label htmlFor="email">E-mail</label>
                <input value={email} onChange={(def) => setEmail(def.target.value)} type="email" placeholder="example@gmail.com" id="email" name="email" required/>

                <label htmlFor="password">Senha</label>
                <input value={password} onChange={(def) => setPassword(def.target.value)} type="password" placeholder="**********" id="password" name="password" required/>

                <button type="submit">Registrar</button>
            </form>

            <button className={styles.linkBtn} onClick={() => props.onFormSwitch('login')}>Já possui uma conta? Entre aqui</button>
        </div>
    )
}