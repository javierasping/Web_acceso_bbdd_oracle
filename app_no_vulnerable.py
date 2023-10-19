import requests,json,cx_Oracle
from flask import Flask, render_template, abort, redirect, request, session
import os


app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/obras', methods=['GET', 'POST'])
def obras():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            # Realiza la conexión a la base de datos Oracle
            dsn_tns = cx_Oracle.makedsn('192.168.122.179', '1521', service_name='ORCLCDB')
            connection = cx_Oracle.connect('javiercruces', 'javiercruces', dsn=dsn_tns)
            cursor = connection.cursor()

            # Consulta la tabla de usuarios para validar las credenciales de manera segura
            cursor.execute("SELECT count(*) FROM usuarios WHERE usuario = :username AND contrasena = :password",
                           username=username, password=password)
            user_data = cursor.fetchone()

            if user_data == (1,):
                # Si las credenciales son válidas, consulta y muestra el contenido de la tabla "entrada"
                cursor.execute("SELECT * FROM entrada")
                entradas = cursor.fetchall()
                cursor.close()
                connection.close()
                return render_template("obrasv2.html", entradas=entradas)
            else:
                cursor.close()
                connection.close()
                return "Credenciales inválidas. Vuelve a intentarlo."

        except cx_Oracle.DatabaseError as e:
            return "Error de autenticación. Vuelve a intentarlo."

    return render_template("login.html")




@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0", 15000, debug=True)

