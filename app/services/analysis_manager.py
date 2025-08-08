# services/analysis_manager.py
import tempfile
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from app.config import SUPPORTED_LANGUAGES, MAX_TOKENS
from app.services.repo import clone_repository, get_relevant_files
from app.services.analysis import analyze_code_chunks, generate_final_report

class AnalysisManager:
    def __init__(self, llm):
        self.llm = llm

    def analyze_repository(self, repo_url, language):
        import hashlib
        from pathlib import Path
        language = language.lower()
        if language not in SUPPORTED_LANGUAGES:
            return {'error': 'Unsupported language'}

        # Create a unique folder name for the repo based on its URL
        repo_hash = hashlib.sha1(repo_url.encode('utf-8')).hexdigest()
        repo_dir = Path(__file__).parent.parent / 'repositories' / repo_hash
        repo_dir = repo_dir.resolve()

        # Clone if not already present, otherwise pull latest changes
        import subprocess
        if not repo_dir.exists():
            repo_dir.parent.mkdir(parents=True, exist_ok=True)
            if not clone_repository(repo_url, str(repo_dir)):
                return {'error': 'Failed to clone repository'}
        else:
            # Try to pull latest changes
            try:
                subprocess.run(['git', '-C', str(repo_dir), 'pull'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Warning: Failed to pull latest changes for {repo_url}: {e}")

        # Use a temp dir for analysis workspace (if needed for intermediate files)
        # But analysis is done on repo_dir
        relevant_files = get_relevant_files(str(repo_dir), language)
        if not relevant_files:
            return {'error': 'No relevant files found for the specified language'}
        text_splitter = RecursiveCharacterTextSplitter.from_language(
            language=SUPPORTED_LANGUAGES[language],
            chunk_size=MAX_TOKENS * 3,
            chunk_overlap=200
        )
        documents = []
        for file_path in relevant_files:
            try:
                loader = TextLoader(file_path)
                docs = loader.load_and_split(text_splitter)
                documents.extend(docs)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
                continue
        code_chunks = [doc.page_content for doc in documents]
        partial_analyses = analyze_code_chunks(code_chunks, language, self.llm)
        final_report = generate_final_report(partial_analyses, language, self.llm)
        return final_report
