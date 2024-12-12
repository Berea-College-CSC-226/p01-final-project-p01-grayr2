################################################################################################################
# Author: Relly Gray
# Class: Software Design and Implementation
#
################################################################################################################
import random

# creates a user
class User:
    def __init__(self, username, preferences=None):
        self.username = username
        self.preferences = preferences or {}  # User preferences
        self.mood_history = []  # Tracks user’s mood input history
        self.saved_playlists = {}  # Stores playlists with names as keys

    def add_mood(self, mood):
        self.mood_history.append(mood)

# creates a saved playlist
    def save_playlist(self, name, playlist):
        if name in self.saved_playlists:
            print(f"Error: A playlist with the name '{name}' already exists.")
        else:
            self.saved_playlists[name] = playlist
            print(f"Playlist '{name}' saved successfully!")

# view your saved playlist
    def view_playlists(self):
        if not self.saved_playlists:
            print("No saved playlists yet.")
        else:
            print("Saved Playlists:")
            for name, playlist in self.saved_playlists.items():
                print(f"Playlist Name: {name}")
                for song in playlist:
                    print(f"- {song}")


class MoodAnalyzer:
    def __init__(self):
        self.mood_map = {
            "happy": "pop",
            "sad": "acoustic",
            "energetic": "electronic",
            "calm": "classical",
            "romantic": "jazz",
            "angry": "rock",
            "fear": "ambient",
            "disgust": "metal",
            "embarrassed": "indie",
            "lustful": "r&b",
            "nostalgic": "retro",
            "hopeful": "uplifting",
            "lonely": "soul",
            "determined": "motivational",
            "jealous": "alternative",
            "heartbroken": "blues",
            "excited": "dance",
            "cheerful": "funk",
            "tense": "drama",
            "grateful": "gospel"
        }

# checks for the entered mood and returns the genre
    def analyze_mood(self, mood):
        genre = self.mood_map.get(mood.lower(), None)
        if genre:
            return genre
        else:
            print(f"Error: Mood '{mood}' not recognized. Try another mood.")
            return None


