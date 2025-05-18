import io
from discord import File
from triggers.base import Trigger
from utils.cache import get_cached_media


class BhornaTrigger(Trigger):
    def match(self, message) -> bool:
        return bool(len(message.content) > 200)
    
    async def handle(self, message, bot):
        media_bytes = get_cached_media("na_bhorya_kar.png")
        msg = "too long didn't read"
        
        await message.channel.send(
            content=msg,
            file=File(fp=io.BytesIO(media_bytes), filename="na_bhorya_kar.png")
        )