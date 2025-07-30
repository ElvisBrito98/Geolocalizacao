import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import Pluscodes from './pluscodes/Pluscodes';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'leaflet/dist/leaflet.css';

  // importe a página

import { BrowserRouter, Routes, Route } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/pluscodes" element={<Pluscodes />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
