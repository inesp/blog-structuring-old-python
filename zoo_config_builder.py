from models import Animal


class ZOOsConfigBuilder:
    def get_config(self):
        return {
            "paris": {
                "is_open_to_public": True,
                "get_config": self._build_paris_config(["girrafe", "lion", "ape"]),
            },
            "vienna": {
                "is_open_to_public": True,
                "get_config": self._build_vienna_config(["elephant", "tucan"]),
            },
        }

    @classmethod
    def _build_paris_config(cls, animal_types):
        def _get_config(owner, zoo_size):
            animals = cls._create_animals(animal_types)
            return {
                "owner": owner,
                "zoo_size": zoo_size,
                "animals": animals,
                "most_popular_animal": "giraffe",
            }

        return _get_config

    @classmethod
    def _build_vienna_config(cls, animal_types):
        def _get_config(owner, zoo_size):
            animals = cls._create_animals(animal_types + ["pelican"])
            return {
                "owner": owner,
                "zoo_size": zoo_size,
                "animals": animals,
                "free_entrance_day": "friday",
            }

        return _get_config

    @staticmethod
    def _create_animals(animal_names):
        return [Animal(name) for name in animal_names]
