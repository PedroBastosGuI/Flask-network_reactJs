import React from 'react';
import {Container} from './styled';
import LogoPng from '../../assets/logo.png';
//import {Table} from '../../Components/table';

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