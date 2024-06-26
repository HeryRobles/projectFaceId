import cv2


class FaceDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.webcamApp = cv2.CascadeClassifier(cv2.data.haarcascades + 
            'haarcascade_frontalface_default.xml')
        
    def detect_face(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.webcamApp.detectMultiScale(gray, 1.1, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow('WebcamApp', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()
    
    def release(self):
        self.cap.release()







            # cv2.imshow('WebcamApp', frame)
            

        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         self.cap.release()
        #         cv2.destroyAllWindows()
        #         break
        # else: