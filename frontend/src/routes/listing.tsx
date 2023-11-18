import React from 'react';
import HeaderBar from "../components/HeaderBar";
import CraftsmenList from "../components/CraftsmenList";
import {useSearchParams} from "react-router-dom";

function Listing() {
  const [searchParams] = useSearchParams();
  const plz = searchParams.get('plz');
  if (!plz) {
    throw new Response('Missing "plz" parameter', { status: 400 });
  }

  return (
    <div>
      <HeaderBar/>
      <CraftsmenList plz={plz}/>
    </div>
  );
}

export default Listing;