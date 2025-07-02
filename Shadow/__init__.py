from SafoneAPI import SafoneAPI

from Shadow.core.bot import Hotty
from Shadow.core.dir import dirr
from Shadow.core.git import git
from Shadow.core.userbot import Userbot
from Shadow.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "Raiden_Robot"  # connect music api key "Dont change it"
