import React from 'react';
import logo from "../check24.svg";

function HeaderBar() {
  return (
    <header className='bg-primary text-bg-primary py-2 px-4 mb-4'>
      <h1 className='mx-4'>
        <a href='/'><img src={logo} alt='CHECK24 Logo' height='24px' className='me-3' /></a>
        Handwerkervergleich</h1>
    </header>
  );
}

export default HeaderBar;