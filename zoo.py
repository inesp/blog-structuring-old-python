from datetime import datetime

from models import Person


class Zoo:
    def __init__(self, zoo_config):
        self._owner_name = zoo_config["owner"]
        self._free_entrance_day = zoo_config.get("free_entrance_day", "Monday")

        self.animals = zoo_config["animals"]
        self.size = zoo_config["zoo_size"]

        self.most_popular_animal = self._resolve_most_popular_animal(
            zoo_config.get("most_popular_animal")
        )

    def _resolve_most_popular_animal(self, most_popular_name):
        for animal in self.animals:
            if animal.name == most_popular_name:
                return animal

        return None

    def owner(self):
        return Person.query.filter(Person.name == self._owner_name).one_or_none()

    def is_entrance_free(self):
        today = datetime.today().strftime("%A")
        return today == self._free_entrance_day
