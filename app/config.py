# app/config.py

import os

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
