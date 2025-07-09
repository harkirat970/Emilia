import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "9bdff4a34dc5e155d1240b35a0013982" # API_HASH from my.telegram.org
    API_ID = 20500424 # API_ID from my.telegram.org

    BOT_ID = 521 # BOT_ID
    BOT_USERNAME = "Emilia49bot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://manseerat685:Kirat2006Harkirat@cluster0.fmlz30j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "deadgroupchat2" # Support Chat Username
    UPDATE_CHANNEL = "detergentlab" # Update Channel Username
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp" # Start Image
    DEV_USERS = [7489809533] # Dev Users
    TOKEN = "8150036125:AAE-NAbntZU5h-c4sJesPocJkKzjGqakklI" # Bot Token from @BotFather
    CLONE_LIMIT = 0 # Number of clones your bot can make

    EVENT_LOGS = -1002344972842 # Event Logs Chat ID
    OWNER_ID = 7684887614 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Emilia" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
