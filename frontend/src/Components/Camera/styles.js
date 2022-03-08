import styled from 'styled-components';


export const Container = styled.div`
align-items: center;
margin-top:4rem;
justify-content: center;
`;

export const Camera = styled.div`
display:flex;
align-items: center;
justify-content: space-between;
flex-direction: row;
`;

export const Video = styled.video`
width: 100%;
height:768px;

margin-left: 3rem;

border-radius: 0.25rem;

`;

export const Button = styled.button`

margin-right: 4rem;
padding: 1rem 1.75rem;
border-radius: 0.75rem;

background: var(--green);

font-family: 'Poppins', sans-serif;
font-size:1.25rem;
font-weight:bold;
color: var(--text);
transition: filter 0.2s;
border: 0;

&:hover{
    filter:brightness(0.7)
}
`;

export const Result = styled.div`
display:flex;
align-items: center;
justify-content: space-between;
flex-direction: row;
margin: 4rem;
`;

export const Canvas = styled.canvas`
width: 100%;
height:768px;

margin-left: 4rem;

border-radius: 0.25rem;


`;

export const ButtonClose = styled.button`
margin-left: 4rem;
margin-right: 4rem;
padding: 1rem 1.75rem;
border-radius: 0.75rem;

background: var(--green);

font-family: 'Poppins', sans-serif;
font-size:1.25rem;
font-weight:bold;
color: var(--text);
transition: filter 0.2s;
border: 0;

&:hover{
    filter:brightness(0.7)
}

`;