import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("DB_USER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
DBHOST = str(os.getenv("DBHOST"))

admins = [
    778981429
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
