import React from 'react';
import logo from "../check24.svg";

function HeaderBar() {
  const headerStyle = {
    backgroundColor: '#063773',
    color: 'white',
    padding: '1rem 1rem',
    marginBottom: '1rem'
  };

  return (
    <header className='text-white py-4 mb-2' style={{backgroundColor: '#063773'}}>
      <h1 className='container mb-0'>
        <a href='/'><img src={logo} alt='CHECK24 Logo' height='24px' className='me-3' /></a>
        <span className="header-title fs-3">Handwerkervergleich</span>
      </h1>
    </header>
  );
}

export default HeaderBar;