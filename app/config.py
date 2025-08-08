# config.py
import os
from langchain.text_splitter import Language

MAX_TOKENS = 4000  # Adjust based on your LLM's token limit
SUPPORTED_LANGUAGES = {
    'java': Language.JAVA,
    'python': Language.PYTHON,
    'javascript': Language.JS,
    'php': Language.PHP,
    'csharp': Language.CSHARP,
}

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
