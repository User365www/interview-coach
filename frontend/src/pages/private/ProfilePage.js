import React, { useState, useEffect } from 'react';
import { useAuth } from '../../context/AuthContext'; // Импортируем наш хук

const ProfilePage = () => {
    const [profile, setProfile] = useState(null);
    const [loading, setLoading] = useState(true);
    const { authTokens } = useAuth(); // Получаем токены из контекста

    useEffect(() => {
        const getProfileData = async () => {
            try {
                // ВАЖНО: Убедитесь, что URL-адрес совпадает с тем, который вы настроили в Django.
                // Скорее всего, это будет что-то вроде /api/users/profile/
                const response = await fetch('http://127.0.0.1:8000/api/users/profile/', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        // Прикрепляем токен для аутентификации - это ключ к защищенным эндпоинтам!
                        'Authorization': 'Bearer ' + String(authTokens.access)
                    }
                });

                const data = await response.json();

                if (response.ok) {
                    setProfile(data);
                } else {
                    // Можно обработать ошибку, например, если токен просрочен
                    console.error("Не удалось загрузить профиль");
                }
            } catch (error) {
                console.error("Ошибка при запросе к API:", error);
            } finally {
                setLoading(false); // В любом случае убираем загрузку
            }
        };

        if (authTokens) {
            getProfileData();
        } else {
            // Если токенов нет, сразу прекращаем загрузку
            setLoading(false);
        }

    }, []);

    if (loading) {
        return <div>Загрузка профиля...</div>;
    }

    if (!profile) {
        return <div>Не удалось загрузить данные профиля.</div>;
    }

    // Когда данные загружены, отображаем их
    return (
        <div>
            <h1>Мой профиль</h1>
            <p><strong>Имя и Фамилия:</strong> {profile.name}</p>
            <p><strong>Тип пользователя:</strong> {profile.type}</p>
            <p><strong>Характеристика:</strong> {profile.description}</p>
            <p><strong>Количество пройденных собеседований:</strong> {profile.interview_count_passed}</p>
            <p><strong>Успешные собеседования:</strong> {profile.positive_results}</p>
            <p><strong>Неудачные собеседования:</strong> {profile.negative_results}</p>
            <p><strong>Проведённые собеседования:</strong> {profile.interview_count_taken}</p>
            {/* Добавьте другие поля по необходимости */}
        </div>
    );
};

export default ProfilePage;