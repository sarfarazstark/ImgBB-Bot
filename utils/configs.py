import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")


    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", None)

    OWNER_ID = int(os.environ.get("OWNER_ID", "1120608892"))
    BOT_NAME = os.environ.get("BOT_NAME", "ImgbBot")

    START_PIC = "https://i.imgur.com/zYIllxt.jpg"
    HELP_PIC = "https://i.imgur.com/AmxAlix.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @ImgbBot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """🤖 **My Name:** [ImgBB](t.me/ImgbBot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Heroku](heroku.com)

👨‍💻 **Developer:** [Sarfaraz Stark](t.me/SarfarazStark)

👥 **Support Group:** [Blue Whale Group](https://t.me/bluewhalegroup)

📢 **Updates Channel:** [🐋Blue Whale Bots ](https://t.me/BlueWhaleBots)


❤ [Donate](https://www.paypal.me/SarfarazStark) (PayPal)
"""

    HELP_TEXT = """💡 Just Send Me Your Photo And I'll Upload it To You .  That's it

❤ [Donate](https://www.paypal.me/SarfarazStark) (PayPal)
"""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @SarfarazStarkBot",

    WAIT = "💬 Please Wait !!"
