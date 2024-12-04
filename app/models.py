# app/models.py

from typing import List

from openai import OpenAI

from app.config import Config
from app.github_helper import get_github_issues

client = OpenAI(Config.OPENAI_API_KEY)


class CodeAssistant:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def complete_code(self, code: str) -> str:
        """Generate code completion based on a given code snippet."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that writes and completes code.",
                },
                {
                    "role": "user",
                    "content": code,
                },
            ],
            temperature=0.5,
        )

        # Extracting the code suggestion from the response
        return response.choices[0].message.content.strip()

    def detect_bugs(self, code: str) -> list:
        """Analyze code for potential bugs or issues."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that identifies bugs and issues in code.",
                },
                {
                    "role": "user",
                    "content": f"Detect bugs in the following code:\n{code}",
                },
            ],
            temperature=0.3,
        )

        # Extract the potential issues (bugs) from the assistant's response
        issues = response.choices[0].message.content.strip().split("\n")
        return issues

    def generate_documentation(self, code: str) -> str:
        """Generate a docstring for a given Python function or class."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Python documentation generator.",
                },
                {
                    "role": "user",
                    "content": f"Generate a docstring for the following Python function:\n{code}",
                },
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()

    def refactor_code(self, code: str) -> str:
        """Suggest refactoring improvements for the provided code."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python expert and a code refactorer.",
                },
                {
                    "role": "user",
                    "content": f"Refactor the following Python code to improve readability, performance, and maintainability:\n{code}",
                },
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()

    def generate_unit_tests(self, code: str) -> str:
        """Generate unit tests for the given Python function or class."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in writing unit tests using pytest.",
                },
                {
                    "role": "user",
                    "content": f"Generate unit tests for the following Python function using pytest:\n{code}",
                },
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()

    def natural_language_to_code(self, description: str) -> str:
        """Convert natural language description to code."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a Python expert that can convert natural language descriptions into Python code.",
                },
                {
                    "role": "user",
                    "content": f"Write a Python function for this task: {description}",
                },
            ],
            max_tokens=150,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()

    def translate_code(self, code: str, from_lang: str, to_lang: str) -> str:
        """Translate code from one language to another."""
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert at translating code between programming languages.",
                },
                {
                    "role": "user",
                    "content": f"Translate the following {from_lang} code to {to_lang}:\n{code}",
                },
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()

    def generate_project_documentation(self, project_files: List[str]) -> str:
        """Generate documentation for the whole project."""
        documentation = ""
        for file in project_files:
            with open(file, "r") as f:
                code = f.read()
            doc = client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in generating documentation for Python projects.",
                    },
                    {
                        "role": "user",
                        "content": f"Generate documentation for the following Python code:\n{code}",
                    },
                ],
                temperature=0.5,
            )
            documentation += doc.choices[0].content.strip() + "\n\n"
        return documentation

    def suggest_solution_for_issue(self, issue_title: str, issue_body: str) -> str:
        """Suggest solutions for a GitHub issue."""
        prompt = f"Here is a GitHub issue:\nTitle: {issue_title}\nDescription: {issue_body}\nSuggest a possible solution or code fix for the issue."

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in resolving GitHub issues and suggesting solutions.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        return response.choices[0].content.strip()

    def analyze_github_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        labels: str = None,
        assignee: str = None,
        milestone: str = None,
        per_page: int = 10,
        page: int = 1,
    ) -> dict:
        """Fetch issues from GitHub based on filters and generate solutions for each issue."""
        issues = get_github_issues(
            owner, repo, state, labels, assignee, milestone, per_page, page
        )
        if "error" in issues:
            return issues

        solutions = []
        for issue in issues:
            title = issue.get("title", "No title")
            body = issue.get("body", "No description available")
            solution = self.suggest_solution_for_issue(title, body)
            solutions.append({"title": title, "body": body, "solution": solution})
        return solutions
