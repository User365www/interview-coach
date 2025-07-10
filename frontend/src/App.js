// import React from 'react';
// import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import { AuthProvider } from './context/AuthContext';
// import Header from './components/Header/Header';
// import HomePage from './pages/public/HomePage';
// import LoginPage from './pages/public/LoginPage';
// import CandidateListPage from './pages/private/CandidateListPage';
// import HRListPage from './pages/private/HRListPage';
// import ProfilePage from './pages/private/ProfilePage';
//
// function App() {
//   return (
//     <AuthProvider>
//       <BrowserRouter>
//         <Header />
//         <Routes>
//           <Route path="/" element={<HomePage />} />
//           <Route path="/login" element={<LoginPage />} />
//           <Route path="/candidates" element={<CandidateListPage />} />
//           <Route path="/hr-list" element={<HRListPage />} />
//           <Route path="/profile" element={<ProfilePage />} />
//         </Routes>
//       </BrowserRouter>
//     </AuthProvider>
//   );
// }
//
// export default App;
// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/public/HomePage";
import LoginPage from "./pages/public/LoginPage";
import Header from "./components/Header/Header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </Router>
  );
}

export default App;