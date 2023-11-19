import os
import subprocess
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
from urllib.request import urlopen

from db.models import Postcode, Profile, Ranking, Base

postcode_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/postcode.json'
score_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/quality_factor_score.json'
profile_url = 'https://raw.githubusercontent.com/check24-profis/hackatum-2023/main/service_provider_profile.json'

if __name__ == '__main__':
    container_id = None
    try:
        container_id = subprocess.run([
            'docker', 'run', '--rm', '-d', '-p', '5432:5432',
            '-e', 'POSTGRES_HOST_AUTH_METHOD=trust',
            '-e', 'POSTGRES_DB=craftsmen',
            'postgis/postgis'
        ], stdout=subprocess.PIPE).stdout.decode().strip()
        time.sleep(3)

        engine = create_engine('postgresql://postgres@localhost/craftsmen')
        Session = sessionmaker(bind=engine)
        session = Session()

        # create tables
        Base.metadata.create_all(bind=engine)

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

        score_response = urlopen(score_url)
        score_data = json.loads(score_response.read())
        score_for_id = {score.id: score for score in score_data}

        profile_lst = []
        for data in profile_data:
            score = score_for_id[data['id']]
            profile_lst.append(
                Profile(
                    profile_id=data['id'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    city=data['city'],
                    street=data['street'],
                    house_number=data['house_number'],
                    geog='POINT({} {})'.format(data['lon'], data['lat']),
                    max_driving_distance=data['max_driving_distance'],
                    picture_score=score['profile_picture_score'],
                    description_score=score['profile_description_score'],
                )
            )
        session.add_all(profile_lst)

        session.commit()

        session.close()

        sql_dump = subprocess.run([
            'docker', 'exec', container_id, 'pg_dump', '-U', 'postgres', 'craftsmen'
        ], stdout=subprocess.PIPE).stdout.decode()

        os.makedirs('../sql', exist_ok=True)
        with open('../sql/20-data.sql', 'w') as f:
            f.write(sql_dump)

    finally:
        if container_id:
            subprocess.run(['docker', 'stop', container_id])
