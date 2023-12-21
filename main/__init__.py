#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("BQAph8USqGz3pxtMMZq8Wz39pgoNNOFxlhZAaBUmw5l6url-7kyYffVdCC0buXvXqbWhF3z_-ljn_vm9zDYDZNdaz-NfQKpHkhJJmzgOrQkCI_4lEAwiJ2DfQF7pfPWvtLAlR35fwJS3ziPFuo-fdwhvS8bFpVT2uSL_E4By2NtlKNBAcTLfORCFgzBR_ymNZYrdl11cx-cvZ_4H7HIfNlS9mSXYye8q2CimmBOjwTLAoNxWHY0ist7TnmB0SrGolymjJXfjMuEvVGI40Nj-LtXCLGF-qDTPjfBa9BmoivdfXofs-a5hYkt-rFJXsWhc7Zu8rP6ehFH0LfZmm71b_W68AAAAAWqO1EoA", default=None)
FORCESUB = config("teddfffe", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
