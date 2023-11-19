import React from 'react';
import HeaderBar from "../components/HeaderBar";
import CraftsmenList from "../components/CraftsmenList";
import {useSearchParams} from "react-router-dom";
import GetCraftman from '../components/GetCraftman';

function SearchingCraftsman() {

  return (
    <div>
      <HeaderBar/>
      <GetCraftman/>
    </div>
  );
}

export default SearchingCraftsman;