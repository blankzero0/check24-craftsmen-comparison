import React, { useState } from 'react';
import { Form } from 'react-router-dom';


interface PatchRequest {
    maxDrivingDistance?: number;
    profilePictureScore?: number;
    profileDescriptionScore?: number;
  }


function ChangeCraftman( { maxDrivingDistance = 0, profilePictureScore = 0, profileDescriptionScore = 0 } : PatchRequest) {

    const names = ["Maximale Fahrtdistanz", "Profilbild Score", "Profilbeschreibung Score"]
    const items = ["maxDrivingDistance", "profilePictureScore", "profileDescriptionScore"]
    const values = [maxDrivingDistance, profilePictureScore, profileDescriptionScore]
    // unklar, wie man die PatchRequest Variablen hier ändern kann...
    return(
        <>
            
            <Form className='container d-grid gap-4'>
            {items.map((item, index) => 
                <div>
                    <p>{names[index]}: {values[index]}</p>
                    <div className='form-floating'>
                        <input type='number' id={item} name={item} inputMode='numeric' required className='form-control'/>
                        <label htmlFor='num' className='form-label'>New Maximal Driving Distance</label>
                    </div>
                </div>
            )}
            <button className='btn btn-primary py-3 rounded-pill'>SAVE CHANGE</button>
        </Form>
        </>
    )
}

export default ChangeCraftman