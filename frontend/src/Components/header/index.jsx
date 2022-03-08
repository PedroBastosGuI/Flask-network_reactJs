import React from "react";
import { Container, Content } from "./styles";

import logoImag from '../../assets/logo.png';
export function Header() {
    return(
        <Container>
            <Content>
                <img src={logoImag}/>                
            </Content>
        </Container>
    );
}