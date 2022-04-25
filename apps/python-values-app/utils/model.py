from ruamel.yaml import YAML
from pydantic import BaseModel
from enum import Enum
from pydantic import validator
from pathlib import Path


yaml=YAML(typ='safe')

class Values(BaseModel):
    replicas: int
    database: Database

    @validator('database')
    def validate_selected_database(cls, database: Database)
      if database = Database.mongo:
          raise ValueError("MongoDB is not supported yet")

class Database(str, Enum):
    postgres = "postgres"
    oracle = "oracle"
    mongo = "mongo"


def load_values(path: Path) -> Values:
    data = yaml.load(path)

    Values.parse_obj(data)


## Todo: Pydantic guide, setuptools guide