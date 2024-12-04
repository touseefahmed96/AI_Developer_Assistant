# app/utils.py

import requests
from app.config import Config


def get_github_pr_info(pr_url: str):
    """Fetch pull request data from GitHub."""
    headers = {"Authorization": f"token {Config.GITHUB_API_TOKEN}"}
    response = requests.get(pr_url, headers=headers)
    return response.json()
