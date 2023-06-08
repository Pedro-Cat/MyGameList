//Isso é uma página pra quando acontecer o erro 404, aqui um link ensinando a fazer no django https://www.youtube.com/watch?v=3SKjPppM_DU

import React from 'react';
import styled from '.././styles/404.module.css'

const NoMatch = () =>{
    return(
        <div className={styled.page404}>
            <h2>Error 404: Page not found</h2>
            <p>Go back to <a href='/'>Home page</a></p>
        </div>
    )
} 

export default NoMatch;