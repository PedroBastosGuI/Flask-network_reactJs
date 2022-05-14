import axios from 'axios';
import React, {useState,useEffect} from 'react';



export function Table(){

   const[data, setData] = useState("dados");

    useEffect(()=>{

        async function request(){
            const response = await axios.get("http://localhost:5000/teste");
            setData(response.data)
        };
        request();

    },[]);


    return(
        <div>
            <h1>Resutaldos de classificação</h1>
            <p>
                {
                    data.ardidos
                }
                </p>
        </div>
    );

}