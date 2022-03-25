import React from 'react';
import {Container} from './styled';
import { Button } from 'react-bootstrap';
import LogoPng from '../../assets/logo.png'

export function Header(){
    return(
        <Container>
        <div className="background_image">
            <img
                src={LogoPng}
                
            />
        </div>

        </Container>
    );
};