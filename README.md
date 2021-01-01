# Macha
Designing algorithms for skill-based matchmaking.

## Quickstart
### Fetching historical matches
```python
from Macha import fetch_dataset

# select title
game = "ps4-madden19"
data = fetch_dataset(game)

# save to csv
path = "datasets/" + game + ".csv"
data.to_csv(path)
```