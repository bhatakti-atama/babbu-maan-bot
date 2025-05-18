from discord import File
from triggers.base import Trigger
import random
import requests
from io import BytesIO

class R34CatTrigger(Trigger):
    def match(self, message) -> bool:
        return "r34" in message.content.lower()

    async def handle(self, message, bot):
        is_static = random.random() < 0.5
        image_url = "https://cataas.com/cat" if is_static else "https://cataas.com/cat/gif"
        file_name = "cat.jpg" if is_static else "cat.gif"

        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.RequestException:
            await message.channel.send(content="Failed to fetch cat image.")
            return

        msg = "here is a cute cat"
        image_data = BytesIO(response.content)

        # No need to open with PIL if just sending raw content
        await message.channel.send(
            content=msg,
            file=File(image_data, filename=file_name)
    )   

        