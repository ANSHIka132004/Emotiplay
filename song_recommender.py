import random

class SongRecommender:
    def __init__(self):
        # Offline song recommendations for each emotion
        self.emotion_songs = {
            'happy': [
                {
                    'title': 'Happy',
                    'artist': 'Pharrell Williams',
                    'genre': 'Pop',
                    'year': 2013,
                    'spotify_link': 'https://open.spotify.com/track/60nZcImOyXatj1tXhqKjVA'
                },
                {
                    'title': 'Good Vibrations',
                    'artist': 'Beach Boys',
                    'genre': 'Rock',
                    'year': 1966,
                    'spotify_link': 'https://open.spotify.com/track/5QhNhKP0t6F8OQqVrDS5Hn'
                },
                {
                    'title': 'Walking on Sunshine',
                    'artist': 'Katrina & The Waves',
                    'genre': 'Pop',
                    'year': 1983,
                    'spotify_link': 'https://open.spotify.com/track/5yAN5c0KjVEwqIpDOG0Wmb'
                },
                {
                    'title': 'Don\'t Stop Believin\'',
                    'artist': 'Journey',
                    'genre': 'Rock',
                    'year': 1981,
                    'spotify_link': 'https://open.spotify.com/track/4bHb5Su9OI12cKr2vunCQD'
                },
                {
                    'title': 'I Gotta Feeling',
                    'artist': 'Black Eyed Peas',
                    'genre': 'Pop',
                    'year': 2009,
                    'spotify_link': 'https://open.spotify.com/track/4kLLWz7srcuLk7kwHlJqrH'
                }
            ],
            'sad': [
                {
                    'title': 'Someone Like You',
                    'artist': 'Adele',
                    'genre': 'Pop',
                    'year': 2011,
                    'spotify_link': 'https://open.spotify.com/track/4kLLWz7srcuLk7kwHlJqrH'
                },
                {
                    'title': 'All of Me',
                    'artist': 'John Legend',
                    'genre': 'Pop',
                    'year': 2013,
                    'spotify_link': 'https://open.spotify.com/track/3U4isOIWMTrULl197l5gMj'
                },
                {
                    'title': 'Say Something',
                    'artist': 'A Great Big World',
                    'genre': 'Pop',
                    'year': 2013,
                    'spotify_link': 'https://open.spotify.com/track/6Vc5wAMmXdKIAM7WUoEb8N'
                },
                {
                    'title': 'Stay With Me',
                    'artist': 'Sam Smith',
                    'genre': 'Pop',
                    'year': 2014,
                    'spotify_link': 'https://open.spotify.com/track/5Db9VidYfGrVYvWzyQar5l'
                },
                {
                    'title': 'The Sound of Silence',
                    'artist': 'Simon & Garfunkel',
                    'genre': 'Folk',
                    'year': 1964,
                    'spotify_link': 'https://open.spotify.com/track/39fULoyTveNtlnf12Eqpyv'
                }
            ],
            'angry': [
                {
                    'title': 'In the End',
                    'artist': 'Linkin Park',
                    'genre': 'Rock',
                    'year': 2000,
                    'spotify_link': 'https://open.spotify.com/track/3aY1jFwqGk2q4mpVxVeITv'
                },
                {
                    'title': 'Break Stuff',
                    'artist': 'Limp Bizkit',
                    'genre': 'Rock',
                    'year': 1999,
                    'spotify_link': 'https://open.spotify.com/track/2YC6ET3q1F29B0V7UcPV70'
                },
                {
                    'title': 'Given Up',
                    'artist': 'Linkin Park',
                    'genre': 'Rock',
                    'year': 2007,
                    'spotify_link': 'https://open.spotify.com/track/1nN6H5qFk5Qe2TowHv1Cgb'
                },
                {
                    'title': 'Bodies',
                    'artist': 'Drowning Pool',
                    'genre': 'Rock',
                    'year': 2001,
                    'spotify_link': 'https://open.spotify.com/track/3DtgT6dLkfTaWsgjRTag0G'
                },
                {
                    'title': 'Last Resort',
                    'artist': 'Papa Roach',
                    'genre': 'Rock',
                    'year': 2000,
                    'spotify_link': 'https://open.spotify.com/track/5W8YXBz9MTIDyrpYaCg2Ky'
                }
            ],
            'surprise': [
                {
                    'title': 'Bohemian Rhapsody',
                    'artist': 'Queen',
                    'genre': 'Rock',
                    'year': 1975,
                    'spotify_link': 'https://open.spotify.com/track/3z8h0TUyReEj6JjT1yvhwv'
                },
                {
                    'title': 'Sweet Dreams (Are Made of This)',
                    'artist': 'Eurythmics',
                    'genre': 'Pop',
                    'year': 1983,
                    'spotify_link': 'https://open.spotify.com/track/1TfqLAPs4K0s6Eu15Icbuf'
                },
                {
                    'title': 'Somebody That I Used to Know',
                    'artist': 'Gotye',
                    'genre': 'Pop',
                    'year': 2011,
                    'spotify_link': 'https://open.spotify.com/track/4U0m5UyN5g524TEnva0x0P'
                },
                {
                    'title': 'Sweet Caroline',
                    'artist': 'Neil Diamond',
                    'genre': 'Pop',
                    'year': 1969,
                    'spotify_link': 'https://open.spotify.com/track/62AuGbAkt8Ox2IrFFb8Ghe'
                },
                {
                    'title': 'Don\'t Stop Me Now',
                    'artist': 'Queen',
                    'genre': 'Rock',
                    'year': 1978,
                    'spotify_link': 'https://open.spotify.com/track/7hQJA50XrCWABAu5v6Qb4s'
                }
            ],
            'neutral': [
                {
                    'title': 'The Sound of Silence',
                    'artist': 'Simon & Garfunkel',
                    'genre': 'Folk',
                    'year': 1964,
                    'spotify_link': 'https://open.spotify.com/track/39fULoyTveNtlnf12Eqpyv'
                },
                {
                    'title': 'Hallelujah',
                    'artist': 'Jeff Buckley',
                    'genre': 'Folk',
                    'year': 1994,
                    'spotify_link': 'https://open.spotify.com/track/3pRaLNL3b8x5uBOcsgvdqM'
                },
                {
                    'title': 'Mad World',
                    'artist': 'Gary Jules',
                    'genre': 'Pop',
                    'year': 2001,
                    'spotify_link': 'https://open.spotify.com/track/3JOVTQ5h8DeGFaIGxjr6vE'
                },
                {
                    'title': 'Boulevard of Broken Dreams',
                    'artist': 'Green Day',
                    'genre': 'Rock',
                    'year': 2004,
                    'spotify_link': 'https://open.spotify.com/track/5GQc3NkjPzRjET9vnhq0Ap'
                },
                {
                    'title': 'Yesterday',
                    'artist': 'The Beatles',
                    'genre': 'Rock',
                    'year': 1965,
                    'spotify_link': 'https://open.spotify.com/track/3BQHpFgAp4l80e1XslIjNI'
                }
            ]
        }

    def get_song_recommendations(self, emotion):
        """Get song recommendations based on the detected emotion."""
        if emotion in self.emotion_songs:
            # Return 5 random songs for the emotion
            return random.sample(self.emotion_songs[emotion], min(5, len(self.emotion_songs[emotion])))
        return [] 