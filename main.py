from configparser import ConfigParser

from wallpaper import Wallpaper
from utils import set_wallpaper


config = ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    wallpaper = Wallpaper(
        config.get('USER', 'BIRTHDAY'),
        config.getboolean('SETTINGS', 'RAISE_ERRORS'),
        config.getboolean('SETTINGS', 'SET_DESKWALLPAPER')
    )
    wallpaper.set_theme(
        config.get('THEME', 'BG_COLOR'),
        config.get('THEME', 'CHECKBOX_PX'),
        config.get('THEME', 'ON_STATE'),
        config.get('THEME', 'OFF_STATE'),
        config.get('THEME', 'OUTLINE_COLOR'),
        config.get('THEME', 'PADDING_PERCENT')
    )
    wallpaper.set_font(
        config.get('FONT', 'FONT_PATH'),
        config.get('FONT', 'TEXT'),
        config.get('FONT', 'TEXT_SIZE'),
        config.get('FONT', 'TEXT_COLOR')
    )
    wallpaper.make_wallpaper()
    wallpaper.save()

    if wallpaper.set_wallpaper == True:
        set_wallpaper(wallpaper.path)

