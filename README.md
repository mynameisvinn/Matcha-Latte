# Matcha Latte
Matcha Latte is a testing environment to develop algorithms for skill-based matchmaking.

## Quickstart
### Fetching historical matches
Matcha makes it easy to fetch and format datasets from MongoDB.
```python
from Matcha import fetch_dataset

# select title
game = "ps4-madden19"
data = fetch_dataset(game)

# save to csv
path = "datasets/" + game + ".csv"
data.to_csv(path)
```
### Measuring PLR accuracy
Once we've have historical outcomes, we can [measure past performance](https://github.com/mynameisvinn/Matcha/blob/master/Measuring%20PLR%20Accuracy%20on%20Historical%20Matches.ipynb) of the PLR rating system (based on Glicko-2).
```python
from Matcha import calculate_accuracy

path = "datasets/ps4-madden19.csv"
outcomes = pd.read_csv(path)  
res = calculate_accuracy(outcomes)  # accuracy
```