import os
from dotenv import load_dotenv
load_dotenv()
MODEL = "gpt-4o-mini"
API_KEY = os.getenv("OPENAI_API_KEY")
TEXT_MENTION = "STOP"
MAX_TURNS = 15