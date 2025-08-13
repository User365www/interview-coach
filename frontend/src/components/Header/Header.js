import React from 'react';
import { Link } from 'react-router-dom';
// import './Header.css';
import {useAuth} from "../../context/AuthContext";

const Header = () => {
    const {user} = useAuth()
    return (
        <header className="unauth-header">
            <div className="header-container">
                <Link to="/" className="logo">InterviewSystem</Link>
                <nav>
                    <ul className="nav-links">
                        <li><Link to="/">Главная</Link></li>
                        {user ? (
                            <p>Logout</p>
                        ): (
                            <li><Link to="/login">Вход</Link></li>
                        )}
                        {user && <p>Hello {user.username}</p>}
                    </ul>
                </nav>
            </div>
        </header>
    );
};

export default Header;

// import React from 'react';
// import { Link } from 'react-router-dom';
// import './Header.css';
// import { useAuth } from '../../context/AuthContext';
//
// const Header = () => {
//     const { user, logout } = useAuth();
//
//     return (
//         <header className={user ? "auth-header" : "unauth-header"}>
//             <div className="header-container">
//                 <Link to="/" className="Logo">InterviewSystem</Link>
//                 <nav>
//                     <ul className="nav-links">
//                         {user ? (
//                             <>
//                                 <li><Link to="/profile">Профиль</Link></li>
//                                 {user.role === 'candidate' && <li><Link to="/hr-list">HR List</Link></li>}
//                                 {user.role === 'hr' && <li><Link to="/candidates">Кандидаты</Link></li>}
//                                 {user.role === 'admin' && <li><Link to="/reports">Репорты</Link></li>}
//                                 <li><button onClick={logout} className="logout-button">Выйти</button></li>
//                             </>
//                         ) : (
//                             <>
//                                 <li><Link to="/">Главная</Link></li>
//                                 <li><Link to="/login">Вход</Link></li>
//                             </>
//                         )}
//                     </ul>
//                 </nav>
//             </div>
//         </header>
//     );
// };
//
// export default Header;