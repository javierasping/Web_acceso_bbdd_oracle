import requests,json
from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)
url = "https://gateway.marvel.com/v1/public/characters?apikey=1bf075d536f284d8d6c923c4b425be90&hash=0ac16158f12e2734c5e67838045eded3&ts=1683278024.2311842"

@app.route('/')
def inicio():
    return render_template("index.html")




@app.route('/obras')
def obras():
    return render_template("obras.html")


@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0", 15000, debug=True)
