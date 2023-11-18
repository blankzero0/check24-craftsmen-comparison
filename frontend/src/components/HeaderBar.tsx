import React from 'react';
import logo from "../check24.svg";
import {Link} from "react-router-dom";

function HeaderBar() {
  const headerStyle = {
    backgroundColor: '#063773',
    color: 'white',
    padding: '1rem 1rem',
    marginBottom: '1rem'
  };

  return (
    <header className='text-white py-4 mb-4' style={{backgroundColor: '#063773'}}>
      <h1 className='container mb-0'>
        <Link to='/'><img src={logo} alt='CHECK24 Logo' height='24px' className='me-3' /></Link>
        <span className="header-title fs-3">Handwerkervergleich</span>
      </h1>
    </header>
  );
}

export default HeaderBar;