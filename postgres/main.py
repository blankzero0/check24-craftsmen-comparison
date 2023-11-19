from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
from urllib.request import urlopen

from models.postcode import Postcode
from models.profile import Profile
from models.ranking import Ranking

postcode_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/postcode.json'
score_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/quality_factor_score.json'
profile_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/service_provider_profile.json'

if __name__ == '__main__':
    engine = create_engine('postgresql://craftmen:craftmen@localhost:5432/craftmen')
    Session = sessionmaker(bind=engine)
    session = Session()

    # create tables
    Postcode.__table__.create(engine)
    Profile.__table__.create(engine)
    Ranking.__table__.create(engine)

    # insert postcode data

    response = urlopen(postcode_url)
    data = json.loads(response.read())
    postcode_lst = []

    for i in data:
        postcode = i['postcode']
        geog = 'POINT({} {})'.format(i['lon'], i['lat'])
        dist_group = i['postcode_extension_distance_group'][-1]
        postcode_lst.append(Postcode(postcode=postcode, geog=geog, dist_group=dist_group))

    session.add_all(postcode_lst)

    # insert profile data

    profile_response = urlopen(profile_url)
    profile_data = json.loads(profile_response.read())
    profile_lst = []

    score_response = urlopen(score_url)
    score_data = json.loads(score_response.read())

    for data in profile_data:
        profile_lst.append(
            Profile(
                profile_id = data['id'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                city = data['city'],
                street = data['street'],
                house_number = data['house_number'],
                geog = 'POINT({} {})'.format(data['lon'], data['lat']),
                max_driving_distance = data['max_driving_distance']
            )
        )

    for j, k in enumerate(score_data):
        profile_lst[j].picture_score = k['profile_picture_score']
        profile_lst[j].description_score = k['profile_description_score']
    
    session.add_all(profile_lst)

    # commit
    session.commit()

    # close session
    session.close()
