import re
import io
from discord import File
from triggers.base import Trigger
from utils.cache import get_cached_media


class RoastTrigger(Trigger):
    def match(self, message) -> bool:
        return "shakal dekh" in message.content.lower()
    
    async def handle(self, message, bot):
        media_bytes = get_cached_media("shekhar_roasts_you.mp4")
        if message.mentions:
            tagged = ", ".join(user.mention for user in message.mentions)
            msg = f"Sale {tagged} shakal dekh apni" if len(message.mentions) == 1 else f"Salon {tagged} shakal dekho apni"
        else:
            msg = "Sarre shakal dekho apni"
        
        await message.channel.send(
            content=msg,
            file=File(fp=io.BytesIO(media_bytes), filename="babbu_maan_lunn_te_vajj.mp4")
        )