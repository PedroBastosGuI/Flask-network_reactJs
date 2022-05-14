import axios from 'axios';
import React, {useState,useEffect} from 'react';
import {Container} from './styled';


export function Table(){

   const[data, setData] = useState("dados");

    useEffect(()=>{

        async function request(){
            const response = await axios.get("http://localhost:5000/teste");
            setData(response.data)
        };
        request();

    },[]);

    console.log(data)

    return(
        <Container>
            <table>
                <thead>
                    <tr>
                        <th>Grãos Maduros</th>
                        <th>Grãos Quebrados</th>
                        <th>Grãos Esverdeados</th>
                        <th>Grãos Queimados</th>
                        <th>Grãos Ardidos</th>
                        <th>Grãos Mofados</th>
                        <th>Grãos Amassados</th>
                        <th>Grãos Danificado por insetos</th>
                        <th>Impurezas</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>{Math.round(data.maduro * 100).toFixed(2)} %</td>
                        <td>{Math.round(data.quebrado * 100).toFixed(2)} %</td>
                        <td>{Math.round(data.esverdado * 100).toFixed(2)} %</td>
                        <td>{Math.round(data.queimado* 100).toFixed(2)} %</td>
                        <td>{Math.round(data.ardidos* 100).toFixed(2)} %</td>
                        <td>{Math.round(data.mofados* 100).toFixed(2)} %</td>
                        <td>{Math.round(data.amassados* 100).toFixed(2)} %</td>
                        <td>{Math.round(data.danificados* 100).toFixed(2)} %</td>
                        <td>{Math.round(data.impurezas* 100).toFixed(2)} %</td>
                    </tr>
                    
                </tbody>
            </table>
        </Container>
    );

}