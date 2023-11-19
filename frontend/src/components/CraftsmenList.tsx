import React, {useCallback, useEffect, useState} from 'react';
import {Craftsman, DefaultService} from "../api";
import CraftsmanCard from "./CraftsmanCard";

type Props = {
  plz: string
}

function CraftsmenList({ plz }: Props) {
  const [craftsmen, setCraftsmen] = useState<Craftsman[]>([]);
  const [below, setBelow] = useState<number | undefined>(undefined);

  const fetchNextCraftsmen = useCallback(
    async (below: number | undefined) => {
      return DefaultService.getCraftsmen(plz, below);
    },
    [plz],
  );

  const updateCraftsmen = useCallback(
    async () => {
      const response = await fetchNextCraftsmen(below);
      setCraftsmen(craftsmen => craftsmen.concat(response.craftsmen));
      setBelow(response.below);
    },
    [setCraftsmen, below, setBelow, fetchNextCraftsmen],
  );


  useEffect(() => {
    let ignore = false;

    fetchNextCraftsmen(undefined).then((response) => {
      if (ignore) return;
      setCraftsmen(craftsmen => craftsmen.concat(response.craftsmen));
      setBelow(response.below);
    });

    return () => {
      ignore = true;
    }
  }, [fetchNextCraftsmen]);


  craftsmen.sort((a, b) => b.rankingScore - a.rankingScore);
  return (
    <div className='container mb-4'>
      <ul className='d-grid gap-4 ps-0'>
        {craftsmen.map(craftsman => <CraftsmanCard key={craftsman.id} craftsman={craftsman}/>)}
      </ul>
      {below && <button onClick={updateCraftsmen} className='btn btn-primary rounded-pill'>Mehr anzeigen</button>}
    </div>
  );
}

export default CraftsmenList;