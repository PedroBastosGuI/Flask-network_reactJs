import styled from "styled-components";

export const Container = styled.div`
margin-top: 2rem;

padding: 0 2rem;
table{
    width: 100%;
    th{
        color:var(--text-body);
        font-weight: 600;
        padding:1rem 2rem;
        text-align:center;
        line-height:1.5rem;
        font-size: 1.3rem;
        font-family:'Spartan',sans-serif;
        color:#ffff;
    }
    td{
        padding:1rem 2rem;
        border:0;
        background: #c1c1c1;
        color:var(--text-body);
        font-size: 1rem;
        font-family:'Spartan',sans-serif;
        color:#000;
        font-weight: 500;

    }
}
`