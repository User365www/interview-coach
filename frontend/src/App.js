// import { AuthProvider } from './context/AuthContext';
// import React from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import HomePage from "./pages/public/HomePage";
// import LoginPage from "./pages/public/LoginPage";
// import RegisterPage from "./pages/public/RegisterPage"
// import Header from "./components/Header/Header";
// import ProfilePage from './pages/private/ProfilePage';
// import CandidateListPage from './pages/private/CandidateListPage';
// import HRListPage from './pages/private/HRListPage';
// import ReportPage from './pages/private/ReportPage';
// import PrivateRoute from './components/PrivateRoute';
//
// function App() {
//   return (
//         <Router>
//             {/*<AuthProvider>*/}
//               <Header />
//               <Routes>
//                 <Route path="/" element={<HomePage />} />
//                 <Route path="/login" element={<LoginPage />} />
//                 {/*<Route path="/register" element={<RegisterPage />} />*/}
//
//                 {/*<Route element={<PrivateRoute />}>*/}
//                 {/*    <Route path="/profile" element={<ProfilePage />} />*/}
//                 {/*    <Route path="/candidates" element={<CandidateListPage />} />*/}
//                 {/*    <Route path="/hr-list" element={<HRListPage />} />*/}
//                 {/*    <Route path="/reports" element={<ReportPage />} />*/}
//                 {/*</Route>*/}
//               </Routes>
//             {/*</AuthProvider>*/}
//         </Router>
//   );
// }
//
// export default App;

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/public/HomePage";
import LoginPage from "./pages/public/LoginPage";
import Header from "./components/Header/Header";
import PrivateRoute from './components/PrivateRoute';
import {AuthProvider} from "./context/AuthContext";
import ProfilePage from './pages/private/ProfilePage';
import CandidateListPage from './pages/private/CandidateListPage';
import HRListPage from './pages/private/HRListPage';
import ReportPage from './pages/private/ReportPage';
import RegisterPage from "./pages/public/RegisterPage";
import CreateRoomPage from "./pages/private/CreateRoomPage";
import VideoCallPage from "./pages/private/VideoCallPage";


function App() {
  return (
    <Router>
      <AuthProvider>
          <Header />
          <Routes>
            <Route element={<PrivateRoute />}>
                <Route path="/profile" element={<ProfilePage />} />
                <Route path="/candidate-list" element={<CandidateListPage />} />
                <Route path="/hr-list" element={<HRListPage />} />
                <Route path="/reports" element={<ReportPage />} />
                <Route path="/create-room" element={<CreateRoomPage />} />
                <Route path="/videocall/:roomId" element={<VideoCallPage />} />
            </Route>
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />
          </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;