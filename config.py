import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN=os.getenv("TOKEN")
DATABASE_URL=os.getenv("URL")