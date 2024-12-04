# app/services.py

from app.models import CodeAssistant
from app.schemas import (
    CodeConversionResponse,
    CodeDescriptionRequest,
    CodeRequest,
    CodeCompletionResponse,
    BugDetectionResponse,
    CodeTranslationRequest,
    CodeTranslationResponse,
    DocumentationResponse,
    GitHubIssueRequest,
    GitHubIssueResponse,
    ProjectDocumentationRequest,
    ProjectDocumentationResponse,
    RefactoringResponse,
    UnitTestGenerationResponse,
)

assistant = CodeAssistant()


def get_code_suggestions(request: CodeRequest) -> CodeCompletionResponse:
    """Handles code completion requests."""
    suggestion = assistant.complete_code(request.code)
    return CodeCompletionResponse(suggestion=suggestion)


def detect_code_bugs(request: CodeRequest) -> BugDetectionResponse:
    """Handles bug detection requests."""
    issues = assistant.detect_bugs(request.code)
    return BugDetectionResponse(issues=issues)


def generate_code_documentation(request: CodeRequest) -> DocumentationResponse:
    """Handles documentation generation requests."""
    docstring = assistant.generate_documentation(request.code)
    return DocumentationResponse(docstring=docstring)


def refactor_code(request: CodeRequest) -> RefactoringResponse:
    """Handles code refactoring suggestions."""
    refactored_code = assistant.refactor_code(request.code)
    return RefactoringResponse(refactored_code=refactored_code)


def generate_unit_tests(request: CodeRequest) -> UnitTestGenerationResponse:
    """Handles unit test generation."""
    unit_tests = assistant.generate_unit_tests(request.code)
    return UnitTestGenerationResponse(unit_tests=unit_tests)


def convert_natural_language_to_code(
    request: CodeDescriptionRequest,
) -> CodeConversionResponse:
    """Handles conversion from natural language to code."""
    code = assistant.natural_language_to_code(request.description)
    return CodeConversionResponse(code=code)


def translate_code(request: CodeTranslationRequest) -> CodeTranslationResponse:
    """Handles code translation requests."""
    translated_code = assistant.translate_code(
        request.code, request.from_language, request.to_language
    )
    return CodeTranslationResponse(translated_code=translated_code)


def generate_project_documentation(
    request: ProjectDocumentationRequest,
) -> ProjectDocumentationResponse:
    """Generates documentation for the entire project."""
    documentation = assistant.generate_project_documentation(request.project_files)
    return ProjectDocumentationResponse(documentation=documentation)


def analyze_github_issues(request: GitHubIssueRequest) -> GitHubIssueResponse:
    """Fetch issues from GitHub and generate solutions for filtered issues."""
    solutions = assistant.analyze_github_issues(
        request.owner,
        request.repo,
        request.state,
        request.labels,
        request.assignee,
        request.milestone,
        request.per_page,
        request.page,
    )
    return GitHubIssueResponse(issues=solutions)
