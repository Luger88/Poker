import configparser
import os

def update_steam_id(config_path, new_steam_id):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}")

    config = configparser.ConfigParser()
    config.read(config_path)

    if 'SteamSettings' not in config:
        config.add_section('SteamSettings')

    config['SteamSettings']['SteamID'] = new_steam_id

    with open(config_path, 'w') as configfile:
        config.write(configfile)

# Пример использования
config_path = 'd:/Steam/steamapps/common/Poker Night at the Inventory/game_config.ini'
new_steam_id = '31280'
update_steam_id(config_path, new_steam_id)
