import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

const RegisterPage = () => {
    // Используем один объект для хранения всех данных формы
    const [formData, setFormData] = useState({
        name: '',
        type: 'candidate', // Значение по умолчанию
        description: '',
        username: '',
        password: '',
        password2: ''
    });

    const [errors, setErrors] = useState(null);
    const { loginUser } = useAuth();
    const navigate = useNavigate();

    // Универсальный обработчик для всех полей
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors(null);

        if (formData.password !== formData.password2) {
        setErrors({ password2: ["Пароли не совпадают!"] });
        return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/api/users/register/', { // Проверьте, что URL верный
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                // Отправляем все данные, кроме повторного пароля
                body: JSON.stringify({
                    name: formData.name,
                    type: formData.type,
                    description: formData.description,
                    username: formData.username,
                    password: formData.password,
                    password2: formData.password2
                })
            });

            const data = await response.json();

            if (response.status === 201) {
                // Если регистрация успешна, логинимся и переходим на главную
                await loginUser({ preventDefault: () => {}, target: { username: {value: formData.username}, password: {value: formData.password} } });
                navigate('/');
            } else {
                console.error("Ошибки валидации от сервера:", data);
            setErrors(data);
            }
        } catch (error) {
            console.error("Произошла сетевая ошибка:", error);
            setErrors({ general: ["Не удалось связаться с сервером. Попробуйте позже."] });
        }
    };

    return (
        <div>
            <h2>Регистрация нового пользователя</h2>
            {errors?.general && <p style={{ color: 'red' }}>{errors.general}</p>}
            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '400px', gap: '10px' }}>
                <input
                    type="text" name="name"
                    placeholder="Имя и Фамилия"
                    value={formData.name} onChange={handleChange} required
                />
                {errors?.name && <p style={{ color: 'red' }}>{errors.name}</p>}
                <input
                    type="text" name="username"
                    placeholder="Логин (username)"
                    value={formData.username} onChange={handleChange} required
                />
                {errors?.username && <p style={{ color: 'red' }}>{errors.username}</p>}

                <label htmlFor="type">Тип пользователя:</label>
                <select name="type" id="type" value={formData.type} onChange={handleChange}>
                    <option value="candidate">Кандидат</option>
                    <option value="hr">Сотрудник отдела кадров (HR)</option>
                    {/* Регистрацию админа обычно убирают из публичной формы */}
                    {/* <option value="admin">Администратор</option> */}
                </select>

                <label htmlFor="description">Характеристика (о себе):</label>
                <textarea
                    name="description" id="description"
                    placeholder="Расскажите немного о себе"
                    value={formData.description} onChange={handleChange}
                    rows="4"
                ></textarea>

                <input
                    type="password" name="password"
                    placeholder="Пароль (минимум 8 символов)"
                    value={formData.password} onChange={handleChange} required
                />
                {errors?.password && <p style={{ color: 'red' }}>{errors.password}</p>}
                <input
                    type="password" name="password2"
                    placeholder="Повторите пароль"
                    value={formData.password2} onChange={handleChange} required
                />
                {errors?.password2 && <p style={{ color: 'red' }}>{errors.password2}</p>}
                <button type="submit">Зарегистрироваться</button>
            </form>
            <p>
                Уже есть аккаунт? <Link to="/login">Войти</Link>
            </p>
        </div>
    );
};

export default RegisterPage;