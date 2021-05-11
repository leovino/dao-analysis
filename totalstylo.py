# as always we start with importing the libraries that we are going to need
# brandonrose.com/clustering

import re, nltk
from pandas import DataFrame
import numpy as numpy

# to conduct the analysis we are going to need afew other libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram

# matplotlib for viz
import matplotlib.pyplot as plt

# load in texts:
with open('dereklin.txt', 'r', encoding='utf8') as rf:
    lintext = rf.read()

with open('stephenmitchell.txt', 'r', encoding='utf8') as rf:
    mitchelltext = rf.read()

with open('jameslegge.txt', 'r', encoding='utf8') as rf:
    leggetext = rf.read()

with open('giafufeng.txt', 'r', encoding='utf8') as rf:
    fengtext = rf.read()

with open('brucelinnell.txt', 'r', encoding='utf8') as rf:
    linnelltext = rf.read()

# concatenate it for easy use
totalDao = lintext + mitchelltext + leggetext + fengtext + linnelltext

# break into each author section
daos = re.split(r"82",totalDao)
#print(len(daos))


# containers for information
labels = []
author = []
i = 0

# go through the items in the list
for text in (daos):
    
    if i == 0:
        author = "Lin"
    if i == 1:
        author = "Mitchell"
    if i == 2:
        author = "Legge"
    if i == 3:
        author = "Feng"
    if i == 4:
        author = "Linnell"

    if author != None:
        currentauthor = i
        labels.append(author)

    i = i + 1
    #print(author)

vectorizer = TfidfVectorizer(max_features=1000, use_idf=False)

count_matrix = vectorizer.fit_transform(daos)

# get the distances between all of the documents.
distances = euclidean_distances(count_matrix)

# first we can group documents together based on which ones are closest
# we will use the "ward" algorithm to do it
linkages = linkage(distances, 'ward')

# we will use scipy's dendogram function
dendrogram(linkages, labels=labels, orientation='right', leaf_font_size=8, leaf_rotation=45)

# adjust how it looks a bit
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

plt.tight_layout()

# author_dictionary = {"['Lin']": 0, "['Mitchell']": 1, "['Legge']": 2, "['Feng']": 3, "['Linnell']": 4}
# print(author_dictionary)
# color_dictionary = {0: "blue", 1: "red", 2: "green", 3: "black", 4: "purple"}

# # create an axis object to manipulate the color of our labels
# ax = plt.gca()

# # get the labels
# labels = ax.get_ymajorticklabels()
# print(labels)

# # interate through the labels and change their colors
# for label in labels:
#     #label.set_color(color_dictionary[label.get_text()])
#     label_text = label.get_text()
#     print("101", label_text)
#     author = author_dictionary[label_text]
#     color = color_dictionary[author]
#     label.set_color(color)

plt.show()


