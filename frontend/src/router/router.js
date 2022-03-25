import React from 'react';
import {Route,BrowserRouter} from 'react-router-dom';


import {App} from '../App';
import{Welcome} from '../Welcome';
import{Results} from'../Results'


function Routes() {
    return(
        <BrowserRouter>
            <Route />
            <Route/>
            <Route/>
        </BrowserRouter>
    );
}