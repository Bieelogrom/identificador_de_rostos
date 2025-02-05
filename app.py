from flask import Flask, render_template, Response, request
import numpy as np
import cv2
import datetime, time
import os, sys
from threading import Thread

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def home():
    opcoes = ["Ligar/Desligar", "Tirar foto", "Preto e branco", "Negativo", "Focar no rosto", "Parar de gravar"]
    return render_template('index.html', opcoes=opcoes)

if __name__ == "__main__":
    app.run(debug=True)