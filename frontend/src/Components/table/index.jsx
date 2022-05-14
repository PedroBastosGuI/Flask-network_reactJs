import axios from 'axios';
import React, {useState,useEffect} from 'react';



export function Table(){

   const[data, setData] = useState(null);

    useEffect(()=>{

        async function request(){
            const response = await axios.post("http://localhost:5000/");
        };
        request();

    },[]);


    return(
        <h1>oie</h1>
    );

}