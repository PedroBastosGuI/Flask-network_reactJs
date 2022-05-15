import axios from 'axios';
import React, {useState,useEffect} from 'react';
import {Container} from './styled';


export function Table(){

   const[data, setData] = useState("0.0 %");

     useEffect(()=>{

        async function request(){
            const response = await axios.get("http://localhost:5000/teste");
            setData(response.data)
            console.log(response.data)

        };
        request();

    },[]);

    console.log(data)

    return(
        <Container>
            <table>
                <thead>
                    <tr>
                        <th>Grãos Amassados</th>
                        <th>Grãos Ardidos</th>
                        <th>Grãos Chochos</th>
                        <th>Grãos Esverdeados</th>
                        <th>Grãos Germinados</th>
                        <th>Grãos Impurezas</th>
                        <th>Grãos Maduros</th>
                        <th>Grãos Mofados</th>
                        <th>Grãos Danificado por insetos</th>
                        <th>Grãos Quebrados</th>
                        <th>Grãos Queimados</th>
                    </tr>
                </thead>


                <tbody>
                    <tr>
                        <td>{data.Amassados} %</td>
                        <td>{data.Ardidos} %</td>
                        <td>{data.Chochos} %</td>
                        <td>{data.Esverdeados} %</td>
                        <td>{data.Germinados} %</td>
                        <td>{data.Impurezas} %</td>
                        <td>{data.Maduros} %</td>
                        <td>{data.Mofados} %</td>
                        <td>{data.Picados_por_inseto} %</td>
                        <td>{data.Quebrados} %</td>
                        <td>{data.Queimados} %</td>

                    </tr>
                    
                </tbody>
            </table>
        </Container>
    );

}