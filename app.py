import requests,json,cx_Oracle
from flask import Flask, render_template, abort, redirect, request, session
import os


app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def inicio():
    return render_template("index.html")




import cx_Oracle

# ...

# ...

@app.route('/obras', methods=['GET', 'POST'])
def obras():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            dsn_tns = cx_Oracle.makedsn('192.168.122.179', '1521', service_name='ORCLCDB')
            connection = cx_Oracle.connect(username, password, dsn=dsn_tns)            
            session['usuario_autenticado'] = True
            
            # Consulta el contenido de la tabla "autores".
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM concierto")
            contenido_concierto = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
            
            cursor.close()
            connection.close()
            
            return render_template("obras.html", contenido_concierto=contenido_concierto)
            
        except cx_Oracle.DatabaseError as e:
            return "Error: Credenciales incorrectas. Vuelve a intentarlo."
    
    # Si el usuario ya está autenticado, muestra la página de obras.
    if session.get('usuario_autenticado'):
        return render_template("obras.html")

    # Si el método es GET y el usuario no está autenticado, muestra el formulario de inicio de sesión.
    return render_template("login.html")

# ...



@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0", 15000, debug=True)
