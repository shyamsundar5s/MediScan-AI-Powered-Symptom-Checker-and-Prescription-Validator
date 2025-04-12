import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SymptomChecker from './components/SymptomChecker';
import PrescriptionValidator from './components/PrescriptionValidator';
import Chatbot from './components/Chatbot';
import DoctorConnect from './components/DoctorConnect';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>MediScan - AI-Powered Symptom Checker</h1>
        <Routes>
          <Route path="/symptom-checker" element={<SymptomChecker />} />
          <Route path="/prescription-validator" element={<PrescriptionValidator />} />
          <Route path="/chatbot" element={<Chatbot />} />
          <Route path="/doctor-connect" element={<DoctorConnect />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
