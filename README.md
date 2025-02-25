# UFC Scorigami: Visualizing Unique Fight-Ending Times
By: Ethan Ooi

**UFC Scorigami** is an analytical model that tracks fight-ending times in UFC history, inspired by NFL Scorigami. It provides an **interactive table** where users can explore every unique fight-ending time ranging from UFC 1 to UFC Fight Night: Cejudo vs. Song.

## Interactive Table
[UFCGami on Render](https://ufcgami-1.onrender.com) 

*This site may take ~50s to load if inactive due to free-tier hosting on Render.*

## Data
This repository contains all the code and data used for the project. A web scraper for [UFC Fights](http://ufcstats.com/statistics/events/completed) can be found in [ufcstatswebscraper.ipynb](ufcstatswebscraper.ipynb). This will provide you with [ufcfights.csv](ufcfights.csv) which I use in [create_ufc_fights.sql](create_ufc_fights.sql) to create a refined database for Python manipulation and analysis. The rest of the code for finding all the unique fight-ending times and the creation of the interactive Dash table is in [UFCgami.py](UFCgami.py).

## Key Findings
The **interactive table** has every specific time, but these are some general takeaways. 

- The earliest finish in UFC history occured at 0:05 in the 1st round.
- We can see that there are many missing values in the 4th and 5th round. This is because UFC fights are generally 3 rounds, with the exception of **ALL** title fights, Fight Night main events, and a few other co-main or special fights, where these fights are 5 rounds.
- Every second of the 1st round has seen a stoppage, except for the first 4 seconds.