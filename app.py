from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/ligar",methods=['POST'])
def ligar():
    return render_template('ligar.html')


@app.route("/desligar",methods=['POST'])
def desligar():
    return render_template('desligar.html')       
 
        
if __name__ == "__main__":
    app.run(debug=True)
    

