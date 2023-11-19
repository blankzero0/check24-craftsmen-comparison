import React from 'react';
import HeaderBar from "../components/HeaderBar";
import {useSearchParams} from "react-router-dom";
import ChangeCraftman from '../components/ChangeCraftman';
import GetCraftman from '../components/GetCraftman';

function Change() {


  return (
    <div>
      <HeaderBar/>
      <ChangeCraftman/>
    </div>
  );
}

export default Change;