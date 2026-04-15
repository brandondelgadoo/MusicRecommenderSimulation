import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV into dictionaries with numeric fields converted."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences and explain why."""
    score = 0.0
    reasons: List[str] = []

    if song["genre"] == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    def add_similarity_points(
        feature_name: str, max_points: float, value_range: float
    ) -> None:
        nonlocal score

        if feature_name not in user_prefs:
            return

        difference = abs(song[feature_name] - user_prefs[feature_name])
        closeness = max(0.0, 1 - (difference / value_range))
        points = max_points * closeness
        score += points
        reasons.append(f"{feature_name} close (+{points:.2f})")

    add_similarity_points("energy", 2.0, 1.0)
    add_similarity_points("valence", 1.0, 1.0)
    add_similarity_points("danceability", 1.0, 1.0)
    add_similarity_points("acousticness", 0.5, 1.0)
    add_similarity_points("tempo_bpm", 0.5, 92.0)

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank all songs by score and return the top k with explanations."""
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "baseline similarity only"
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
