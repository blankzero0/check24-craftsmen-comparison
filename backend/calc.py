from geoalchemy2.comparator import Comparator
from geopy import distance as dist
from geoalchemy2 import functions as func, Geography
from sqlalchemy import select
from timeit import timeit

from db.connection import session

from db.postcode import Postcode
from db.profile import Profile
from db.ranking import Ranking


def calc(postcode: Postcode):
    pass

if __name__ == '__main__':
    print(len((calc(session.query(Postcode).first()))))
