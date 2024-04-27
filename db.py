import mysql.connector
from datetime import datetime

class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="asistencia"

        )

        self.cursor = self.conn.cursor()
    
    def insert_empleado(self, numero_empleado, timestamp, imagen):
        query = "INSERT INTO registro_empleados (numero_empleado, hora, imagen) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (numero_empleado, timestamp, imagen))
        self.conn.commit()

    def existe_empleado(self, numero_empleado):
        query = "SELECT COUNT(*) FROM registro_empleados WHERE numero_empleado = %s"
        self.cursor.execute(query, (numero_empleado,))
        result = self.cursor.fetchone()[0]
        return result > 0
  
    def close(self):
        self.cursor.close()
        self.conn.close()