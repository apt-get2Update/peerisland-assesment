# services/repo.py
import subprocess
import os

def clone_repository(repo_url, temp_dir):
    """Clone the repository to a temporary directory"""
    try:
        subprocess.run(['git', 'clone', repo_url, temp_dir], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_relevant_files(directory, language):
    """Get relevant files based on language"""
    extensions = {
        'python': ['.py'],
        'javascript': ['.js', '.jsx'],
        'java': ['.java'],
        'php': ['.php'],
        'csharp': ['.cs'],
    }.get(language, [])
    
    relevant_files = []
    for root, _, files in os.walk(directory):
        # Skip any directory that is a test/tests folder
        parts = root.lower().split(os.sep)
        if 'test' in parts or 'tests' in parts:
            continue
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                relevant_files.append(os.path.join(root, file))
    return relevant_files
