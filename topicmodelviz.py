# let's visualize the information from this topic model using the output files
import matplotlib.pyplot as plt
import seaborn as sns
from utilites_pv import open_text

# let's load in the information. tentopickeys.txt will contain info on the
# topics
topics_info = open_text("tentopickeys.txt")
topics_info = topics_info.split("\n")
topics = {}

#iterate through the topics
for line in topics_info:
    if line != "":
        topic_data = line.split("\t")
        # grab topic number
        topic_number = topic_data[0]
        weight = float(topic_data[1])
        words = topic_data[2].split(" ")
        topics[topic_number] = (weight, words)

# let's visualize this
sns.set()

# seting the index
index = [i for i in range(len(topics))]

# setting the weight
weights = [topics[str(i)][0] for i in range(len(topics))]

# create some labels:
labels = [f"Topic {i}" for i in range(len(topics))]

# adjust the graph visuals
sns.barplot(index, weights, color="forestgreen")
sns.cubehelix_palette(start=.5, rot=-.5, as_cmap=True)
plt.xticks(index, labels, rotation=90)
plt.xlabel('Topic')
plt.ylabel('Weight')
plt.title('Topic Weights')
plt.tight_layout()
plt.show()