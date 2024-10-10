from sqlalchemy import create_engine

from src.repository.entity.base_entity import Base


class PostgresConfiguration:

    def __init__(self):
        # self.engine = create_engine("postgresql://admin:admin@127.0.0.1/postgres")
        self.engine = create_engine("postgresql+psycopg2://admin:admin@database:5432/postgres")
        Base.metadata.create_all(self.engine)

    def get_engine(self):
        return self.engine
