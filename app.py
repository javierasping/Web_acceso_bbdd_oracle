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
            dsn_tns = cx_Oracle.makedsn('192.168.122.169', '1521', service_name='GN')
            connection = cx_Oracle.connect(username, password, dsn=dsn_tns)            
            session['usuario_autenticado'] = True
            # ORCLCDB
            cursor = connection.cursor()
            cursor.execute("select * from PROFESORES")
            tablas_con_permiso = cursor.fetchall()
            contenido_tablas = {}

            # for tabla in tablas_con_permiso:
            #     cursor.execute(f"SELECT * FROM {tabla[0]}")
            #     contenido_tabla = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
            #     contenido_tablas[tabla[0]] = contenido_tabla

            cursor.close()
            connection.close()
            
            return render_template("profesores.html", tablas_con_permiso=tablas_con_permiso, contenido_tablas=contenido_tablas)
            
        except cx_Oracle.DatabaseError as e:
            return "Error: Credenciales incorrectas. Vuelve a intentarlo."


    # Si el método es GET y el usuario no está autenticado, muestra el formulario de inicio de sesión.
    return render_template("login.html")

# ...



@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0", 15000, debug=True)