# the music database and songs to fit the genres
class MusicDatabase:
    def __init__(self):
        self.songs = {
            "pop": [
                "Happy - Pharrell Williams", "Shake It Off - Taylor Swift", "Blinding Lights - The Weeknd",
                "Uptown Funk - Mark Ronson ft. Bruno Mars", "Can't Stop the Feeling! - Justin Timberlake",
                "Walking on Sunshine - Katrina and the Waves", "Call Me Maybe - Carly Rae Jepsen",
                "Dynamite - BTS", "Roar - Katy Perry", "All About That Bass - Meghan Trainor"
            ],
            "acoustic": [
                "Someone Like You - Adele", "Photograph - Ed Sheeran", "The A Team - Ed Sheeran",
                "Let Her Go - Passenger", "Tears in Heaven - Eric Clapton", "Skinny Love - Bon Iver",
                "Blackbird - The Beatles", "Wonderwall (Acoustic) - Oasis", "More Than Words - Extreme",
                "Fast Car - Tracy Chapman"
            ],
            "electronic": [
                "Titanium - David Guetta ft. Sia", "Animals - Martin Garrix", "Wake Me Up - Avicii",
                "Clarity - Zedd ft. Foxes", "Strobe - Deadmau5", "Stay - Kygo ft. Maty Noyes",
                "Lean On - Major Lazer & DJ Snake", "Faded - Alan Walker", "Starboy - The Weeknd ft. Daft Punk",
                "One More Time - Daft Punk"
            ],
            "classical": [
                "Canon in D - Pachelbel", "Clair de Lune - Debussy", "Symphony No. 5 - Beethoven",
                "The Four Seasons - Vivaldi", "Nocturne Op. 9 No. 2 - Chopin", "Eine kleine Nachtmusik - Mozart",
                "Swan Lake - Tchaikovsky", "Moonlight Sonata - Beethoven", "Ave Maria - Schubert",
                "Ride of the Valkyries - Wagner"
            ],
            "jazz": [
                "So What - Miles Davis", "Take Five - Dave Brubeck", "Feeling Good - Nina Simone",
                "Summertime - Ella Fitzgerald", "All of Me - Billie Holiday", "Fly Me to the Moon - Frank Sinatra",
                "Blue in Green - Miles Davis", "A Night in Tunisia - Dizzy Gillespie",
                "Autumn Leaves - Cannonball Adderley", "Round Midnight - Thelonious Monk"
            ],
            "rock": [
                "Bohemian Rhapsody - Queen", "Stairway to Heaven - Led Zeppelin", "Hotel California - Eagles",
                "Smoke on the Water - Deep Purple", "Sweet Child o' Mine - Guns N' Roses", "Back in Black - AC/DC",
                "Livin' on a Prayer - Bon Jovi", "Highway to Hell - AC/DC", "Imagine - John Lennon",
                "Purple Haze - Jimi Hendrix"
            ],
            "ambient": [
                "Weightless - Marconi Union", "Spiegel im Spiegel - Arvo Pärt", "Monday - Ludovico Einaudi",
                "An Ending (Ascent) - Brian Eno", "Bloom - Ólafur Arnalds", "Opus 23 - Dustin O'Halloran",
                "Arrival of the Birds - The Cinematic Orchestra", "We Move Lightly - Dustin O'Halloran",
                "Clair de Lune - Debussy", "Time - Hans Zimmer"
            ],
            "metal": [
                "Master of Puppets - Metallica", "Painkiller - Judas Priest", "Ace of Spades - Motörhead",
                "Hallowed Be Thy Name - Iron Maiden", "Chop Suey! - System of a Down", "Holy Wars - Megadeth",
                "The Beautiful People - Marilyn Manson", "Raining Blood - Slayer", "Paranoid - Black Sabbath",
                "Du Hast - Rammstein"
            ],
            "indie": [
                "Take Me Out - Franz Ferdinand", "Fluorescent Adolescent - Arctic Monkeys",
                "Wake Up - Arcade Fire", "1901 - Phoenix", "Home - Edward Sharpe & The Magnetic Zeros",
                "Little Lion Man - Mumford & Sons", "Skinny Love - Bon Iver", "Dog Days Are Over - Florence + The Machine",
                "Electric Feel - MGMT", "Such Great Heights - The Postal Service"
            ],
            "r&b": [
                "Earned It - The Weeknd", "Adorn - Miguel", "Redbone - Childish Gambino",
                "Blow - Beyoncé", "Climax - Usher", "Superstar - Usher", "Do I Do - Stevie Wonder",
                "End of the Road - Boyz II Men", "No Scrubs - TLC", "So Sick - Ne-Yo"
            ],
            "retro": [
                "Take on Me - A-ha", "Sweet Dreams - Eurythmics", "Don't Stop Believin' - Journey",
                "Eye of the Tiger - Survivor", "Billie Jean - Michael Jackson", "Dancing Queen - ABBA",
                "Come On Eileen - Dexys Midnight Runners", "Africa - Toto", "Footloose - Kenny Loggins",
                "Summer of '69 - Bryan Adams"
            ],
            "uplifting": [
                "Rise Up - Andra Day", "Stronger - Kelly Clarkson", "Don't Stop Me Now - Queen",
                "I Will Survive - Gloria Gaynor", "Fight Song - Rachel Platten", "Brave - Sara Bareilles",
                "Beautiful Day - U2", "A Sky Full of Stars - Coldplay", "On Top of the World - Imagine Dragons",
                "Don't Stop Believin' - Journey"
            ],
            "soul": [
                "A Change is Gonna Come - Sam Cooke", "Let's Stay Together - Al Green",
                "Try a Little Tenderness - Otis Redding", "Stand By Me - Ben E. King",
                "Ain't No Sunshine - Bill Withers", "At Last - Etta James",
                "Superstition - Stevie Wonder", "If You Don't Know Me By Now - Harold Melvin & the Blue Notes",
                "Me and Mrs. Jones - Billy Paul", "You Make Me Feel Like A Natural Woman - Aretha Franklin"
            ],
            "motivational": [
                "Eye of the Tiger - Survivor", "Lose Yourself - Eminem", "We Will Rock You - Queen",
                "Stronger - Kanye West", "Can't Hold Us - Macklemore & Ryan Lewis",
                "Run the World (Girls) - Beyoncé", "Shake It Off - Taylor Swift",
                "Hall of Fame - The Script", "Don't Stop Believin' - Journey",
                "I Gotta Feeling - The Black Eyed Peas"
            ],
            "alternative": [
                "Creep - Radiohead", "Smells Like Teen Spirit - Nirvana", "Mr. Brightside - The Killers",
                "Seven Nation Army - The White Stripes", "Boulevard of Broken Dreams - Green Day",
                "Somebody Told Me - The Killers", "Everlong - Foo Fighters", "1979 - The Smashing Pumpkins",
                "Clocks - Coldplay", "When I Come Around - Green Day"
            ],
            "blues": [
                "The Thrill is Gone - B.B. King", "Crossroads - Robert Johnson",
                "Sweet Home Chicago - Buddy Guy", "Hoochie Coochie Man - Muddy Waters",
                "Red House - Jimi Hendrix", "Pride and Joy - Stevie Ray Vaughan",
                "Stormy Monday - T-Bone Walker", "Boom Boom - John Lee Hooker",
                "Ain't Nobody's Business - Bessie Smith", "Key to the Highway - Eric Clapton"
            ],
            "dance": [
                "Uptown Funk - Mark Ronson ft. Bruno Mars", "Sorry - Justin Bieber",
                "Titanium - David Guetta ft. Sia", "Turn Down for What - DJ Snake & Lil Jon",
                "Wake Me Up - Avicii", "Don't Start Now - Dua Lipa", "Lean On - Major Lazer",
                "Shut Up and Dance - Walk the Moon", "Hey Ya! - OutKast", "Get Lucky - Daft Punk"
            ],
            "funk": [
                "Uptown Funk - Mark Ronson ft. Bruno Mars", "Superstition - Stevie Wonder",
                "Brick House - Commodores", "Get Down On It - Kool & The Gang",
                "Pick Up the Pieces - Average White Band", "Flashlight - Parliament",
                "Give Up the Funk - Parliament", "Let's Groove - Earth, Wind & Fire",
                "Sex Machine - James Brown", "Jungle Boogie - Kool & The Gang"
            ],
            "drama": [
                "In the End - Linkin Park", "Boulevard of Broken Dreams - Green Day",
                "Numb - Linkin Park", "Chasing Cars - Snow Patrol", "With or Without You - U2",
                "Runaway - Kanye West", "Nothing Else Matters - Metallica", "Hurt - Johnny Cash",
                "November Rain - Guns N' Roses", "The Scientist - Coldplay"
            ],
            "gospel": [
                "Amazing Grace - Traditional", "Take Me to the King - Tamela Mann",
                "Break Every Chain - Tasha Cobbs", "Every Praise - Hezekiah Walker",
                "I Smile - Kirk Franklin", "You Are Good - Israel Houghton",
                "Nobody Greater - Vashawn Mitchell", "Blessings - Laura Story",
                "How Great Is Our God - Chris Tomlin", "Shout to the Lord - Hillsong Worship"
            ]
        }

    def get_songs_by_genre(self, genre):
        return self.songs.get(genre, ["No songs available for this genre"])

