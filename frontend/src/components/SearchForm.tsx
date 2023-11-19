import React from 'react';
import {Form} from "react-router-dom";

function SearchForm() {

  const filterNonDigits = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.target.value = e.target.value.replace(/[^0-9]/g, '');
  };

  const containerStyle = {
    alignItems: 'center',     // Vertically center the content // Horizontally center the content
    height: '70vh'           // Set the height to fill the viewport
  };

  // type=number would display spin buttons
  return (
    <Form method='GET' action='/listing' className='container d-grid' style={containerStyle}>
      <div className='d-grid gap-4'>
        <p className='mt-0 mb-0'>In welcher PLZ suchen Sie einen Handwerker?</p>
        <div className='form-floating'>
          <input type='text' id='plz' name='plz' inputMode='numeric' minLength={5} maxLength={5} autoComplete='postal-code' pattern='[0-9]{5}' required onInput={filterNonDigits} className='form-control'/>
          <label htmlFor='plz' className='form-label'>Ihre PLZ</label>
        </div>
        <button className='btn btn-primary py-3 rounded-pill'>SUCHEN</button>
      </div>
    </Form>
  );
}

export default SearchForm;
