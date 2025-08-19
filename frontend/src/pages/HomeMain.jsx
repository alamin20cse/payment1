import React from 'react';
import { Outlet } from 'react-router-dom';
import NavBar from './Navbar';

const HomeMain = () => {
    return (
        <div>
            <NavBar></NavBar>

            <Outlet></Outlet>
            
        </div>
    );
};

export default HomeMain;