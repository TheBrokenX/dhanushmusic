from DhanushX.core.bot import DhanushXBot
from DhanushX.core.dir import dirr
from DhanushX.core.git import git
from DhanushX.core.userbot import Userbot
from DhanushX.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = DhanushXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
