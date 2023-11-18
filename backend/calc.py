from geoalchemy2.comparator import Comparator
from geopy import distance as dist
from geoalchemy2 import functions as func, Geography
from sqlalchemy import select
from timeit import timeit

from db.connection import session

from db.postcode_model import Postcode
from db.service_provider_profile_model import ServiceProviderProfile
from db.quality_factor_score_model import QualityFactorScore


def calc(postcode: Postcode):
    lat, lon = postcode.lat, postcode.lon

    given_point = f"SRID=4326;POINT({lat} {lon})"

    response = []

    query = select(
        ServiceProviderProfile,
        func.ST_Distance(
            func.ST_GeogFromText(given_point),
            func.ST_MakePoint(ServiceProviderProfile.lon, ServiceProviderProfile.lat).cast(Geography)
        ).label('distance')
    )

    result = session.execute(query)

    for row in result:
        if row.distance > row.max_driving_distance:
            continue

        print(f"Distance to {row.first_name} {row.last_name} is too far ({row.distance}m)")

        qfc = session.query(QualityFactorScore).filter(QualityFactorScore.profile_id == row.id).first()

        profile_score = 0.4 * qfc.profile_picture_score + 0.6 * qfc.profile_description_score

        default_distance = 80
        distance_score = 1 - (row.distance / default_distance)

        if distance_score > default_distance:
            distance_weight = 0.01
        else:
            distance_weight = 0.15

        response.append(distance_weight * distance_score + (1 - distance_weight) * profile_score)

    return response


if __name__ == '__main__':
    print(len((calc(session.query(Postcode).first()))))
