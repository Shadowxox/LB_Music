import requests
from pyrogram import filters

from Shadow import app

sfw_actions = [
    "waifu",
    "neko",
    "shinobu",
    "bully",
    "cry",
    "hug",
    "kiss",
    "lick",
    "pat",
    "smug",
    "highfive",
    "nom",
    "bite",
    "slap",
    "wink",
    "poke",
    "dance",
    "cringe",
    "blush",
    "happy",
    "kick",
]

# Dynamically create handlers for each sfw action
for action in sfw_actions:

    @app.on_message(filters.command(action))
    def send_action_image(client, message, action=action):
        try:
            response = requests.get(f"https://api.waifu.pics/sfw/{action}")
            response.raise_for_status()
            image_url = response.json().get("url")

            if image_url:
                file_extension = image_url.split(".")[-1].lower()
                if file_extension == "gif":
                    client.send_animation(chat_id=message.chat.id, animation=image_url)
                else:
                    client.send_photo(chat_id=message.chat.id, photo=image_url)
            else:
                message.reply("Could not retrieve any image.")

        except requests.RequestException as e:
            print(f"Error in API request: {e}")
            message.reply("An error occurred while retrieving the image.")
