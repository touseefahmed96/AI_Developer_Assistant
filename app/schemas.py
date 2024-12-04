# app/schemas.py

from pydantic import BaseModel
from typing import List, Optional


class CodeRequest(BaseModel):
    code: str
    language: str


class CodeCompletionResponse(BaseModel):
    suggestion: str


class BugDetectionResponse(BaseModel):
    issues: List[str]


class DocumentationResponse(BaseModel):
    docstring: str


class RefactoringResponse(BaseModel):
    refactored_code: str


class UnitTestGenerationResponse(BaseModel):
    unit_tests: str


class CodeDescriptionRequest(BaseModel):
    description: str
    language: str


class CodeConversionResponse(BaseModel):
    code: str


class CodeTranslationRequest(BaseModel):
    code: str
    from_language: str
    to_language: str


class CodeTranslationResponse(BaseModel):
    translated_code: str


class ProjectDocumentationRequest(BaseModel):
    project_files: List[str]


class ProjectDocumentationResponse(BaseModel):
    documentation: str


class GitHubIssueRequest(BaseModel):
    owner: str
    repo: str
    state: Optional[str] = "open"  # Default to 'open'
    labels: Optional[str] = None
    assignee: Optional[str] = None
    milestone: Optional[str] = None
    per_page: Optional[int] = 10  # Default to 10 issues per page
    page: Optional[int] = 1  # Default to first page


class GitHubIssueSolution(BaseModel):
    title: str
    body: str
    solution: str


class GitHubIssueResponse(BaseModel):
    issues: List[GitHubIssueSolution]
