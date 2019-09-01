from typing import Dict, Optional

from zoo import Zoo
from zoo_config_builder import ZOOsConfigBuilder, ZooConfiguration

TCityName = str


class City:
    def __init__(self, name: str):
        self.name: str = name
        self.zoo: Optional[Zoo] = self.create_zoo("Mrs Zoo Keeper")

    def create_zoo(self, owner: str) -> Optional[Zoo]:
        zoo_configs: Dict[
            TCityName, ZooConfiguration
        ] = ZOOsConfigBuilder().get_config()

        config: ZooConfiguration = zoo_configs.get(self.name)
        if not config or not config.is_open_to_public:
            return None

        return Zoo(config.get_config(owner, 130))
