# import needed libraries
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# open the text file
with open('stephenmitchell.txt','r', encoding='utf8') as rf:
    text = rf.read()

# clean up the text    
text = text.lower()
text = text.replace(",", "")
text = text.replace('.', "")

# replace newlines
text = text.replace('\n','')
text = text.replace('""',"" )


# get the words in the text
words = text.split(" ")

# get the unique words
unique_words = set(words)

# empty variable to hold results
word_frequencies = {}

# iterate
for i,word in enumerate(unique_words):
    if i % 100 == 0:
        print(i, word)
    frequency = words.count(word)
    word_frequencies[word] = frequency

# sort the keys by their values
sorted_words = sorted(word_frequencies, key=word_frequencies.get, reverse=True)

#sorted_words_and_frequencies = [[word, word_frequencies[word]] for word in sorted_words]
for word in sorted_words[:10]:
    print(word, word_frequencies[word])

objects = (sorted_words[:10])

# set y axis
yaxisvals = objects

yaxis = np.arange(len(objects))

# sort by word freq
first_few_freqs = []
for word in sorted_words[:10]:
    first_few_freqs.append(word_frequencies[word])
# define x axis
xaxis = first_few_freqs

# adjust data visuals
plt.bar(yaxis, xaxis, align='center', alpha=0.5)
plt.xticks(yaxis, objects)
plt.ylabel('Frequency')
plt.title('Most Common Words in Mitchell')

plt.show()
