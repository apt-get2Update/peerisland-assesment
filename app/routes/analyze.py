# routes/analyze.py
from flask import Blueprint, request, jsonify
from app.llm import llm
from app.services.analysis_manager import AnalysisManager

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    repo_url = data.get('repoUrl')
    language = data.get('language', 'python').lower()
    manager = AnalysisManager(llm)
    result = manager.analyze_repository(repo_url, language)
    return jsonify(result)
