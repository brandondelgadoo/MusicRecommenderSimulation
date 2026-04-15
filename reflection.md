# Reflection

## Profile Comparisons

High-Energy Pop vs Chill Lofi: The pop profile pushed energetic, bright, danceable songs like `Sunrise City` and `Gym Hero` to the top, while the lofi profile shifted toward slower and more acoustic songs like `Library Rain` and `Midnight Coding`. That makes sense because the lofi profile asked for lower energy, lower tempo, and much higher acousticness.

High-Energy Pop vs Deep Intense Rock: Both profiles like high energy, so some overlap appears in the numeric similarity, but the rock profile changes the winners because it prefers lower valence and an intense mood. That is why `Storm Runner` jumps to the top for rock, while `Sunrise City` stays on top for pop.

Chill Lofi vs Deep Intense Rock: These profiles pull the system in opposite directions. Lofi favors calm, slow, acoustic tracks, while the rock profile favors fast, loud, and low-acousticness songs. The outputs changed in the exact way I would expect, which is a good sign that the numeric similarity logic is doing real work.

Deep Intense Rock vs Conflicted Sad Party: This comparison exposed one weakness in the model. Both profiles prefer high energy, so songs like `Gym Hero` score well even though the emotional intent is different. The system can tell that moody and intense are different labels, but it does not truly understand why a "sad party" request is more complex than just mixing low valence with high danceability.

## Plain-Language Takeaway

`Gym Hero` keeps showing up because it is a strong numeric match for several profiles. It has very high energy, very high danceability, low acousticness, and a reasonably fast tempo, so the scoring formula sees it as close to many "exciting" user targets even when the genre or emotional nuance is not perfect. That means the recommender is consistent, but it also shows how a simple formula can over-reward one kind of song shape.
