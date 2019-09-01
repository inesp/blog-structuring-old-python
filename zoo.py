from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional

from models import Animal, Person


class WeekDay(Enum):
    MON = "Monday"
    WED = "Wednesday"
    FRI = "Friday"


@dataclass
class ZooOutline:
    owner_name: str
    size: int
    animals: List[Animal]

    free_entrance_day: WeekDay = field(default=WeekDay.MON)

    most_popular_animal: Optional[str] = None


class Zoo:
    def __init__(self, zoo_outline: ZooOutline):
        self._owner_name: str = zoo_outline.owner_name
        self._free_entrance_day: WeekDay = zoo_outline.free_entrance_day

        self.animals: List[Animal] = zoo_outline.animals
        self.size: int = zoo_outline.size

        self.most_popular_animal = self._resolve_most_popular_animal(
            zoo_outline.most_popular_animal
        )

    def _resolve_most_popular_animal(self, most_popular: str):
        for animal in self.animals:
            if animal.name == most_popular:
                return animal

        return None

    def owner(self):
        return Person.query.filter(Person.name == self._owner_name).one_or_none()

    def is_entrance_free(self):
        today = datetime.today().strftime("%A")
        return today == self._free_entrance_day.value
