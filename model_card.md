# Model Card

## Model Name

**VibeFinder 1.0**

## Goal / Task

This recommender tries to suggest songs a user will probably like from a small catalog. It compares each song to a user taste profile and returns the top matches. The goal is to simulate how a simple music recommender works.

## Data Used

The dataset has 18 songs in `data/songs.csv`. Each song has `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. I added songs beyond the starter file so the catalog would have more variety. The data is still very small, so it cannot represent real music taste very well.

## Algorithm Summary

The system gives points for a `genre` match and a `mood` match. It also gives similarity points when a song is close to the user's target values for `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. Songs that are closer to the target values get more points. After every song is scored, the program sorts the songs from highest score to lowest score and returns the top results.

## Observed Behavior / Biases

The system does a good job when the user profile is clear, like happy pop or chill lofi. A weakness is that high-energy songs can show up for many profiles, even when the genre is not a great fit. `Gym Hero` appeared often because its numeric features match several "exciting" profiles. The system can also over-prioritize genre and fixed target values, which may create a small filter bubble and reduce variety.

## Evaluation Process

I tested the recommender with four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicted Sad Party. I looked at the top 5 songs for each profile and checked whether the results felt reasonable. I also tried a small experiment where I doubled the energy weight and cut the genre bonus in half. That change made high-energy songs even more dominant, which showed that the system is sensitive to the weights.

## Intended Use and Non-Intended Use

This project is meant for classroom learning and experimentation. It is useful for showing how a simple content-based recommender can score and rank songs. It should not be used for real users, real music products, or serious decision-making. It does not understand lyrics, context, culture, or changing user taste over time.

## Ideas for Improvement

- Add more songs and more genres so the results are less repetitive.
- Add diversity rules so the top 5 is not filled with songs that feel too similar.
- Use softer genre similarity instead of only exact genre matches.

## Personal Reflection

My biggest learning moment was seeing how much the weights shape the final recommendations. A small change in the energy weight changed the rankings more than I expected. AI tools helped me move faster when I needed structure, examples, and debugging help, but I still had to double-check the logic because a suggestion can sound correct while pushing the system in the wrong direction. What surprised me most is that even a very simple scoring formula can still feel like a real recommender when the results line up with a user's vibe. If I kept going, I would try adding more profiles, more data, and a diversity rule so the system could recommend songs that are both relevant and varied.
