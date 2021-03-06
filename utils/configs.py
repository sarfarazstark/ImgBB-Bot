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
ð Hi ! {} Welcome To @ImgbBot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """ð¤ **My Name:** [ImgBB](t.me/ImgbBot)

ð **Language:** [Python 3](https://www.python.org)

ð **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

ð¡ **Hosted On:** [Heroku](heroku.com)

ð¨âð» **Developer:** [Sarfaraz Stark](t.me/SarfarazStark)

ð¥ **Support Group:** [Blue Whale Group](https://t.me/bluewhalegroup)

ð¢ **Updates Channel:** [ðBlue Whale Bots ](https://t.me/BlueWhaleBots)


â¤ [Donate](https://www.paypal.me/SarfarazStark) (PayPal)
"""

    HELP_TEXT = """ð¡ Just Send Me Your Photo And I'll Upload it To You .  That's it

â¤ [Donate](https://www.paypal.me/SarfarazStark) (PayPal)
"""

    ERR_TEXT = "â ï¸ API Not Found"

    ERRTOKEN_TEXT = "ð¶ The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @SarfarazStarkBot",

    WAIT = "ð¬ Please Wait !!"
