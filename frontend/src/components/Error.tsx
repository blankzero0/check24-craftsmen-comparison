import React from 'react';
import HeaderBar from "./HeaderBar";

function Error() {
  return (
    <div>
      <HeaderBar/>
      <div className='container'>
        <div className='alert alert-danger'>Ein Fehler ist aufgetreten.</div>
      </div>
    </div>
  );
}

export default Error;