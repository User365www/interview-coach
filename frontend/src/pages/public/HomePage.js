import React from 'react';
import './HomePage.css';
import Header from "../../components/Header/Header";

const HomePage = () => {
    return (
        <div className="home-page">
            <div className="home-content">
                <h1>Добро пожаловать в систему собеседований</h1>
                <p>Платформа для взаимодействия кандидатов и HR-специалистов</p>
                <div className="features">
                    <div className="feature-card">
                        <h3>Для кандидатов</h3>
                        <p>Найдите лучших HR-специалистов и организуйте собеседования</p>
                    </div>
                    <div className="feature-card">
                        <h3>Для HR</h3>
                        <p>Найдите талантливых кандидатов и проводите собеседования</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default HomePage;