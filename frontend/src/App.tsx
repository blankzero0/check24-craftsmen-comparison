import React from 'react';
import logo from './check24.svg'

function App() {
  return (
    <div>
      <header className='bg-primary text-bg-primary py-2 px-4 mb-4'>
        <h1 className='mx-4'>
          <a href='/'><img src={logo} alt='CHECK24 Logo' height='24px' className='me-3' /></a>
          Handwerkervergleich</h1>
      </header>
      <main className='container d-grid gap-4'>
        <p className='my-0'>In welcher PLZ suchen Sie einen Maler?</p>
        <div className='form-floating'>
          <input type='text' id='plz' inputMode='numeric' minLength={5} maxLength={5} autoComplete='postal-code' className='form-control'/>
          <label htmlFor='plz' className='form-label'>Ihre PLZ</label>
        </div>
        <button className='btn btn-primary'>Weiter</button>
      </main>
    </div>
  );
}

export default App;
