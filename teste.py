"""App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# General Config
BOT_TOKEN = environ.get('BOT_TOKEN')
REDIS_HOST = environ.get('REDIS_HOST')
REDIS_PORT = environ.get('REDIS_PORT')
REDIS_PASSWORD = environ.get('REDIS_PASSWORD')

# PRINT ALL LOCAL SETTINGS
print("BOT_TOKEN: " + BOT_TOKEN)
print("REDIS_HOST: " + REDIS_HOST)
print("REDIS_PORT: " + REDIS_PORT)
print("REDIS_PASSWORD: " + REDIS_PASSWORD)

