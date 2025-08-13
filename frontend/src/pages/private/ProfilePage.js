import React from 'react';
// import { useAuth } from '../../context/AuthContext';
import { Navigate } from 'react-router-dom';

const ProfilePage = () => {
  // const { auth } = useAuth();

  // if (!auth.isAuthenticated) {
  //   return <Navigate to="/login" />;
  // }

  return (
    <div className="profile-page">
      <h1>Ваш профиль</h1>
      {/*<p>Роль: {auth.userRole}</p>*/}
    </div>
  );
};

export default ProfilePage;