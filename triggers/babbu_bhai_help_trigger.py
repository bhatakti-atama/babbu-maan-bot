from discord import Embed
from discord import Color
from triggers.base import Trigger

class BabbuBhaiHelpTrigger(Trigger):
    def match(self, message) -> bool:
        return "babbu bhai help" in message.content.lower()

    async def handle(self, message, bot):
        embed = Embed(
            title="👊 Babbu Bhai Commands Menu 👊",
            description="Here’s what your Astaad can do:",
            color= Color.orange()
        )
        embed.add_field(name="`babbu bhai help`", value="📜 Shows this list of available commands.", inline=False)
        embed.add_field(name="`lunn te vajj [@user]`", value="📹 Sends a “lunn te vajjo” video. Tag someone or let it fly for everyone.", inline=False)
        embed.add_field(name="`r34`", value="🐱 Sends a wholesome cat pic or gif to cleanse your soul.", inline=False)
        embed.add_field(name="`hoes mad`", value="🤬 Drops the legendary *hoes mad* meme whenever someone gets salty.", inline=False)
        embed.add_field(name="`jarvis [@user]`", value="🔧 Use this to 'deactivate' someone. Toto gone. Mission complete.", inline=False)
        embed.add_field(name="`na bhoreya kar`", value="🗣️ If someone writes a long essay (over 200 chars), Babbu Bhai will roast them.", inline=False)

        # No need to open with PIL if just sending raw content
        await message.channel.send(
            content= embed
    )   