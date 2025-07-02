"""from pyrogram import filters
from Shadow  import app
from Shadow .utils.https import fetch  # Import the fetch function

url_sfw = "https://api.waifu.pics/sfw/pat"

@app.on_message(filters.command("pat"))
async def slap(client, message):
    # Fetch a random slap gif
    response = await fetch.get(url_sfw)
    result = response.json()  # Parse the JSON response
    img = result["url"]
    await message.reply_animation(img)"""
