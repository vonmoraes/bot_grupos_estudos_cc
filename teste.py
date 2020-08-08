"""App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# General Config
SECRET_KEY = environ.get('BOT_TOKEN')

print(SECRET_KEY)
print(basedir)
