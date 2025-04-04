from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
from keras.models import load_model, Sequential, model_from_json
from keras.preprocessing.image import img_to_array
from movie_recommender import MovieRecommender
from song_recommender import SongRecommender
import json
import os

# Get the absolute path to the directory containing this script
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Load the trained model
try:
    model = load_model("emotiondetector.keras")
except:
    try:
        with open("emotiondetector.json", "r") as json_file:
            model_json = json_file.read()
        model = model_from_json(model_json)
        model.load_weights("emotiondetector.keras")
    except Exception as e:
        print(f"Error loading model: {e}")
        exit(1)

# Initialize recommenders
movie_recommender = MovieRecommender("fa6cd92828619e5fbbea572656800674")
song_recommender = SongRecommender()

# Load OpenCV's pre-trained face detector
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Define emotion labels
labels = ['angry', 'happy', 'neutral', 'sad', 'surprise']

# Global variables
current_emotion = None
wishlist = []

def extract_features(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (48, 48))
    image = img_to_array(image)
    image = image.astype("float") / 255.0
    image = np.expand_dims(image, axis=[0, -1])
    return image

def generate_frames():
    webcam = cv2.VideoCapture(0)
    while True:
        ret, frame = webcam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)  # Increased minimum face size
        )

        global current_emotion
        if len(faces) == 0:
            current_emotion = None
            # Add text to guide user
            cv2.putText(frame, "No face detected. Please position your face in the center.", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            for (x, y, w, h) in faces:
                face_roi = frame[y:y+h, x:x+w]
                face_input = extract_features(face_roi)
                prediction = model.predict(face_input, verbose=0)
                predicted_label = labels[np.argmax(prediction)]
                confidence = np.max(prediction) * 100
                current_emotion = predicted_label

                # Draw rectangle around face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # Add emotion label with confidence
                label_text = f"{predicted_label} ({confidence:.1f}%)"
                cv2.putText(frame, label_text, (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                # Add guide text
                cv2.putText(frame, "Face detected! Click 'Get Recommendations'", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_recommendations')
def get_recommendations():
    if current_emotion:
        movie_recommendations = movie_recommender.get_movie_recommendations(current_emotion)
        song_recommendations = song_recommender.get_song_recommendations(current_emotion)
        return jsonify({
            'movies': movie_recommendations,
            'songs': song_recommendations
        })
    return jsonify({'movies': [], 'songs': []})

@app.route('/add_to_wishlist', methods=['POST'])
def add_to_wishlist():
    movie = request.json
    if movie not in wishlist:
        wishlist.append(movie)
    return jsonify({"status": "success"})

@app.route('/get_wishlist')
def get_wishlist():
    return jsonify(wishlist)

@app.route('/remove_from_wishlist', methods=['POST'])
def remove_from_wishlist():
    movie = request.json
    if movie in wishlist:
        wishlist.remove(movie)
    return jsonify({"status": "success"})

@app.route('/get_current_emotion')
def get_current_emotion():
    return jsonify({"emotion": current_emotion})

if __name__ == '__main__':
    app.run(debug=True) 