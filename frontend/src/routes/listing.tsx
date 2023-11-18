import React from 'react';
import HeaderBar from "../components/HeaderBar";
import CraftsmenList from "../components/CraftsmenList";
import {Craftsman} from "../api";
import {useLoaderData} from "react-router-dom";

export async function loader({ request } : { request: Request }): Promise<Craftsman[]> {
  const url = new URL(request.url);
  const plz = url.searchParams.get('plz');
  if (!plz) {
    throw new Response('Missing "plz" parameter', { status: 400 });
  }

  const response = { craftsmen: [
    {
      id: 1,
      name: 'Malerfachbetrieb Hein',
      rankingScore: 3,
    },
    {
      id: 3,
      name: 'Farbgebung Malereibetrieb',
      rankingScore: 1,
    },
    {
      id: 2,
      name: 'Malermeister Christian Neubauer',
      rankingScore: 2,
    },
  ]};
  const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));
  await sleep(1000);
  return response.craftsmen;
}

function Listing() {
  const craftsmen = useLoaderData() as Craftsman[];

  return (
    <div>
      <HeaderBar/>
      <CraftsmenList craftsmen={craftsmen}/>
    </div>
  );
}

export default Listing;