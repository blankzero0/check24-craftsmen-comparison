import React from 'react';
import {Form} from "react-router-dom";

function SearchForm() {

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const originalValue = e.target.value;
    const newValue = originalValue.replace(/[^0-9]/g, '');

    if (originalValue !== newValue) {
      
    }

    e.target.value = newValue;
  };

// type = text, da für number auf der rechten Seite unerwünschte Pfeile erscheinen
  return (
    <Form method='GET' action='/listing' className='container d-grid gap-4'>
      <p className='my-0'>In welcher PLZ suchen Sie einen Handwerker?</p>
      <div className='form-floating'>
        <input type='text' id='plz' name='plz' inputMode='numeric' minLength={5} maxLength={5} autoComplete='postal-code' required className='form-control' onChange={handleInputChange}/>
        <label htmlFor='plz' className='form-label'>Ihre PLZ</label>
      </div>
      <button className='btn btn-primary py-3 rounded-pill'>SUCHEN</button>
    </Form>
  );
}

export default SearchForm;
