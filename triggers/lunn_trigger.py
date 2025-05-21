import re
import io
from discord import File
from triggers.base import Trigger
from phrase_variations.lunn_variants import lunn_variants
from utils.cache import get_cached_media

pattern = re.compile("|".join(re.escape(v) for v in lunn_variants), re.IGNORECASE)

class LunnTeVajjTrigger(Trigger):
    def match(self, message) -> bool:
        return bool(pattern.search(message.content))
    
    async def handle(self, message, bot):
        media_bytes = get_cached_media("babbu_maan_lunn_te_vajj.mp4")
        if message.mentions:
            tagged = ", ".join(user.mention for user in message.mentions)
            msg = f"Sale {tagged} lunn te vajj" if len(message.mentions) == 1 else f"Salon {tagged} lunn te vajjo"
        else:
            msg = "Sarre lunn te vajjo"
        
        await message.channel.send(
            content=msg,
            file=File(fp=io.BytesIO(media_bytes), filename="babbu_maan_lunn_te_vajj.mp4")
        )