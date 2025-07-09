// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/public/HomePage";
import LoginPage from "./pages/public/LoginPage";
//import Header from "./components/Header";

function App() {
  return (
    <Router>
      {/*<Header /> /!* Общая шапка для всех страниц *!/*/}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </Router>
  );
}

export default App;