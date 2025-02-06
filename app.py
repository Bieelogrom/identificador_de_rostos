from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__, template_folder="./templates")

def capture_by_frames(): 
    global camera
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read() 
        detector=cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
        faces=detector.detectMultiScale(frame,1.2,6)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/ligar",methods=['POST'])
def ligar():
    return render_template('ligar.html')


@app.route("/desligar",methods=['POST'])
def desligar():
    if camera.isOpened():
        camera.release()
    return render_template('desligar.html')       
 
@app.route('/video_capture')
def video_capture():
    return Response(capture_by_frames(), mimetype='multipart/x-mixed-replace; boudary=frame')
        
if __name__ == "__main__":
    app.run(debug=True,port=8000,use_reloader=False)
    

