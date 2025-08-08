import { useState } from 'react';
import './App.css';
import AnalysisResult from './components/AnalysisResult';

const LANGUAGES = [
  { value: 'python', label: 'Python' },
  { value: 'javascript', label: 'JavaScript' },
  { value: 'java', label: 'Java' },
  { value: 'php', label: 'PHP' },
  { value: 'csharp', label: 'C#' },
];

function App() {
  const [repoUrl, setRepoUrl] = useState('');
  const [language, setLanguage] = useState('python');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleAnalyze = async () => {
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const res = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ repoUrl, language }),
      });
      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.error || 'Analysis failed');
      }
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Code Analyzer</h1>
      <div className="form">
        <input
          type="text"
          placeholder="GitHub Repository URL"
          value={repoUrl}
          onChange={e => setRepoUrl(e.target.value)}
        />
        <select value={language} onChange={e => setLanguage(e.target.value)}>
          {LANGUAGES.map(lang => (
            <option key={lang.value} value={lang.value}>{lang.label}</option>
          ))}
        </select>
        <button onClick={handleAnalyze} disabled={loading || !repoUrl}>
          {loading ? 'Analyzing...' : 'Analyze'}
        </button>
      </div>
      {error && <div className="error">{error}</div>}
      <AnalysisResult result={result} />
    </div>
  );
}

export default App;
