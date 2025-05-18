import re
import io
from discord import File
from triggers.base import Trigger
from phrase_variations.anger_variants import anger_triggers
from utils.cache import get_cached_media

pattern = re.compile(r"\b(" + "|".join(re.escape(v) for v in anger_triggers) + r")\b", re.IGNORECASE)

class HoesMadTrigger(Trigger):
    def match(self, message) -> bool:
        return bool(pattern.search(message.content))
    
    async def handle(self, message, bot):
        media_bytes = get_cached_media("hoes_mad.jpg")
        msg = f"{message.author.mention} hoe is mad"
        
        await message.channel.send(
            content=msg,
            file=File(fp=io.BytesIO(media_bytes), filename="hoes_mad.jpg")
        )