# import needed libraries
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# open the text file
with open('brucelinnell.txt','r', encoding='utf8') as rf:
    text = rf.read()

# clean up the text  
text = text.lower()
text = text.replace(",", "")
text = text.replace('.', "")

# replace newline characters
text = text.replace('\n','')
text = text.replace('""',"" )

# get the words in the text
words = text.split(" ")

# get the unique words
unique_words = set(words)

word_frequencies = {}

# iterate through the text
for i,word in enumerate(unique_words):
    if i % 100 == 0:
        print(i, word)
    frequency = words.count(word)
    word_frequencies[word] = frequency

# sort the keys by their values
sorted_words = sorted(word_frequencies, key=word_frequencies.get, reverse=True)

# get top 10 words
for word in sorted_words[:10]:
    print(word, word_frequencies[word])

# the first most common words was just a space
objects = (sorted_words[1:11])

# y axis
yaxisvals = objects
yaxis = np.arange(len(objects))

# get top ten words
first_few_freqs = []
for word in sorted_words[1:11]:
    first_few_freqs.append(word_frequencies[word])
# x axis
xaxis = first_few_freqs

#set graph visuals
plt.bar(yaxis, xaxis, align='center', alpha=0.5)
plt.xticks(yaxis, objects)
plt.ylabel('Frequency')
plt.title('Most Common Words in Linnell')

plt.show()
