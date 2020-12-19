# Macha
Monte Carlo simulation/testbed for skill-based matchmaking.

## Why simulate skill based matchmaking?
Most rating algorithms require a meaningful "warm up" period (eg Glicko-2, a popular ratings algorithm, [requires 10-15 games](http://glicko.net/glicko/glicko2.pdf) for an accurate rating). 

For games with small samples (e.g., N < 8), we need better rating algorithms, possibly sacrificing certainty for faster convergence.

## Resources
* https://www.tetrisconcept.com/2020/01/building-rating-system-for-competitive.html