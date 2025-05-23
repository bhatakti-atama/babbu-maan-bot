from discord import File
from triggers.base import Trigger
from phrase_variations.lunn_variants import lunn_variants
from utils.cache import get_cached_media
from utils.add_text_to_image import AddTextToImage

class TruckedTrigger(Trigger):
    def match(self, message) -> bool:
        return "truck" in message.content.lower() and len(message.mentions) > 0

    async def handle(self, message, bot):
        text = f"@{message.mentions[0].display_name} you been trucked by @{message.author.display_name}"
        gif_bytes = get_cached_media("anime_truck.gif")
        edited_gif = AddTextToImage(gif_bytes, text, position="top")
        
        await message.channel.send(
            content= text,
            file= File(edited_gif, filename="edited_image.gif")
        )