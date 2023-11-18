import React from 'react';
import {Form} from "react-router-dom";

function SearchForm() {
  return (
    <Form method='GET' action='/listing' className='container d-grid gap-4'>
      <p className='my-0'>In welcher PLZ suchen Sie einen Handwerker?</p>
      <div className='form-floating'>
        <input type='text' id='plz' name='plz' inputMode='numeric' minLength={5} maxLength={5} autoComplete='postal-code' required className='form-control'/>
        <label htmlFor='plz' className='form-label'>Ihre PLZ</label>
      </div>
      <button className='btn btn-primary'>Weiter</button>
    </Form>
  );
}

export default SearchForm;
