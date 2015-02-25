# Basketball
Various Basketball Related Time-Wasters

nba_basketball.py:

Allows the user to simulate a game between two NBA teams. 
The results are based on stats that haven't been shown to be good predictors of results. 
However, they are the best easily translatable statistics for generating a running score, 
which is how this simulator works. There is generally a decent correlation between actual 
team performance and performance within the simulator.

However, there are some notable drawbacks:

1. Teams, on average, score 5% more points than they would in real games. This has been tempered in the 
multiple-game-simulation mode, but it is only applied to the end result and not within the engine that 
drives the simulations themselves.

2. There is extreme volatility in the results. Instead of the back-and-forth nature of the real game, 
simulated games may see margins balloon to 35+ points, even for inferior teams. The multiple-game-simulation mode does 
a good job of tempering this and providing a realistic result, however. 
(Note: If you'd like to see relatively random results with a bit more semblance to reality, 
simulate 2-3 games between the teams at once.) I may attempt to temper this affect within individual games by improving team ratings when they fall down by a certain number of points.

3. Finally, free throws have been overly simplified. For now, only two at a time may attempted, so and-1 attempts and three-shot-fouls are impossible.

nba_data.txt:

Houses the team data used to fuel the simulation engine in pseudo-CSV form (twice-delimitable, once by ',' and once by '-'). 
This data will be updated daily, or as close to that as possible.
