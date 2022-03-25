import {createGlobalStyle} from "styled-components";


export const Global = createGlobalStyle`
    :root{
        --background:#06d76a;
        --shape:#ffff;
        --text-opaacity:#3d3939;
        --text-disable:#d9dbd9;
        --secondary:#05c459;
        -secondary-ligth:#9bfd93;
    }


    *{
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }


input, textarea {
    font: 400 16px "Spartan", "Helvetica Neue",helvetica,sans-serif;
}

@media (min-width: 720px){
    html{
        font-size: 93.75%;
    }
}

@media (min-width: 440px){
    html{
        font-size: 87.5%;
    }
}


body{
    background:var(--text-opaacity);
    color:#000;
    min-width: 100vw;
}


`;