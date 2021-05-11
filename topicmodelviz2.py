# let's visualize the information from this topic model using the output files
import matplotlib.pyplot as plt
import seaborn as sns
from utilites_pv import open_text

# let's load in the information. tendoctopics.txt will contain info on the
# topics
document_topic_info = open_text("tendoctopics.txt")
document_topic_info = document_topic_info.split("\n")
document_topic_prevelance = {}

for line in document_topic_info:
    if line != "":
        info = line.split("\t")
        document_topic_prevelance[str(int(info[0])+1)] = [float(weight) for weight in info[2:]]

#[1]lin [84]linnell [166]feng [249]legge [332]mitchell

#adjust visuals
weights = document_topic_prevelance["332"]
index = [i for i in range(len(weights))]
sns.barplot(index, weights, color="darkseagreen")
plt.xlabel("Topics")
plt.ylabel("Weights")
plt.title("Topic Weight in Mitchell Chapter 1")
plt.tight_layout()
plt.show()