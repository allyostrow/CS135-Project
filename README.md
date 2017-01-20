# Final Project Proposal
We will be generating several animated maps based on the quantity of Hillary Clinton tweets and Donald Trump tweets in locations across the country (or specifically swing states depending on how our data turns out). Color will vary depending on the candidate and brightness will vary with quantity of tweets. These maps would be distinguished by time frame. One map would span the night of the election, another would span the 6 months preceding the election, and another a year before the election. We will be creating filters that we feel relate to these candidates or stances held by these candidates.

In terms of what we find interesting, we hope to do some sort of political analysis based on public opinion. This is especially considering the fact that the election result was such a surprise. This structure can ideally be used to analyze other historical elections, or the change of public awareness of any issue over time.

## Data Plan
Our hope is to scrape data from twitter and therefore be able to extract the content and location of tweets from a specific historical time period.

## Implementation Plan
We will start with some of the concepts from our Twitter and Word Clouds Lab and our Purple America lab, but will be using different code. For example, we are extracting data from Twitter in a different way (we are scraping data from Twitter). Additionally, we are using an animation of density patterns rather than the static and rigid density in the Purple America lab. We will also be using heat maps.

### External Libraries
- CS135-get-old-tweets
- Python Image Library
- gmplot
- mpl toolkits
- Twitter API
- geopy

### Milestones
- scraping data from the specific historical time period
- building the data set
  - identifying location using reverse geocode or coordinates field function
  - developing and implementing filters to identify bias
- making the map images
- pairing and labeling the map images from the two filters and generating a single image
- animating the map images


## Deliverables
- Animated "heatmap" with color gradient showing prevalence/density of interest over specified time periods
- code that can be applied to many situations for sentiment analysis analysis over


# Final Project Report
*What you have achieved/learned*
- This project exposed us to many new libraries such as gmplot, geopy (Google Maps API), and mpl toolkits. We also were able to use unfamiliar features in the Python Image Library. We also learned how to create a gif in the command line and a method in which you can open a browser with selenium and take a screenshot. We have learned, most importantly, how to fail. Things did not go the way we planned. For one, we thought we could use coordinates directly from the json output (from the Twitter API). Turns out, no one reports their coordinates, surprise! Therefore, we had to sift through the json to find the name of the city that the user is based out of and use a separate library to convert the cities to coordinates that we could then map. We also encountered issues in requests limits with geocode. We navigated around this by getting a google maps API for an individual project and creating a new API each time a project exceeded the requests limit. We also learned how to use more element of the PIL such as pasting images side by side and reinforced the skill of creating labels on images that we used in the stocks lab. 

*What open questions remain*
- Is our sample size large enough to do a true, accurate sentiment analysis (<5000 tweets and only using the slogans as filters)?
-


## Instructions to run the code

1. Use CS135-get-old-tweets to produce a csv files that contain the tweet information for a specific query and time period. The command line code format is: python Exporter.py --querysearch "QUERY" --since YYYY-MM-DD --until YYYY-MM-DD --filename “FILENAME”

2. Use a command line argument getloc.py to create a gif with the file from step 1: python3 getloc.py("FILENAME")

Examples:

Hillary & Trump November 2016 Tweets:

- git clone https://github.com/williams-cs/CS135-get-old-tweets.git
- cd CS135-get-old-tweets
- pip install pyquery
- python Exporter.py --querysearch "imwithher" --since 2016-11-01 --until 2016-11-02 --filename “Hil_Nov_1.csv”
  - change the dates and filename to get a number of days of that month
- python Exporter.py --querysearch "makeamericagreatagain" --since 2016-11-01 --until 2016-11-02 --filename “Trump_Nov_1.csv”
  - change the dates and filename to get a number of days of that month

- cd ..
- python3 getloc.py "data/Hil_Nov_1.csv"
  - change the filename until you have produce .json files for each .csv files
- python3 viz.py

Ally's Instructions:

Hillary & Trump November 2016 Tweets:
1. Git clone CS135-get-old-tweets with the command: git clone https://github.com/williams-cs/CS135-get-old-tweets.git. Use this repository to produce a csv files that contain the tweet information for a specific query and time period. The command line code format is: python Exporter.py --querysearch "QUERY" --since YYYY-MM-DD --until YYYY-MM-DD --filename “FILENAME”.

2. Use a command line to run getloc.py. This creates a json file of coordinates with the location file from step 1. This step must be repeated for each location file. The command is: python3 getloc.py "filename"
(in our case, all files were in the data folder so we used "data/filename.csv")

3. Use the command line to run viz.py in order to generate a gif. The command is: python3 viz.py
