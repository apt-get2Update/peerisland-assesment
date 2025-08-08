
# CodeAnalyzer: Fullstack (Backend + UI)

## Overview
This project analyzes code repositories using LLMs (Large Language Models) via the LangChain framework. It supports multiple languages and provides a structured report of the codebase. It includes both a Flask backend and a modern React UI frontend.


## Architecture

```
codeAnalyzer/
├── app/                # Backend (Flask, LangChain)
│   └── ...
├── ui/                 # Frontend (React, Vite)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   └── AnalysisResult.jsx
│   │   └── ...
│   └── ...
└── ...
```

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

---

## Frontend (UI)

- Built with React (Vite)
- Located in the `ui/` folder
- Main logic in `src/App.jsx`, result display in `src/components/AnalysisResult.jsx`

### Features
- Enter a GitHub repo URL and select a language
- Click "Analyze" to trigger backend analysis
- Stylish, card-based display of project overview, architecture, complexity, and key components

### How to Run UI
1. Open a new terminal and go to the `ui` folder:
   ```bash
   cd ui
   npm install
   npm run dev
   ```
2. The UI will be available at `http://localhost:5173` (default Vite port)
3. Make sure the backend is running at `http://localhost:5000` for API calls

## Requirements
See `requirements.txt` for dependencies.


---

Feel free to extend the architecture for more endpoints, languages, or analysis features!

---

Feel free to extend the architecture for more endpoints, languages, or analysis features!
