from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.postcode import Postcode
from models.profile import Profile


if __name__ == '__main__':
    engine = create_engine('postgresql://craftmen:craftmen@localhost:5432/craftmen')
    Session = sessionmaker(bind=engine)
    session = Session()

    # create tables
    Postcode.__table__.create(engine)
    Profile.__table__.create(engine)

    # commit
    session.commit()

    # close session
    session.close()
