import os
from dotenv import load_dotenv

load_dotenv()

API_ID = "23520095"
API_HASH = "3e9f82f8ad3347cec731e8837e60fffa"
BOT_TOKEN = "5732023365:AAFdM3hPmBdlre_bfbCJmdyb7v9zc3rkWtM"
DATABASE_URL = os.getenv("DATABASE_URL", "").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
