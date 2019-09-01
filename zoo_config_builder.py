from dataclasses import dataclass
from typing import Callable, Dict, List

from models import Animal
from zoo import WeekDay, ZooOutline

TZooOwnerName = str
TZooSize = int
TCityName = str

@dataclass
class ZooConfiguration:
    is_open_to_public: bool
    get_config: Callable[[TZooOwnerName, TZooSize], ZooOutline]


class ZOOsConfigBuilder:
    def get_config(self) -> Dict[TCityName, ZooConfiguration]:
        return {
            "paris": ZooConfiguration(
                is_open_to_public=True,
                get_config=self._build_paris_config(["girrafe", "lion", "ape"]),
            ),
            "vienna": ZooConfiguration(
                is_open_to_public=True,
                get_config=self._build_vienna_config(["elephant", "tucan"]),
            ),
        }

    @classmethod
    def _build_paris_config(cls, animal_types: List[str]):
        def _get_config(owner: str, zoo_size: int) -> ZooOutline:
            animals = cls._create_animals(animal_types)
            return ZooOutline(
                owner_name=owner,
                size=zoo_size,
                animals=animals,
                most_popular_animal="giraffe",
            )

        return _get_config

    @classmethod
    def _build_vienna_config(cls, animal_types):
        def _get_config(owner: str, zoo_size: int) -> ZooOutline:
            animals = cls._create_animals(animal_types + ["pelican"])
            return ZooOutline(
                owner_name=owner,
                size=zoo_size,
                animals=animals,
                free_entrance_day=WeekDay.FRI,
            )

        return _get_config

    @staticmethod
    def _create_animals(animal_names):
        return [Animal(name) for name in animal_names]
