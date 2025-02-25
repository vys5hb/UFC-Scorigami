# UFC Scorigami
By: Ethan Ooi

**UFC Scorigami** is an analytical model that tracks fight-ending times in UFC history, inspired by NFL Scorigami. It provides an **interactive table** where users can explore every unique fight-ending time ranging from UFC 1 to UFC Fight Night: Cejudo vs. Song.

## Interactive Table
[UFCGami on Render](https://ufcgami-1.onrender.com) 
*This site may take ~50s to load if inactive.*

## Data
This repository contains all the code and data used for the project. A web scraper for [UFC Fights](http://ufcstats.com/statistics/events/completed) can be found in `ufcstatswebscraper.ipynb`. This will provide you with `ufcfights.csv` which I use in `create_ufc_fights.sql` to create a refined database for Python manipulation and analysis.

## Key Findings
The **interactive table** has every specific time, but there are some general takeaways. 

The earliest finish in UFC history at 0:05 in the first round.

We can see that there are many 