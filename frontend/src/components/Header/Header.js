import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
    return (
        <header className="unauth-header">
            <div className="header-container">
                <Link to="/" className="logo">InterviewSystem</Link>
                <nav>
                    <ul className="nav-links">
                        <li><Link to="/">Главная</Link></li>
                        <li><Link to="/login">Вход</Link></li>
                    </ul>
                </nav>
            </div>
        </header>
    );
};

export default Header;