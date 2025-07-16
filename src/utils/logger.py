import logging
import sys
from src.configs.backend import backend_settings

LOG_LEVEL = logging.INFO if backend_settings.SERVER_PROD else logging.DEBUG

LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"

logging.basicConfig(
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    stream=sys.stdout,
    force=True
)

logging.getLogger("aiogram").setLevel(LOG_LEVEL)
logging.getLogger("aiohttp").setLevel(LOG_LEVEL)

file_handler = logging.FileHandler("logs/hrbot.log")
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
file_handler.setLevel(LOG_LEVEL)
logging.getLogger().addHandler(file_handler)


logger = logging.getLogger("hrbot")
