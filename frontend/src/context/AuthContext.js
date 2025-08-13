import React, { createContext, useContext } from 'react';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const value = { name: 'vatslav' };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    const context = useContext(AuthContext);

    if (context === null) {
        throw new Error('useAuth должен использоваться внутри AuthProvider');
    }

    return context;
};

export default AuthContext;