# app/github_helper.py

import requests

from app.config import Config

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = Config.GITHUB_TOKEN  # Store your GitHub token securely


def get_github_issues(
    owner: str,
    repo: str,
    state: str = "open",
    labels: str = None,
    assignee: str = None,
    milestone: str = None,
    per_page: int = 10,
    page: int = 1,
):
    """
    Fetch filtered issues from a GitHub repository.
    :param owner: GitHub username or organization.
    :param repo: Repository name.
    :param state: The state of issues to fetch ('open', 'closed', 'all').
    :param labels: Comma-separated list of labels to filter by.
    :param assignee: GitHub username of the assignee.
    :param milestone: Milestone name or ID to filter by.
    :param per_page: Number of issues to fetch per page.
    :param page: The page number to fetch.
    :return: List of issues.
    """
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    params = {
        "state": state,
        "labels": labels,
        "assignee": assignee,
        "milestone": milestone,
        "per_page": per_page,
        "page": page,
    }

    # Remove parameters that are None
    params = {key: value for key, value in params.items() if value is not None}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  # Returns a list of issues
    else:
        return {
            "error": f"Failed to fetch issues. {response.status_code}: {response.text}"
        }
