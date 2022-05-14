import styled from 'styled-components';


export const Container = styled.div`
    display:flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    
`;


export const Footer = styled.div`
    margin: 1rem 0;

    button{
        width:16rem;
    height:4rem;
    border: 0;

    background:var(--secondary);
    color:var(--shape);

    font-size:1.5rem;
    font-weight: bold;
    font-family:'Spartan',sans-serif;

    border-radius: 2rem;
    transition: filter 2s;

    cursor: pointer;
    &:hover{
        filter: brightness(0.8);
    }
    }
`;


