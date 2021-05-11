# import needed libraries
import nltk, gensim, os

import regex as re

from utilites_pv import open_text

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

    # originally made for labels, but then abandoned
    currentauthor = i

    # tokenize the current section of the text 
    tokenized_text = nltk.word_tokenize(text)

    # refine the text
    refined = [word for word in tokenized_text if word.isalnum()]

    daos.append(refined)

    i = i + 1

# gensim is designed to run on lists of integers, so we need to respect that unfortunately
corpus_dictionary = gensim.corpora.Dictionary(daos)
#corpus_dictionary.filter_n_most_frequent(150)
#corpus_dictionary.filter_extremes(no_above=.3)

processed_corpus = [corpus_dictionary.doc2bow(totalDao) for totalDao in daos]

# ACTUALLY TOPIC MODEL
number_of_topics = 10

# Once you've done this we will need to tell the code where mallet lives
malletPath = os.path.join("mallet-2.0.8","bin","mallet")

# train the model:
ldaModel = gensim.models.wrappers.ldamallet.LdaMallet(malletPath,corpus=processed_corpus,
                            id2word=corpus_dictionary,num_topics=number_of_topics,
                            optimize_interval=50, prefix="ten")

corpusLda = ldaModel[processed_corpus]

# show the topics and the top five words
topics = ldaModel.show_topics(num_topics=20, num_words=5)

for topic in topics:
    print(topic)
