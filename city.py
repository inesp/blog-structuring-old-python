from zoo import Zoo
from zoo_config_builder import ZOOsConfigBuilder


class City:
    def __init__(self, name):
        self.name = name
        self.zoo = self.create_zoo("Mrs Zoo Keeper")

    def create_zoo(self, owner):
        zoo_configs = ZOOsConfigBuilder().get_config()

        config = zoo_configs.get(self.name)
        if not config or not config.get("is_open_to_public"):
            return None

        return Zoo(config["get_config"](owner, 130))
