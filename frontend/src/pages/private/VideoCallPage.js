import React, { useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';

const VideoCallPage = () => {
    const { roomId } = useParams();
    const localVideoRef = useRef(null);
    const remoteVideoRef = useRef(null);
    const peerConnectionRef = useRef(null);
    const socketRef = useRef(null);
    const isInitiatorRef = useRef(false);
    const iceCandidateQueueRef = useRef([]);
    const connectionEstablishedRef = useRef(false);

    useEffect(() => {
        const setupCall = async () => {
            try {
                // ШАГ 1: ПОЛУЧАЕМ МЕДИА-ПОТОК
                const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
                if (localVideoRef.current) localVideoRef.current.srcObject = stream;

                // ШАГ 2: СОЗДАЕМ PEER CONNECTION
                peerConnectionRef.current = new RTCPeerConnection({ iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] });
                stream.getTracks().forEach(track => peerConnectionRef.current.addTrack(track, stream));

                // ШАГ 3: УСТАНАВЛИВАЕМ ОБРАБОТЧИКИ ДЛЯ PEER CONNECTION
                peerConnectionRef.current.ontrack = (event) => {
                    console.log('[WebRTC] Получен удаленный видеопоток!');
                    if (remoteVideoRef.current) remoteVideoRef.current.srcObject = event.streams[0];
                };

                peerConnectionRef.current.onicecandidate = (event) => {
                    if (event.candidate && socketRef.current?.readyState === WebSocket.OPEN) {
                        socketRef.current.send(JSON.stringify({ type: 'ice-candidate', candidate: event.candidate }));
                    }
                };

                // ШАГ 4: И ТОЛЬКО ТЕПЕРЬ ПОДКЛЮЧАЕМСЯ К WEBSOCKET
                setupWebSocket();
            } catch (error) { console.error("Ошибка при настройке звонка:", error); }
        };

        const setupWebSocket = () => {
            socketRef.current = new WebSocket(`ws://localhost:8000/ws/videocall/${roomId}/`);

            socketRef.current.onopen = () => {
                console.log('[WebSocket] Соединение установлено!');
                socketRef.current.send(JSON.stringify({ type: 'join' }));
            };

            socketRef.current.onmessage = (event) => {
                if (connectionEstablishedRef.current) return;

                const message = JSON.parse(event.data);

                if (message.type === 'join') {
                    if (!isInitiatorRef.current) {
                        isInitiatorRef.current = true;
                        console.log('[WebRTC] Кто-то присоединился. Я - инициатор. Создаю оффер...');
                        createOffer();
                    }
                } else if (message.type === 'offer') {
                    // Исправленная логика: обрабатываем оффер, ТОЛЬКО если мы НЕ инициатор.
                    if (!isInitiatorRef.current) {
                         console.log('[WebRTC] Получен оффер. Создаю ответ...');
                         handleOffer(message.offer);
                    }
                } else if (message.type === 'answer') {
                    console.log('[WebRTC] Получен ответ.');
                    handleAnswer(message.answer);
                } else if (message.type === 'ice-candidate') {
                    handleNewICECandidate(message.candidate);
                }
            };
        };

        const processIceCandidateQueue = () => {
            while (iceCandidateQueueRef.current.length) {
                const candidate = iceCandidateQueueRef.current.shift();
                console.log('[WebRTC] Добавляю кандидата из очереди.');
                handleNewICECandidate(candidate); // Используем основную функцию для обработки
            }
        };

        const handleNewICECandidate = async (candidate) => {
            // Исправленная логика: Проверяем, есть ли remoteDescription. Если нет - в очередь.
            if (!peerConnectionRef.current.remoteDescription) {
                iceCandidateQueueRef.current.push(candidate);
                return;
            }
            try {
                await peerConnectionRef.current.addIceCandidate(new RTCIceCandidate(candidate));
            } catch (error) { console.error("Ошибка при добавлении ICE кандидата:", error); }
        };

        const createOffer = async () => {
            try {
                const offer = await peerConnectionRef.current.createOffer();
                await peerConnectionRef.current.setLocalDescription(offer);
                socketRef.current.send(JSON.stringify({ type: 'offer', offer: offer }));
            } catch (error) { console.error("Ошибка при создании оффера:", error); }
        };

        const handleOffer = async (offer) => {
            try {
                await peerConnectionRef.current.setRemoteDescription(new RTCSessionDescription(offer));
                processIceCandidateQueue();
                const answer = await peerConnectionRef.current.createAnswer();
                await peerConnectionRef.current.setLocalDescription(answer);
                socketRef.current.send(JSON.stringify({ type: 'answer', answer: answer }));
            } catch (error) { console.error("Ошибка при обработке оффера:", error); }
        };

        const handleAnswer = async (answer) => {
            if (!peerConnectionRef.current) return; // Убрали лишнюю проверку
            try {
                await peerConnectionRef.current.setRemoteDescription(new RTCSessionDescription(answer));
                connectionEstablishedRef.current = true;
                processIceCandidateQueue();
            } catch (error) { console.error("Ошибка при обработке ответа:", error); }
        };

        setupCall();

        return () => {
            if (socketRef.current) socketRef.current.close();
            if (peerConnectionRef.current) peerConnectionRef.current.close();
        };
    }, [roomId]);

    // JSX БЕЗ ИЗМЕНЕНИЙ
    return (
        <div>
            <h1>Комната видеозвонка</h1>
            <p>ID комнаты: {roomId}</p>
            <div style={{'display': 'flex', 'gap': '20px'}}>
                <div>
                    <h2>Вы</h2>
                    <video ref={localVideoRef} autoPlay playsInline muted style={{ width: '400px', border: '1px solid black' }} />
                </div>
                <div>
                    <h2>Собеседник</h2>
                    <video ref={remoteVideoRef} autoPlay playsInline style={{ width: '400px', border: '1px solid black' }} />
                </div>
            </div>
        </div>
    );
};

export default VideoCallPage;