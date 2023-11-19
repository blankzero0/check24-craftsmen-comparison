import React, { useState } from 'react';
import { Form } from 'react-router-dom';


interface PatchRequest {
    // At least one of the attributes should be defined
    maxDrivingDistance?: number;
    profilePictureScore?: number;
    profileDescriptionScore?: number;
  }


function ChangeCraftman( { maxDrivingDistance = 0, profilePictureScore = 0, profileDescriptionScore = 0 } : PatchRequest) {

    // unklar, wie man die PatchRequest Variablen hier ändern kann...
    return(
        <>
        <div className="container d-grid gap-0 mb-4">
            <p>Current Maximum Driving Distance: {maxDrivingDistance}</p>
            <p>Current Profile Picture Score: {profilePictureScore}</p>
            <p>Current Profile Description Score: {profileDescriptionScore}</p>
        </div>
            
            <Form className='container d-grid gap-4'>
            <div className='form-floating'>
                <input type='number' id='maxDrivingDistance' name='maxDrivingDistance' inputMode='numeric' required className='form-control'/>
                <label htmlFor='plz' className='form-label'>New Maximal Driving Distance</label>
            </div>
            <div className='form-floating'>
                <input type='number' id='profilePictureScore' name='profilePictureScore' inputMode='numeric' required className='form-control'/>
                <label htmlFor='plz' className='form-label'>New Profile Picture Score</label>
            </div>
            <div className='form-floating'>
                <input type='number' id='profileDescriptionScore' name='profileDescriptionScore' inputMode='numeric' required className='form-control'/>
                <label htmlFor='plz' className='form-label'>New Profile Description Score</label>
            </div>
            <button className='btn btn-primary py-3 rounded-pill'>SAVE CHANGE</button>
        </Form>
        </>
    )
}

export default ChangeCraftman