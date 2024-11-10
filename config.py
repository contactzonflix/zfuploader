import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "13323016")

API_HASH = os.environ.get("API_HASH", "68e791e616100248b0a53ae86a661a12")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7718585217:AAF7KwY_bZA7oEw6zS4zsyceOCgrHHXSRZU") 

DB_NAME = os.environ.get("DB_NAME","xxx")     

DB_URL = os.environ.get("DB_URL","xxx")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/nr6nqC4/IMG-20241030-153858-361.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6534916669 5965340120').split()]

PORT = os.environ.get("PORT", "8080")

MAX_BTN = int(os.environ.get('MAX_BTN', '5'))
PLAYERX_API_KEY = os.environ.get("PLAYERX_API_KEY", "OZXIlJDnA7XNFtLT")
STREAMWISH_API_KEY = os.environ.get("STREAMWISH_API_KEY", "12723nbydgiy65rubeisl")
VIDHIDE_API_KEY = os.environ.get("VIDHIDE_API_KEY", "33607i8rsm44jwzx1rh3b")
STREAMWISH_WATCH_URL = os.environ.get("STREAMWISH_WATCH_URL","hlswish.com") #input only FQDN without https:// ✅
STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "R794XJ7xzeuddRy")
STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "85b1adf18183b1dded50")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002397221880"))
DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
