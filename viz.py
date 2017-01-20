import gmplot
import os
import sys
import json
import re
from geopy import geocoders, exc
from selenium import webdriver
from time import sleep
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def imagegrab(filename, name):
    """
    Converts a json file of coordinates into a heatmap image with given name
    """
    with open(filename) as fout:
        coords = json.load(fout)
    gmap = gmplot.GoogleMapPlotter(39.8282,-98.5795, 4)
    gmap.heatmap(coords["lat"], coords["long"], radius = 30)
    gmap.draw("{}.html".format(name))
    browser = webdriver.Chrome()
    browser.get("file:///C:/Users/Elliott/roxannecorbeil-project/{}.html".format(name))
    sleep(1)
    browser.save_screenshot("{}.png".format(name))
    browser.close()

def label_images(filename, label):
    """
    Takes an image and labels it with the appropriate filter name, overwrites the initial file
    """
    im = Image.open(filename)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", size=250)
    font2 = ImageFont.truetype("arial.ttf", size=150)
    fin = filename.split("_")
    if fin[1] == "Yr":
        month = fin[2][:-4]
        l = ["Dec, 2015", "Jan, 2016", "Feb, 2016", "Mar, 2016", "Apr, 2016", "May, 2016", "Jun, 2016", "Jul, 2016", "Aug, 2016", "Sep, 2016", "Oct, 2016", "Nov, 2016"]
        time = l[int(month)-1]
    else:
        day = fin[2][:-4]
        time = "Nov {}, 2016".format(day)
    draw.text((0, 0), label, (0, 0, 0), font = font)
    draw.text((0, 300), time, (0, 0, 0), font = font2)
    im.save(filename)

def prepare_images(f1, f2, f3, filter_1, filter_2):
    """
    Takes image files f1 (str) and f2 (str), labels them with their respective filters (str), and displays them side by side in a new file, f3 (str).
    """
    label_images(f1, filter_1)
    label_images(f2, filter_2)

    im1 = Image.open(f1)
    im2 = Image.open(f2)

    max_height = max(im1.height, im2.height) #in our case the two maps are the same size, but this would allow for the use of two maps of different heights
    new_image = Image.new('RGB', (im1.width + im2.width, max_height))
    new_image.paste(im = im1, box = (0, 0))
    new_image.paste(im = im2, box = (im1.width + 30, 0)) #30 pixel horizontal space between file1 and file2
    new_image.save(f3 + ".png")

if __name__ == "__main__":

    for num in range(1, 13):
        imagegrab("coordinates/Trump_Yr_{}.json".format(num), "Trump{}".format(num))
        imagegrab("coordinates/Hil_Yr_{}.json".format(num), "Hillary{}".format(num))
        prepare_images("Trump{}.png".format(num), "Hillary{}.png".format(num), "Months{}".format(num), "Hillary", "Trump")
    os.system("magick -delay 100 -loop 0 Months*.png Months.gif")

    for num in range(1,8):
        imagegrab("coordinates/Trump_Nov_{}.json".format(num), "Trumpn{}".format(num))
        imagegrab("coordinates/Hil_Nov_{}.json".format(num), "Hillaryn{}".format(num))
        prepare_images("Trumpn{}.png".format(num), "Hillaryn{}.png".format(num), "November{}".format(num), "Hillary", "Trump")
    os.system("magick -delay 100 -loop 0 November*.png November.gif")
