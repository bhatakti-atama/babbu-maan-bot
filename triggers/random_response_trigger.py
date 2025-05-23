import random
from utils.gemini import generate_response
from triggers.base import Trigger

class RandomResponseTrigger(Trigger):
    MAX_LENGTH = 500
    def match(self,message) -> bool:
        return len(message.content) <= self.MAX_LENGTH and random.randint(1,30) == 1 #respond to only 4% of the messages
    
    async def handle(self,message,bot):
        response = await generate_response(message.content)
        if response:
            await message.reply(response)
