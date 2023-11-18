import React from 'react';
import {Craftsman} from "../api";
import CraftsmanCard from "./CraftsmanCard";

type Props = {
  craftsmen: Craftsman[]
}

function CraftsmenList({ craftsmen }: Props) {
  craftsmen.sort((a, b) => b.rankingScore - a.rankingScore);
  return (
    <div className='container'>
      <ul className='d-grid gap-4 px-0'>
        {craftsmen.map(craftsman => <CraftsmanCard craftsman={craftsman}/>)}
      </ul>
    </div>
  );
}

export default CraftsmenList;