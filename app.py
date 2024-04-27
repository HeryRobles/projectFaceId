import tkinter as tk
from tkinter import messagebox
import cv2
from datetime import datetime
from db import Database
from face_detection import FaceDetector

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Registro de empleados')

        self.detector = FaceDetector()
        self.db = Database('localhost', 'root', '', 'asistencia')

        self.label = tk.Label(root, text='Registro de empleados', font=('Arial', 20))
        self.label.pack(pady=20)

        self.entry_label = tk.Label(root, text='Número de empleado:', font=('Arial', 12))
        self.entry_label.pack()
        self.entry = tk.Entry(root, font=('Arial', 12))
        self.entry.pack(pady=10)

        self.capture_button = tk.Button(root, text='Capturar', font=('Arial', 12), command=self.capture)
        self.capture_button.pack(pady=20)

        self.exit_button = tk.Button(root, text='Salir', font=('Arial', 12), command=root.destroy)
        self.exit_button.pack(pady=20)

    def capture(self):
        numero_empleado = self.entry.get()
        timestamp = datetime.now()
        frame = self.detector.detect_face()
        if frame is not None:
            _, img_encoded = cv2.imencode('.jpg', frame)

            if self.db.existe_empleado(numero_empleado):
                
                self.db.insert_empleado(numero_empleado, timestamp, img_encoded.tobytes())
                messagebox.showinfo('Registro', 'Empleado registrado correctamente')
            else:
                messagebox.showerror('Error', 'Empleado no registrado')
        else:
            messagebox.showerror('Error', 'No se detectó ningún rostro')
    
    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.detector.release()
        self.db.close() 

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.run()

