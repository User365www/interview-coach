import { createContext, useContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { jwtDecode } from "jwt-decode";

const AuthContext = createContext();

export default AuthContext();

export const AuthProvider = ({ children }) => {
//   const [user, setUser] = useState(null);
//   const [token, setToken] = useState(localStorage.getItem('access_token'));
//   const navigate = useNavigate();

  // Проверка токена при инициализации
  // useEffect(() => {
  //   if (token) {
  //     const decoded = jwtDecode(token);
  //     setUser(decoded);
  //   }
  // }, [token]);

  // const login = async (username, password) => {
  //   const response = await fetch('/api/token/', {
  //     method: 'POST',
  //     headers: { 'Content-Type': 'application/json' },
  //     body: JSON.stringify({ username, password })
  //   });
  //
  //   if (response.ok) {
  //     const data = await response.json();
  //     localStorage.setItem('access_token', data.access);
  //     localStorage.setItem('refresh_token', data.refresh);
  //     setToken(data.access);
  //     navigate('/profile');
  //   } else {
  //     throw new Error('Ошибка аутентификации');
  //   }
  // };

  // const logout = () => {
  //   localStorage.removeItem('access_token');
  //   localStorage.removeItem('refresh_token');
  //   setToken(null);
  //   setUser(null);
  //   navigate('/');
  // };
  //
  // const getUserRole = () => {
  //   if (!token) return null;
  //   const decoded = jwtDecode(token);
  //   return decoded.role; // 'candidate', 'hr' или 'admin'
  // };

  return (
    <AuthContext.Provider value={{ 'name':'vatslav' }}>
      {/*, login, logout, getUserRole*/}
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);