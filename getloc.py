from geopy import geocoders, exc
import json
import re
import csv
import sys

def locgrab(filename):
    '''
    Takes the filename of a csv produced by CS135-get-old-tweets and returns a list of locations from those tweets.
    Note that not all of the tweets have locations, in fact only about 5-10% pf the tweets will have locations.
    '''
    locations = []
    with open(filename, 'r') as fout:
        tweets = list(csv.reader(fout, delimiter = ';'))[1:]
        for tweet in tweets:
            if tweet[5] != "":
                locations.append(tweet[5])
    return locations


def loc_to_coord(codes):
    """
    Converts a list of locations into a list of coordinates that can then be plotted.
    If the exception "geopy.exc.GeocoderQuotaExceeded" is thrown, then create a new
    Google Maps API key.
    """
    def adfilter(codes):
        return re.findall("""[a-zA-Z]+, [A-Z]{2}""", ";".join(codes))

    api_key = "AIzaSyCxQCjOrHFAf7T-W3vtUYqWkgSFkvMjxN4"

    g = geocoders.GoogleV3(api_key = api_key)
    coords = {"lat":[], "long":[]}
    for code in adfilter(codes):
        if code != "":
            try:
                place = g.geocode(code)
                if place != None:
                    coords["lat"].append(place.latitude)
                    coords["long"].append(place.longitude)
            except (exc.GeocoderTimedOut, exc.GeocoderQueryError):
                    pass
    return coords


if __name__ == "__main__":


    places = locgrab(sys.argv[1])
    coords = loc_to_coord(places)

    ### Upload coordinates in their dictionary form to a .json file in the coordinates folder
    fin = "coordinates/"+sys.argv[1][5:-4]+".json"
    with open(fin, "a") as fout:
        json.dump(coords, fout)
        fout.write("\n")
