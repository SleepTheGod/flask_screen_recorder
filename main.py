from flask import Flask, render_template, send_file, request, redirect, url_for
import pyautogui
import cv2
import os
from threading import Thread
import time
import socketio
import ffmpeg

app = Flask(__name__)
sio = socketio.Server()
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

recording = False
output_file = "output.mp4"
frames_per_second = 20.0
resolution = pyautogui.size()

def record_screen():
    global recording
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), frames_per_second, resolution)
    while recording:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        out.write(frame)
    out.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_recording', methods=['POST'])
def start_recording():
    global recording
    recording = True
    thread = Thread(target=record_screen)
    thread.start()
    return redirect(url_for('index'))

@app.route('/stop_recording', methods=['POST'])
def stop_recording():
    global recording
    recording = False
    return redirect(url_for('index'))

@app.route('/download_recording')
def download_recording():
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
