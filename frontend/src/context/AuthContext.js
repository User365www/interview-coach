// import { createContext, useContext, useState, useEffect } from 'react';
// import axios from 'axios';
//
// const AuthContext = createContext();
//
// export function AuthProvider({ children }) {
//   const [auth, setAuth] = useState({
//     isAuthenticated: false,
//     userRole: null,
//     isLoading: true
//   });
//
//   const checkAuth = async () => {
//     try {
//       const response = await axios.get('api/candidates/check/');
//       setAuth({
//         isAuthenticated: response.data.is_authenticated,
//         userRole: response.data.role,
//         isLoading: false
//       });
//     } catch (error) {
//       setAuth({
//         isAuthenticated: false,
//         userRole: null,
//         isLoading: false
//       });
//     }
//   };
//
//   useEffect(() => {
//     checkAuth();
//   }, []);
//
//   return (
//     <AuthContext.Provider value={{ auth, checkAuth }}>
//       {children}
//     </AuthContext.Provider>
//   );
// }
//
// export const useAuth = () => {
//   const context = useContext(AuthContext);
//   if (!context) {
//     throw new Error('useAuth must be used within an AuthProvider');
//   }
//   return context;
// };