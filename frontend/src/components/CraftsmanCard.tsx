import React from 'react';
import {Craftsman} from "../api";
import defaultProfile from '../default-profile.svg'

type Props = {
  craftsman: Craftsman
}

function CraftsmanCard({craftsman}: Props) {
  return (
    <ul key={craftsman.id} className='card ps-0 overflow-hidden'>
      <div className='card-body d-flex'>
        <img src={defaultProfile} alt='Profilbild' width='100px' height='100px' className='me-3' />
        <div>
          <h2 className='fs-5'>{craftsman.name}</h2>
          <p>[score = {craftsman.rankingScore}]</p>
        </div>
      </div>
    </ul>
  );
}

export default CraftsmanCard;