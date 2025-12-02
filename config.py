from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "26106561"))
API_HASH = getenv("API_HASH", "6bf2b0a825260beafe9955ffed29f978")

BOT_TOKEN = getenv("BOT_TOKEN", "7550184093:AAEwTZ-19Vgl6ax7VfpS0Tawe43LmTu0glQ")
OWNER_ID = int(getenv("OWNER_ID", "7753899951"))

MONGO_DB_URI = "mongodb+srv://demo38174_db_user:myhTrNGcYm5zpQus@cluster0.dboqmtf.mongodb.net/?appName=Cluster0"
MUST_JOIN = getenv("MUST_JOIN", main_channel_pr)


