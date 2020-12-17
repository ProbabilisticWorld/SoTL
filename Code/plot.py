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
    r(N-1): average
    rN: st dev

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
    (grade,hits) = (np.genfromtxt(input,dtype=float,delimiter=',',skip_header=2,skip_footer=2,usecols=(6)),
                    np.genfromtxt(input,dtype=int,delimiter=',',skip_header=2,skip_footer=2,usecols=(7))) # Should be cols 5 and 6, since genfromtxt *should* start counting at 0, but for some reason it has decided to start countintg from 1.

    # Import avg and stdev for quiz grade and number of hits; https://stackoverflow.com/a/38705069
    qstats = np.genfromtxt(input,dtype=float,delimiter=',',skip_header=2,usecols=(5)) # genfromtxt *should* start counting at 0, but for some reason it has decided to start countintg from 1? AND ALSO it is jumping over one column for last two rows???? So I end up needing the correct index for this genfromtxt, but for the wrong reason and it is inconsistent with the previous genfromtxt\
    (qavg,qstdev) = (qstats[-2:-1][0],qstats[-1:][0]) # Average is second-to-last row; stdev is last row
    hstats = np.genfromtxt(input,dtype=float,delimiter=',',skip_header=2,usecols=(6)) # See comment on qstats
    (havg,hstdev) = (hstats[-2:-1][0],hstats[-1:][0]) # Average is second-to-last row; stdev is last row

    # Plot data
    fig, ax = plt.subplots()
    ax.scatter(hits,grade,marker='+')

    # Plot stats
    ax.axhline(qavg,linestyle='solid',label='Quiz avg')
    ax.axhline(qavg+qstdev,linestyle='dashed')
    ax.axhline(qavg-qstdev,linestyle='dashed',label=r'$\pm$stdev')

    ax.axvline(havg,color='orange',linestyle='solid',label='Avg hits')
    ax.axvline(havg+hstdev,color='orange',linestyle='dashed')
    ax.axvline(havg-hstdev,color='orange',linestyle='dashed',label=r'$\pm$stdev')

    # Configure and label
    ax.set_title('Quiz '+str(nquiz)+': '+name)
    ax.set_xlabel('Total module views')
    ax.set_ylabel('Quiz '+str(nquiz)+' grade')
    ax.legend(loc=4)
    ax.set_xlim(left=-1) # shifted slightly negative to see ticks at x = 0
    ax.set_ylim(-0.1,1.1) # shifted slightly negative to see ticks at y = 0 and y = 1

    # View/save
    #plt.show()
    plt.savefig('q'+str(nquiz)+'-plot.pdf')
    plt.savefig('q'+str(nquiz)+'-plot.png')

if __name__ == '__main__':
    yqtr='sp20'
    makeplots('%s/q1-scatter-lect-ex.csv'%yqtr,1,'Measuring motion')
    makeplots('%s/q2-scatter-lect-ex.csv'%yqtr,2,'Energy')
    makeplots('%s/q3-scatter-lect-ex.csv'%yqtr,3,'Momentum')
    makeplots('%s/q4-scatter-lect-ex.csv'%yqtr,4,'Force')
    makeplots('%s/q5-scatter-lect-ex.csv'%yqtr,5,'Work')
