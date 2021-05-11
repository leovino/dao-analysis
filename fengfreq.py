# import libraries
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# open the text file
with open('giafufeng.txt','r', encoding='utf8') as rf:
    text = rf.read()

# clean text      
text = text.lower()
text = text.replace(",", "")
text = text.replace('.', "")

# replace new lines
text = text.replace('\n','')
text = text.replace('""',"" )

# get the words in the text
words = text.split(" ")

# get the unique words
unique_words = set(words)

# hold results
word_frequencies = {}

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

# get top ten words
objects = (sorted_words[:10])

# y axis
yaxisvals = objects
yaxis = np.arange(len(objects))

# make a list to sort words
first_few_freqs = []
# You wrote a for loop earlier that iterates over the first 10 lines of sorted_words. Let's recycle that code!
for word in sorted_words[:10]:
    first_few_freqs.append(word_frequencies[word])
# x axis
xaxis = first_few_freqs

# set graph visuals
plt.bar(yaxis, xaxis, align='center', alpha=0.5)
plt.xticks(yaxis, objects)
plt.ylabel('Frequency')
plt.title('Most Common Words in Feng')

plt.show()
