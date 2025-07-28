import { useState } from 'react';

function App() {
  const [form, setForm] = useState({
    tenth_cgpa: '',
    puc_cgpa: '',
    caste: 'General',
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/predict_branch", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });
    const data = await res.json();
    setResult(data.predicted_branch);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Branch Predictor</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" name="tenth_cgpa" placeholder="10th CGPA" step="0.01" onChange={handleChange} required />
        <input type="number" name="puc_cgpa" placeholder="PUC CGPA" step="0.01" onChange={handleChange} required />
        <select name="caste" onChange={handleChange}>
          <option value="General">General</option>
          <option value="OBC">OBC</option>
          <option value="SC">SC</option>
          <option value="ST">ST</option>
        </select>
        <button type="submit">Predict Branch</button>
      </form>

      {result && <h3>Suggested Branch: {result}</h3>}
    </div>
  );
}

export default App;
