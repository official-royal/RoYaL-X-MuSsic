from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1000"))

OWNER_ID = int(getenv("OWNER_ID", ""))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/0fc760cb0777ea04b7dfe.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0fc760cb0777ea04b7dfe.jpg")

SESSION = getenv("SESSION", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/CHATTING_GRUP001")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DHIMAN_FEELINGS")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1808943146").split()))


FAILED = "https://telegra.ph/file/0fc760cb0777ea04b7dfe.jpg"
