import factory.alchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_factory_boy_session():
    from settings import local_settings as settings
    engine = create_engine(
                url=f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
                f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.DB_NAME}",
                echo=settings.ECHO_DB_QUERIES,
                max_overflow=-1,
            )
    session = sessionmaker(bind=engine)()
    return session


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base abstract class for factories.py"""

    class Meta:
        abstract = True
        sqlalchemy_session = get_factory_boy_session()
        sqlalchemy_session_persistence = "flush"
