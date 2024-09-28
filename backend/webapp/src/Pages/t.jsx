import React, { useRef, useState, useEffect } from 'react';
import axios from 'axios';

const CameraPage = () => {
    const videoRef = useRef(null);
    const [streaming, setStreaming] = useState(false);
    const [stream, setStream] = useState(null);

    const startCamera = async () => {
        try {
            const newStream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoRef.current.srcObject = newStream;
            setStream(newStream);
            setStreaming(true);
        } catch (err) {
            console.error("Error accessing webcam: ", err);
        }
    };

    const stopCamera = () => {
        if (stream) {
            const tracks = stream.getTracks();
            tracks.forEach(track => track.stop()); // Stop all tracks (video and audio)
            videoRef.current.srcObject = null; // Clear the video feed
            setStreaming(false);
        }
    };

    const sendFrameToServer = async () => {
        if (videoRef.current && streaming) {
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');
            canvas.width = videoRef.current.videoWidth;
            canvas.height = videoRef.current.videoHeight;
            context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
            const imageData = canvas.toDataURL('image/jpeg');

            try {
                const response = await axios.post('http://localhost:8002/get_camera_model/', {
                    image: imageData
                }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                console.log("Predictions: ", response.data.predictions);
            } catch (err) {
                console.error("Error sending frame to server: ", err);
            }
        }
    };

    useEffect(() => {
        let interval;
        if (streaming) {
            interval = setInterval(() => {
                sendFrameToServer();
            }, 1000);
        }

        return () => clearInterval(interval);
    }, [streaming]);

    // Stop camera when leaving the page
    useEffect(() => {
        return () => stopCamera();
    }, []);

    return (
        <div>
            <video ref={videoRef} autoPlay style={{ width: '100%' }} />
            <div>
                {!streaming ? (
                    <button onClick={startCamera}>Start Camera</button>
                ) : (
                    <button onClick={stopCamera}>Stop Camera</button>
                )}
            </div>
        </div>
    );
};

export default CameraPage;
