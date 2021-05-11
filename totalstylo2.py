# import needed libraries
import nltk, gensim, os

import regex as re

# make opening the files easier
from utilites_pv import open_text

# more libraries
import re, nltk
from pandas import DataFrame
import numpy as numpy

# to conduct the analysis we are going to need a few other libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

# matplotlib for viz
import matplotlib.pyplot as plt

# load in the texts
linText = open_text("dereklin.txt")
linnellText = open_text("brucelinnell.txt")
fengText = open_text("giafufeng.txt")
leggeText = open_text("jameslegge.txt")
mitchellText = open_text("stephenmitchell.txt")

# divide each text into sections
linSections = re.split(r'\d+', linText)
linnellSections = re.split(r'\d+', linnellText)
fengSections = re.split(r'\d+', fengText)
leggeSections = re.split(r'\d+', leggeText)
mitchellSections = re.split(r'\d+', mitchellText)


# concatenate the texts
totalDao = linSections + linnellSections + fengSections + leggeSections + mitchellSections

# container for all the texts
refinedText = []

# Let's do a bit of cleaning first to prep our texts for analysis in gensim
lemmatizer = nltk.WordNetLemmatizer()

# empty variables and containers
author = []
currentauthor = []
i = 0
daos = []
labels = []

# check length
print(len(totalDao))

# go through the items in the list
for text in (totalDao):
    
    #410 sections total, each author has 82 (the item at position 0 is nothing)
    if i in range(0, 82):
        labels.append("Lin")
    if i in range(83, 165):
        labels.append("Linnell")
    if i in range(166, 248):
        labels.append("Feng")
    if i in range(249, 331):
        labels.append("Legge")
    if i in range(332, 414):
        labels.append("Mitchell")

    currentauthor = i
    
    # tokenize and refine
    tokenized_text = nltk.word_tokenize(text)
    
    refined = " ".join([word for word in tokenized_text if word.isalnum()])

    daos.append(refined)

    i = i + 1

vectorizer = TfidfVectorizer(max_features=1000, use_idf=False)

count_matrix = vectorizer.fit_transform(daos)

# get the distances between all of the documents.
distances = euclidean_distances(count_matrix)

# first we can group documents together based on which ones are closest
# we will use the "ward" algorithm to do it
linkages = linkage(distances[:406], 'ward')

# we will use scipy's dendogram function
dendrogram(linkages, labels=labels, orientation='right', leaf_font_size=8, leaf_rotation=45)

# adjust how it looks a bit
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

plt.tight_layout()

# distinguish between the authors
author_dictionary = {"Lin": 0, "Mitchell": 1, "Legge": 2, "Feng": 3, "Linnell": 4}
print(author_dictionary)
color_dictionary = {0: "blue", 1: "red", 2: "green", 3: "black", 4: "purple"}

# create an axis object to manipulate the color of our labels
ax = plt.gca()

# get the labels
labels = ax.get_ymajorticklabels()

# interate through the labels and change their colors
for label in labels:
    #label.set_color(color_dictionary[label.get_text()])
    label_text = label.get_text()
    author = author_dictionary[label_text]
    color = color_dictionary[author]
    label.set_color(color)

plt.show()