# this is the spotify link database
class MusicRecommender:
    def __init__(self, database):
        self.database = database
        self.playlist_links = {
            "pop": "https://open.spotify.com/playlist/37i9dQZF1EQncLwOalG3K7",
            "acoustic": "https://open.spotify.com/playlist/37i9dQZF1EIdu0PHOCYQ71",
            "electronic": "https://open.spotify.com/playlist/37i9dQZF1EIgtdfeeWwF7B",
            "classical": "https://open.spotify.com/playlist/37i9dQZF1EIghNBbh3wJEC",
            "jazz": "https://open.spotify.com/playlist/37i9dQZF1EIdgqvd8Qfc5i",
            "rock": "https://open.spotify.com/playlist/37i9dQZF1EQpj7X7UK8OOF",
            "ambient": "https://open.spotify.com/playlist/37i9dQZF1EIfXgTSpbzUXS",
            "metal": "https://open.spotify.com/playlist/37i9dQZF1EQpgT26jgbgRI",
            "indie": "https://open.spotify.com/playlist/37i9dQZF1EQqkOPvHGajmW",
            "r&b": "https://open.spotify.com/playlist/37i9dQZF1EQoqCH7BwIYb7",
            "retro": "https://open.spotify.com/playlist/37i9dQZF1EIeaq4GvA0R5R",
            "uplifting": "https://open.spotify.com/playlist/37i9dQZF1EIeOoLWBf6eek",
            "soul": "https://open.spotify.com/playlist/37i9dQZF1EIhnwggN3ojua",
            "motivational": "https://open.spotify.com/playlist/37i9dQZF1EIeBQQL9SHmkZ",
            "alternative": "https://open.spotify.com/playlist/37i9dQZF1EIgvT6k4mUrw7",
            "blues": "https://open.spotify.com/playlist/37i9dQZF1DXd9rSDyQguIk",
            "dance": "https://open.spotify.com/playlist/37i9dQZF1EIfumGmFpHj8i",
            "funk": "https://open.spotify.com/playlist/37i9dQZF1EIcZuVzFmiIZ9",
            "drama": "https://open.spotify.com/playlist/37i9dQZF1EIhKU1TvoH9JR",
            "gospel": "https://open.spotify.com/playlist/63D6rRGu1VaWFhW9AP1LXD"
        }

