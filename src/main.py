"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.80,
            "tempo_bpm": 122,
            "valence": 0.82,
            "danceability": 0.84,
            "acousticness": 0.20,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.38,
            "tempo_bpm": 76,
            "valence": 0.58,
            "danceability": 0.60,
            "acousticness": 0.82,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.92,
            "tempo_bpm": 145,
            "valence": 0.45,
            "danceability": 0.55,
            "acousticness": 0.08,
        },
        "Conflicted Sad Party": {
            "genre": "pop",
            "mood": "moody",
            "energy": 0.90,
            "tempo_bpm": 128,
            "valence": 0.25,
            "danceability": 0.88,
            "acousticness": 0.10,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {profile_name} ===\n")
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{index}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
            print()


if __name__ == "__main__":
    main()
