🧠 How It Works
-The system captures an image via webcam.
-A trained Keras model (emotiondetector.keras) predicts the emotion.
-Based on your detected emotion, the system:

   🎵 Shows a curated list of 5 songs (with Spotify links).
   🎬 Suggests 5 mood-matching movies.
To enhance the user's emotional state and uplift user's mood quickly.

PROJECT STRUCTURE
├── app.py                   # Flask web app controller

├── emotiondetector.keras   # Trained model file

├── emotiondetector.json    # Model architecture

├── song_recommender.py     # Song recommendations based on emotion

├── movie_recommender.py    # Movie recommendations based on emotion

├── requirements.txt        # Required Python packages


