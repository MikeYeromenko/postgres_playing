import re
import uuid

from sqlalchemy import Column, text, TIMESTAMP, MetaData, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, declarative_mixin, declared_attr, sessionmaker


NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",  # Index
    "uq": "uq_%(table_name)s_%(column_0_name)s",  # UniqueConstraint
    "ck": "ck_%(table_name)s_%(constraint_name)s",  # Check
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # ForeignKey
    "pk": "pk_%(table_name)s",  # PrimaryKey
}


@declarative_mixin
class TableNameMixin:
    pattern = re.compile(r"(?<!^)(?=[A-Z])")

    @declared_attr
    def __tablename__(cls):
        return cls.pattern.sub("_", cls.__name__).lower()


@declarative_mixin
class UUIDMixin:
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, server_default=text("gen_random_uuid()"), primary_key=True)


@declarative_mixin
class CreatedAtMixin:
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("timezone('utc', now())"), nullable=False)


@declarative_mixin
class UpdatedAtMixin:
    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("timezone('utc', now())"),
        server_onupdate=text("timezone('utc', now())"),
        nullable=False,
    )


@declarative_mixin
class CreatedUpdatedMixin(CreatedAtMixin, UpdatedAtMixin):
    ...


Base = declarative_base(cls=TableNameMixin, metadata=MetaData(naming_convention=NAMING_CONVENTION))


def get_session_factory():
    from settings import local_settings as settings
    engine = create_engine(
                url=f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@"
                f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.DB_NAME}",
                echo=settings.ECHO_DB_QUERIES,
                max_overflow=-1,
            )
    session_factory = sessionmaker(bind=engine)
    return session_factory
