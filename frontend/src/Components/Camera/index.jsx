import React,{useRef, useEffect, useState} from 'react';
import { Container,
Footer,
} from './styles';

export function CameraInit(){

    const canvasRef = useRef();
    const imageRef = useRef();
    const videoRef = useRef();

    const [result, setResult] = useState("0.00");

    useEffect(() => {
        async function getCameraStream() {
          const stream = await navigator.mediaDevices.getUserMedia({
            audio: false,
            video: true,
          });
      
          if (videoRef.current) {      
            videoRef.current.srcObject = stream;
          }
        };
      
        getCameraStream();
      }, []);


  
    async function PostImageData(){
        captureImageFromCamera();
          const formData = new FormData();
          formData.append('image', imageRef.current);
  
          await fetch('/classify', {
            method: "POST",
            body: formData,
          });
    }
      
      const playCameraStream = () => {
        if (videoRef.current) {
          videoRef.current.play();
        }
      };
    
      const captureImageFromCamera = () => {
        const context = canvasRef.current.getContext('2d');
        const { videoWidth, videoHeight } = videoRef.current;
    
        canvasRef.current.width = videoWidth;
        canvasRef.current.height = videoHeight;
    
        context.drawImage(videoRef.current, 0, 0, videoWidth, videoHeight);
    
        canvasRef.current.toBlob((blob) => {
          imageRef.current = blob;
        })
      };
    return(
        
        <Container>
          <div classname="video">
            <video ref={videoRef} onCanPlay={() => playCameraStream()} id="video" />
            <canvas ref={canvasRef} hidden></canvas>
          </div>

          <Footer>
            <button
            onClick={PostImageData}
            >
              Classificar
            </button>
          </Footer>
        </Container>
      

    );
}

