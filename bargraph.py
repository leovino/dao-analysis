import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

yaxis = (412,192,158,155,142,134,99,96,69,68)
xaxis = ("the","is","and","to","not","of","it","be","who","are")

plt.bar(xaxis, yaxis, align='center', alpha=0.5)
plt.xticks(yaxis, xaxis)
plt.ylabel('Frequency')
plt.title('Most Common Words')

plt.show()