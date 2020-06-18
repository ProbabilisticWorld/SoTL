import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'

def makeplots(input, nquiz, name):
    '''
    Generate plots from csv files.

    All input files must be 'name.csv' (including quotes), formatted as follows (from Cavnas output):
    r1: header info
    r2: points possible
    c0: names
    c1: ID
    c2: SIS user ID
    c3: SIS login ID
    c4: Raw score
    c5: Percent (This is added manually--not from canvas)
    c6: Hits on relevant pages (This is added manually--not from canvas)

    nquiz is the quiz number
    name is the name of the quiz
    '''

    # Import data
    (grade,hits) = (np.genfromtxt(input,dtype=float,delimiter=',',skip_header=2,usecols=(6)),
                    np.genfromtxt(input,dtype=int,delimiter=',',skip_header=2,usecols=(7))) # Should be cols 5 and 6, since genfromtxt *should* start counting at 0, but for some reason it has decided to start countintg from 1.

    # Plot data
    fig, ax = plt.subplots()
    ax.scatter(hits,grade,marker='+')

    # Configure and label
    ax.set_title('Quiz '+str(nquiz)+': '+name)
    ax.set_xlabel('Unique page views')
    ax.set_ylabel('Quiz '+str(nquiz)+' grade')
    ax.set_xlim(left=-1) # shifted slightly negative to see ticks at x = 0
    ax.set_ylim(-0.1,1.1) # shifted slightly negative to see ticks at y = 0 and y = 1

    # View/save
    #plt.show()
    plt.savefig('q'+str(nquiz)+'-plot.pdf')

if __name__ == '__main__':
    makeplots('q1-scatter.csv',1,'Measuring motion')
    makeplots('q2-scatter.csv',2,'Energy')
    makeplots('q3-scatter.csv',3,'Momentum')
