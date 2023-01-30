from dataclasses import dataclass, field
from datetime import datetime

from typing import Any, Dict, List, Optional, Union


def deserialize(data: Union[Dict, List]) -> dataclass:
    if type(data) is dict and data.get('__type__'):
        DataClass = eval(data.pop('__type__'))
        for attr, val in data.items():
            if type(val) in (list, dict):
                data[attr] = deserialize(val)
        return DataClass(**data)
    elif type(data) is list:
        return [deserialize(item) for item in data]


class AsDictMixin:
    def _convert_isoformats_to_datetime(self) -> None:
        date_created = getattr(self, "date_created")
        date_modified = getattr(self, "date_modified")
        if type(date_created) is str:
            setattr(self, "date_created", datetime.fromisoformat(date_created))
        if type(date_modified) is str:
            setattr(self, "date_modified", datetime.fromisoformat(date_modified))

    def __post_init__(self) -> None:
        self.__type__ = type(self).__name__  # this helps with deserialization
        if hasattr(self, "date_created") and not getattr(self, "date_created"):
            setattr(self, "date_created", datetime.now())
        elif hasattr(self, "date_created"):
            self._convert_isoformats_to_datetime()

    def _serialize(self, obj: Any) -> Any:
        """
        This method is to turn nested dataclass objects into something that can be easily converted to JSON
        """
        return_object = {}
        if type(obj) in (str, int, bool, type(None)):
            return_object = obj
        elif type(obj) is datetime:
            return_object = obj.isoformat()
        elif type(obj) is list:
            return_object = [self._serialize(thing) for thing in obj]
        elif type(obj) is dict:
            return_object = {attr: self._serialize(value) for attr, value in obj.items()}
        elif object in type.mro(type(obj)):
            return_object = {attr: self._serialize(value) for attr, value in obj.__dict__.items()}
        return return_object

    @property
    def as_dict(self) -> Dict:
        return self._serialize(self)


@dataclass
class ToDoList(AsDictMixin):
    title: str
    active: bool = True
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    tasks: Optional[List] = field(default_factory=lambda: [])


@dataclass
class Task(AsDictMixin):
    name: str
    completed: bool = False
    description: str = ""
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None
