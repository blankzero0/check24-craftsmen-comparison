import React, {useCallback, useEffect, useState} from 'react';
import {Craftsman} from "../api";
import CraftsmanCard from "./CraftsmanCard";

type Props = {
  plz: string
}

function CraftsmenList({ plz }: Props) {
  const [craftsmen, setCraftsmen] = useState<Craftsman[]>([]);
  const [lastRanking, setLastRanking] = useState(1);

  const fetchNextCraftsmen: (ranking: number) => Promise<[Craftsman[], number]> = useCallback(
    async (ranking: number) => {

      const nextCraftsmen: Craftsman[] = [];
      for (let i = 0; i < 10; i++) {
        ranking = ranking / 2;
        nextCraftsmen.push({
          id: Math.random(),
          name: Math.random().toString(16).slice(2),
          rankingScore: ranking,
        });
      }

      const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));
      await sleep(1000);

      return [nextCraftsmen, ranking];
    },
    [],
  );

  const updateCraftsmen = useCallback(
    async () => {
      const [nextCraftsmen, ranking] = await fetchNextCraftsmen(lastRanking);
      setCraftsmen(craftsmen => craftsmen.concat(nextCraftsmen));
      setLastRanking(ranking);
    },
    [setCraftsmen, lastRanking, setLastRanking, fetchNextCraftsmen],
  );


  useEffect(() => {
    let ignore = false;

    fetchNextCraftsmen(1).then(([nextCraftsmen, ranking]) => {
      if (ignore) return;
      setCraftsmen(craftsmen => craftsmen.concat(nextCraftsmen));
      setLastRanking(ranking);
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
      <button onClick={updateCraftsmen} className='btn btn-primary rounded-pill'>Mehr anzeigen</button>
    </div>
  );
}

export default CraftsmenList;