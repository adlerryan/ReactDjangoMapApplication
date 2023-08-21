import React from 'react';
import ReactDOM from 'react-dom/client';
import axios from 'axios'; // Import Axios

import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Set the base URL for Axios requests
axios.defaults.baseURL = 'http://localhost:8000'; // Replace this with your backend server URL

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
