from flask import Flask, render_template, Response, request
import numpy as np
import cv2
import datetime, time
import os, sys
from threading import Thread

global capture,rec_frame,grey,switch,neg,face,rec,out
capture=0
grey=0
neg=0
face=0
switch=1
rec=0

#Cria a pasta para armazenar as fotos salvas
try:
    os.mkdir('./fotos')
except OSError as error:
    pass

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def home():
    opcoes = ["Ligar/Desligar", "Tirar foto", "Preto e branco", "Negativo", "Focar no rosto", "Parar de gravar"]
    return render_template('index.html', opcoes=opcoes)

if __name__ == "__main__":
    app.run(debug=True)