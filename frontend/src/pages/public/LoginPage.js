import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './LoginPage.css';
import { useAuth } from '../../context/AuthContext';

const LoginPage = () => {
    const { loginUser } = useAuth();

    return (
        <div className="login-page">
            <div className="login-container">
                <h2>Вход в систему</h2>
                <form onSubmit={loginUser}>
                    <div className="form-group">
                        <label htmlFor="username">Имя пользователя</label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            placeholder="Введите имя пользователя"
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Пароль</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            placeholder="Введите пароль"
                            required
                        />
                    </div>
                    <button type="submit" className="login-button">Войти</button>
                </form>
                <div className="register-link">
                    Нет аккаунта? <Link to="/register">Зарегистрироваться</Link>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;