# CodeAnalyzer Backend

## Overview
This backend service analyzes code repositories using LLMs (Large Language Models) via the LangChain framework. It supports multiple languages and provides a structured report of the codebase.

## Architecture

```
app/
├── __init__.py           # Flask app factory, registers blueprints
├── main.py               # Entry point for running the Flask app
├── config.py             # Configuration (constants, supported languages)
├── llm.py                # LLM initialization (ChatOpenAI)
├── routes/
│   ├── __init__.py
│   ├── analyze.py        # /analyze endpoint logic
│   └── health.py         # /health endpoint logic
├── services/
│   ├── __init__.py
│   ├── repo.py           # Repo cloning and file discovery
│   ├── analysis.py       # LLM code chunk analysis and report generation
│   └── analysis_manager.py # Orchestrates the analysis workflow
├── repositories/         # Cloned repositories (auto-managed)
└── utils/
    └── __init__.py
```

## Logic Flow

1. **API Request**: Client sends a POST request to `/analyze` with a GitHub repo URL and language.
2. **Repository Handling**:
    - The backend checks if the repo is already cloned in `app/repositories/`.
    - If not, it clones the repo. If yes, it pulls the latest changes.
3. **File Discovery**:
    - Finds all relevant source files for the specified language.
4. **Chunking**:
    - Splits code files into manageable chunks using LangChain's text splitter.
5. **LLM Analysis**:
    - Each chunk is analyzed by the LLM for structure, methods, and patterns.
6. **Report Generation**:
    - Partial analyses are combined into a final structured JSON report.
7. **Response**:
    - The report is returned as a JSON response.

## Endpoints
- `POST /analyze` — Analyze a code repository
- `GET /health` — Health check

## Requirements
See `requirements.txt` for dependencies.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in `.env` or environment variables.
3. From the project root, run:
   ```bash
   python -m app.main
   ```

---

Feel free to extend the architecture for more endpoints, languages, or analysis features!
