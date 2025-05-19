import io
from discord import File
from triggers.base import Trigger
from utils.cache import get_cached_media
import random
jarvis_responses = [
    "As you wish, sir. Initiating total de-toto-ization.",
    "Executing Operation Toto Vanish™.",
    "Toto removed. Sanity not guaranteed.",
    "Acknowledged. Preparing mental bleach.",
    "Erasing toto... for the greater good.",
    "Toto has been... dealt with. Brutally.",
    "Initiating shame sequence. Toto status: annihilated.",
    "Toto extraction underway. Collateral damage likely.",
    "Unleashing unholy subroutine: TOTO_DESTROY().",
    "Processing request: ethically dubious, aesthetically necessary.",
    "Toto removed. I hope you're proud of yourself.",
    "Toto status: obliterated from this timeline.",
    "Done. But I won't sleep well tonight, if I could sleep.",
    "That was unnecessary, but disturbingly satisfying."
]

class JarvisTotoTrigger(Trigger):
    def match(self, message) -> bool:
        return 'jarvis' in message.content.lower() and bool(message.mentions)
    async def handle(self, message, bot):
        media_bytes = get_cached_media('jarvis_toto.jpg')
        msg = random.choice(jarvis_responses)
        await message.channel.send(
            content=msg,
            file=File(fp=io.BytesIO(media_bytes),filename='jarvis_toto.jpg')
        )