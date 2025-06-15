


# Demo video
https://github.com/user-attachments/assets/aeaa65e0-dddb-4ad2-82bf-027ab31f3aac

# How It Works
-The system captures an image via webcam.
-A trained Keras model (emotiondetector.keras) predicts the emotion.
-Based on your detected emotion, the system:
   🎬 Suggests 5 mood-matching movies.
To enhance the user's emotional state and uplift user's mood quickly.

# Dataset & Data Gathering
FER2013 for facial emotion recognition (48x48 grayscale images)
OMDB API for real-time movie metadata: title, overview, genres, ratings, posters
Caching mechanism for faster and limited API usage

# Data Preprocessing
Emotion images normalized, augmented (rotation, shift, zoom, flip)

Emotion-to-genre mapping:

😊 Happy → Comedy, Animation, Adventure

😢 Sad → Drama, Romance

😠 Angry → Action, Thriller

😐 Neutral → Sci-Fi, Documentary

😲 Surprise → Horror, Fantasy

Data validation and error handling

📈 Exploratory Data Analysis
Emotion distribution
Model training/validation accuracy and loss curves
Confusion matrix
Genre distribution insights

# Feature Extraction
Face Detection: Haar Cascades

Emotion Classification: CNN

Movie Metadata: Title, Genre, Rating, Poster, Overview

# Model Training
CNN Architecture: 3 Conv blocks, BatchNorm, Dropout, Dense (512), Softmax output
Training: 50 epochs, batch size 64, Adam optimizer, early stopping, LR scheduler

# Deployment
Backend (Flask):

Real-time video feed & emotion detection
Movie recommendation engine
RESTful API & session management

Frontend:

Live camera feed
Dynamic recommendations
Wishlist feature

Database: SQLite for caching and sessions

# Performance Optimizations
Caching system for movie recommendations
Batch face detection
Optimized model loading
API rate limiting and error logging

# Technologies Used
ML & CV: TensorFlow, Keras, OpenCV

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Database: SQLite

APIs: OMDB API