# this is where the recommended music is printed on the console
    def recommend_music(self, genre, num_songs=3):
        all_songs = self.database.get_songs_by_genre(genre)
        if not all_songs or "No songs available" in all_songs[0]:
            return all_songs, None

        recommended_songs = random.sample(all_songs, min(num_songs, len(all_songs)))
        playlist_link = self.playlist_links.get(genre, "https://www.youtube.com/results?search_query=" + genre)
        return recommended_songs, playlist_link


def get_valid_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if valid_options and user_input.lower() not in valid_options:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")
        elif not user_input:
            print("Input cannot be empty. Please try again.")
        else:
            return user_input.lower()


def main():
    print("Welcome to the Ultimate Mood-Based Music Recommender!")

    # Initialize system components
    username = input("Enter your username: ").strip()
    user = User(username=username)
    mood_analyzer = MoodAnalyzer()
    music_db = MusicDatabase()
    recommender = MusicRecommender(database=music_db)

    while True:
        print("\nMain Menu:")
        print("1. Enter Mood and Get Recommendations")
        print("2. View Saved Playlists")
        print("3. Exit")
        choice = get_valid_input("Choose an option (1, 2, or 3): ", valid_options=["1", "2", "3"])

        if choice == "1":
            mood = get_valid_input("Enter your mood (e.g., happy, sad, energetic, nostalgic, etc.): ")
            genre = mood_analyzer.analyze_mood(mood)
            if genre:
                user.add_mood(mood)
                recommendations, playlist_link = recommender.recommend_music(genre)
                print(f"\nBased on your mood ({mood}), here are some {genre} songs:")
                for song in recommendations:
                    print(f"- {song}")

                print(f"\nExplore more {genre} music here: {playlist_link}")

                save_choice = get_valid_input("Would you like to save this playlist? (yes or no): ", valid_options=["yes", "no"])
                if save_choice == "yes":
                    playlist_name = input("Enter a name for your playlist: ").strip()
                    user.save_playlist(playlist_name, recommendations)

        elif choice == "2":
            user.view_playlists()

        elif choice == "3":
            print("Thank you for using the Ultimate Mood-Based Music Recommender. Goodbye!")
            break


if __name__ == "__main__":
    main()



