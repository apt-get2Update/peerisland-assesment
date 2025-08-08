const API_BASE_URL = 'http://localhost:5000';

export default {
  async analyzeRepository(repoUrl) {
    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        sourceType: 'github',
        repositoryUrl: repoUrl
      }),
    });

    if (!response.ok) {
      throw new Error('Analysis failed');
    }

    return response.json();
  },

  async uploadFiles(files) {
    const formData = new FormData();
    files.forEach(file => formData.append('files', file));

    const response = await fetch(`${API_BASE_URL}/upload`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('File upload failed');
    }

    return response.json();
  }
};