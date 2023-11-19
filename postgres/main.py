from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
from urllib.request import urlopen

from models.postcode import Postcode
from models.profile import Profile
from models.ranking import Ranking

postcode_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/postcode.json'

if __name__ == '__main__':
    engine = create_engine('postgresql://craftmen:craftmen@localhost:5432/craftmen')
    Session = sessionmaker(bind=engine)
    session = Session()

    # create tables
    Postcode.__table__.create(engine)
    Profile.__table__.create(engine)
    Ranking.__table__.create(engine)

    # connect to json
    response = urlopen(postcode_url)
    data = json.loads(response.read())

    postcode_lst = []

    for i in data:
        postcode = i['postcode']
        geog = 'POINT({} {})'.format(i['lon'], i['lat'])
        dist_group = i['postcode_extension_distance_group'][-1]
        postcode_lst.append(Postcode(postcode=postcode, geog=geog, dist_group=dist_group))

    # insert data
    session.add_all(postcode_lst)

    # commit
    session.commit()

    # close session
    session.close()
