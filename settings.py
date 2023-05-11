import logging
import os

# Log configuration
logger = logging.getLogger("gpt_chat")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))


# Token for ChaGPT BOT
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

# database credentials
DB_NAME = os.getenv("DB_NAME")
DB_SERVER_NAME = os.getenv("DB_SERVER_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

