"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n{profile_name}")
    print(f"Preferences: {user_prefs}")
    print("Top recommendations:")
    for song, score, explanation in recommendations:
        print(f"- {song['title']} by {song['artist']} | Score: {score:.2f}")
        print(f"  Because: {explanation}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        "Edge Case: Sad But High Energy": {"genre": "pop", "mood": "sad", "energy": 0.9},
        "Edge Case: Unknown Genre": {"genre": "opera", "mood": "peaceful", "energy": 0.4},
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
