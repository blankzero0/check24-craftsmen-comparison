import React from 'react';
import './SearchForm.css'

function SearchForm() {


  return (
    <main className='container d-grid gap-4'>
      <p className='my-0'>In welcher PLZ suchen Sie einen Maler?</p>
      <div className='form-floating'>
        <input type='text' id='plz' inputMode='numeric' minLength={5} maxLength={5} autoComplete='postal-code' className='form-control'/>
        <label htmlFor='plz' className='form-label'>Ihre PLZ</label>
      </div>
      <button className='btn btn-primary py-3'>Weiter</button>
    </main>
  );
}

export default SearchForm;
