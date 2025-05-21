from dotenv import load_dotenv
from utils.fetch_system_prompt import read_prompt
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API = os.getenv('GEMINI_API')
SYSTEM_PROMPT=read_prompt()