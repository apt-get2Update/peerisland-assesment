import React from 'react';

function AnalysisResult({ result }) {
  if (!result) return null;
  return (
    <div className="result">
      <h2>Project Overview</h2>
      <p>{result.overview}</p>
      {result.architecture && <>
        <h3>Architecture</h3>
        <p>{result.architecture}</p>
      </>}
      {result.complexity && <>
        <h3>Complexity</h3>
        <p>
          <b>Overall:</b> {result.complexity.overall}<br />
          <b>Factors:</b> {result.complexity.factors?.join(', ')}
        </p>
      </>}
      <h3>Key Components</h3>
      <div className="components">
        {result.keyComponents?.map((comp, idx) => (
          <div className="component-card" key={idx}>
            <h4>{comp.name}</h4>
            <p>{comp.description}</p>
            {comp.methods && comp.methods.length > 0 && <>
              <b>Methods:</b>
              <ul>
                {comp.methods.map((m, i) => (
                  <li key={i}>
                    <code>{m.signature}</code>
                    <div>{m.description}</div>
                  </li>
                ))}
              </ul>
            </>}
          </div>
        ))}
      </div>
    </div>
  );
}

export default AnalysisResult;
