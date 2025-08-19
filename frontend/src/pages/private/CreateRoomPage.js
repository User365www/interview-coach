import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext'; // Укажите правильный путь к вашему хуку/контексту

const CreateRoomPage = () => {
    const [roomName, setRoomName] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const { authTokens } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!authTokens) {
            alert("Ошибка аутентификации. Пожалуйста, попробуйте перезайти.");
            return;
        }

        setIsLoading(true);

        try {
            const response = await fetch('http://localhost:8000/api/videocalls/create-room/', { // Заметьте, мы не пишем localhost:8000, т.к. настроили proxy
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + String(authTokens.access)
                },
                body: JSON.stringify({ name: roomName })
            });

            if (response.ok) {
                const data = await response.json();
                navigate(`/videocall/${data.id}`); // Переходим в созданную комнату
            } else {
                alert("Не удалось создать комнату. Попробуйте снова.");
            }
        } catch (error) {
            console.error("Ошибка сети при создании комнаты:", error);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div>
            <h1>Создание комнаты</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Название комнаты (необязательно)"
                    value={roomName}
                    onChange={(e) => setRoomName(e.target.value)}
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Создание...' : 'Создать и войти в комнату'}
                </button>
            </form>
        </div>
    );
};

export default CreateRoomPage;