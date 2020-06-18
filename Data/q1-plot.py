import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'

# Import data
(grade,hits) = (np.genfromtxt('q1-scatter.csv',dtype=float,delimiter=',',skip_header=2,usecols=(6)),
                np.genfromtxt('q1-scatter.csv',dtype=int,delimiter=',',skip_header=2,usecols=(7))) # Should be cols 5 and 6, since genfromtxt *should* start counting at 0, but for some reason it has decided to start countintg from 1.

# Plot setup
#plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(hits,grade,marker='+')
ax.set_title('Quiz 1: Measuring motion')
ax.set_xlabel('Unique page views')
ax.set_ylabel('Quiz 1 grade')
#plt.show()
plt.savefig('q1-plot.png')
