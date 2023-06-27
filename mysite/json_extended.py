import json
from typing import Any

class ExtendedJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, set):
            return {"__set__": True, "values": tuple(obj)}
        return super().default(obj)
    

class ExtendedJsonDecoder(json.JSONDecoder):

    def __init__(self, **kwargs):
        kwargs.setdefault("object_hook", self._object_hook)
        super().__init__(**kwargs)

    @staticmethod
    def _object_hooj(dct):
        if "__set__" in dct:
            return set(dct["values"])
        return dct




