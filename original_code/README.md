This folder is for holding your original assignments that you are using as a reference. 
Put the code in this folder, but DO NOT modify it directly! 

class User:
    # Class Attributes
    def __init__(self, username, preferences=None):
        self.username = username  # User's name
        self.preferences = preferences or {}  # User's preferences
        self.mood_history = []  # Mood history
        self.saved_playlists = []  # Saved playlists

    # Class Methods
    def add_mood(self, mood):
        self.mood_history.append(mood)

    def save_playlist(self, playlist):
        self.saved_playlists.append(playlist)

    def get_preferences(self):
        return self.preferences


class MoodAnalyzer:
    # Class Attributes
    def __init__(self):
        self.mood_map = {
            "happy": "pop",
            "sad": "acoustic",
            "energetic": "electronic",
            "calm": "classical"
        }

    # Class Methods
    def analyze_mood(self, mood):
        return self.mood_map.get(mood.lower(), "unknown")


class MusicDatabase:
    # Class Attributes
    def __init__(self):
        self.songs = {
            "pop": ["Song 1", "Song 2", "Song 3"],
            "acoustic": ["Song 4", "Song 5", "Song 6"],
            "electronic": ["Song 7", "Song 8", "Song 9"],
            "classical": ["Song 10", "Song 11", "Song 12"]
        }

    # Class Methods
    def get_songs_by_genre(self, genre):
        return self.songs.get(genre, ["No songs available for this genre"])


class MusicRecommender:
    # Class Attributes
    def __init__(self, database):
        self.database = database

    # Class Methods
    def recommend_music(self, genre):
        return self.database.get_songs_by_genre(genre)


# Simple Workflow
def main():
    # Initialize classes
    user = User(username="TestUser")
    mood_analyzer = MoodAnalyzer()
    music_db = MusicDatabase()
    recommender = MusicRecommender(database=music_db)

    # Get user input
    mood = input("Enter your mood (e.g., happy, sad, energetic, calm): ").strip()
    
    # Analyze mood
    genre = mood_analyzer.analyze_mood(mood)
    if genre == "unknown":
        print("Sorry, I couldn't recognize that mood. Try again.")
        return

    # Recommend music
    print(f"Based on your mood ({mood}), here are some {genre} songs:")
    recommendations = recommender.recommend_music(genre)
    for song in recommendations:
        print(f"- {song}")


if __name__ == "__main__":
    main()
