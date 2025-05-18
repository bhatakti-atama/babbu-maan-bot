class Trigger:
    def match(self, message) -> bool:
        raise NotImplementedError("Subclasses should implement this method.")
    
    async def handle(self, message, bot):
        raise NotImplementedError("Subclasses should implement this method.")
    