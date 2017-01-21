# Final Project Proposal
We will be generating several animated maps based on the quantity of Hillary Clinton tweets and Donald Trump tweets in locations across the country. The color and the intensity of the color will vary with quantity of tweets. These maps are to be distinguished by time frame. One animated map spans the year before the election another spans the first week of November. We use the hashtags #MakeAmericaGreatAgain and #ImWithHer to indicate support for Trump and Clinton respectively.

In terms of what we find interesting, we hope to do some sort of political analysis based on public opinion. This is especially significant to us considering the fact that the election result was such a surprise. This structure can ideally be used to analyze other historical elections, or to track the change of public sentiment with regards to any issue over time.

## Data Plan
Our hope is to scrape data from twitter and therefore be able to extract the content and location of tweets from a specific historical time period.


### External Libraries
- CS135-get-old-tweets
- Python Image Library
- gmplot
- Twitter API
- geopy
- imagemagick
- gifsicle

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
- This project exposed us to many new libraries such as gmplot, geopy (Google Maps API), and mpl toolkits. We also were able to use unfamiliar features in the Python Image Library. We additionally learned how to create a gif in the command line and a method in which you can open a browser with selenium and take a screenshot. Overall though, we have learned, most importantly, how to fail. Things did not go the way we planned. For one, we thought we could use the locations given by the CS135-get-old-tweets historical tweet searches. Turns out, no one reports their location, surprise! In fact, location was only reported for about .05% of tweets. Therefore, the plan was to use the Twitter API to find the user location for the users of all of the tweets. We had to sift through the json to find the name of the city that the user is based out of and use a separate library to convert the cities to coordinates that we could then map. We did all of this, only to find out that Twitter limited us to 30 calls at a time, which ended up being too inefficient for us to use. Therefore, we just ended up using the locations reported with the tweets and using geopy to get coordinates for each city. We also encountered issues in requests limits with geocode. We navigated around this by getting a google maps API for an individual project and creating a new API each time a project exceeded the requests limit. In addition, we learned how to use more elements of PIL, such as pasting images side by side and reinforced the skill of creating labels on images that we used in the stocks lab.
- We think that despite its imperfections, our final result is a really interesting way to look at public sentiment surrounding such a controversial election and has the potential to be adapted into something that is truly relevant and useful.

*What open questions remain*
- Is our sample size large enough to do a true, accurate sentiment analysis (<5000 tweets and only using the slogans as filters)?
- What other relevant slogans or filters could we use?
- How could we circumvent the Twitter API limits to collect the locations for a larger proportion of the tweets?


## Instructions to run the code
1. Install pyquery, gmplot, selenium, geopy, and pillow

2. Download chromedriver

3. Git clone CS135-get-old-tweets with the command: git clone https://github.com/williams-cs/CS135-get-old-tweets.git. Use this repository to produce csv files that contain the tweet information for a specific query and time period. The command line code format is: python Exporter.py --querysearch "QUERY" --since YYYY-MM-DD --until YYYY-MM-DD --filename “FILENAME”.

4. Use a command line to run getloc.py. This creates a json file of coordinates with the location file from step 1. This step must be repeated for each location file. The command is: python3 getloc.py "filename"
(in our case, all files were in the data folder so we used "data/filename.csv")

3. Use the command line to run viz.py in order to generate a gif. The command is: python3 viz.py. If you are using your own files, you must edit viz.py, specifically ajusting the formatted file names in 'if __name__ == "__main__":'

## Example:

Hillary & Trump November 2016 Tweets:

- pip install pyquery, gmplot, selenium, time, geopy, and pillow
- download chromedriver

In the CS135-get-old-tweets repository:
- python Exporter.py --querysearch "imwithher" --since 2016-11-01 --until 2016-11-02 --filename “Hil_Nov_1.csv”
  - change the dates and filename to get a number of days of that month
- python Exporter.py --querysearch "makeamericagreatagain" --since 2016-11-01 --until 2016-11-02 --filename “Trump_Nov_1.csv”
  - change the dates and filename to get a number of days of that month

In the roxannecorbeil-project repository:
- python3 getloc.py "data/Hil_Nov_1.csv"
  - change the filename until you have produce .json files for each .csv files
- python3 viz.py

Note: It may be necessary to resize the gifs. If so, make use of the gifsicle command line tool.
