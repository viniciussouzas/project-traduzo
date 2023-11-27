from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, json_data: dict):
      super().__init__(json_data)

    def to_dict(self):
      return {
        "name": self.data["name"],
        "acronym": self.data["acronym"],
      }


    @classmethod
    def list_dicts(cls):
      data = cls.find()
      return [cls.to_dict(d) for d in data]
