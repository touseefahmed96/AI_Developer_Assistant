# app/main.py

from fastapi import FastAPI

from app.schemas import (
    BugDetectionResponse,
    CodeCompletionResponse,
    CodeConversionResponse,
    CodeDescriptionRequest,
    CodeRequest,
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
from app.services import (
    analyze_github_issues,
    convert_natural_language_to_code,
    detect_code_bugs,
    generate_code_documentation,
    generate_project_documentation,
    generate_unit_tests,
    get_code_suggestions,
    refactor_code,
)

app = FastAPI()


@app.post("/suggestions", response_model=CodeCompletionResponse)
async def code_suggestions(request: CodeRequest):
    return get_code_suggestions(request)


@app.post("/bug-detection", response_model=BugDetectionResponse)
async def bug_detection(request: CodeRequest):
    return detect_code_bugs(request)


@app.post("/documentation", response_model=DocumentationResponse)
async def code_documentation(request: CodeRequest):
    return generate_code_documentation(request)


@app.post("/refactor", response_model=RefactoringResponse)
async def code_refactor(request: CodeRequest):
    return refactor_code(request)


@app.post("/generate-tests", response_model=UnitTestGenerationResponse)
async def generate_tests(request: CodeRequest):
    return generate_unit_tests(request)


@app.post("/convert-to-code", response_model=CodeConversionResponse)
async def convert_to_code(request: CodeDescriptionRequest):
    return convert_natural_language_to_code(request)


@app.post("/translate-code", response_model=CodeTranslationResponse)
async def translate_code(request: CodeTranslationRequest):
    return translate_code(request)


@app.post("/generate-project-doc", response_model=ProjectDocumentationResponse)
async def generate_project_doc(request: ProjectDocumentationRequest):
    return generate_project_documentation(request)


@app.post("/github-issues", response_model=GitHubIssueResponse)
async def github_issues(request: GitHubIssueRequest):
    return analyze_github_issues(request)
