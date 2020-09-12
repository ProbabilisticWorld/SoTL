import datetime as dt
import numpy as np
import csv

def hits(input):
    '''
    For given page, count unique hits from each student.

    input is a csv file. Must be input as 'filename.csv' (including quotes)
    The csv file must be formatted as follows: Two header rows (these get ignored); first column has names, second column has timestamps
    '''
    # Load text, slice by name and time
    (names,times0) = (np.genfromtxt(input,dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(0)),
                      np.genfromtxt(input,dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(1)))

    # Make array to put dates into, in dateimte format
    times = np.empty(len(times0),dtype=object)

    # Convert dates to datetime format, populate times array
    for i in range(len(times)):
        times[i] = dt.datetime.strptime(times0[i],'%Y-%m-%d %H:%M:%S')


    # Compare times: flag hits from a given student that are separated by less than 60 s
    # Make new arrays for flagged data
    names_flagged = np.empty_like(names)
    np.copyto(names_flagged,names)
    times_flagged = np.empty_like(times)
    np.copyto(times_flagged,times)
    for i in range(len(times)):
        if i == 0:
            i = 1 # start at 1 so I can compare to item 0
        elif names[i] == names[i-1]:
            if times[i] <= times[i-1] + dt.timedelta(seconds=60):
                names_flagged[i] = 0 # Flag name as 0
                times_flagged[i] = 0 # Flag time as 0

    # Removed flagged entries from above
    indices = [] # This will be used in the np.delete() function
    for i in range(len(names)):
        if names_flagged[i] == '0':
            indices.append(i)

    # For both names and times, copy to a new array, then remove flagged entries
    names_cropped = np.empty_like(names_flagged) # define new array
    np.copyto(names_cropped,names_flagged) # copty data to new array
    names_cropped = np.delete(names_cropped,indices) # remove flagged entries

    times_cropped = np.empty_like(times_flagged) # define new array
    np.copyto(times_cropped,times_flagged) # copy data to new array
    times_cropped = np.delete(times_cropped,indices) # remove flagged entries


    # Count hits for each name
    # Make empty for final data: one for names, one for count
    names_no_repeats = []
    hits = []

    s = 1 # start counting at 1
    for i in range(len(names_cropped)):
        if i == 0:
            i = 1 # start at 1 so I can compare to item 0
        elif names_cropped[i] == names_cropped[i - 1]:
            s = s + 1
        else:
            names_no_repeats.append(names_cropped[i-1])
            hits.append(s)
            s = 1

    # Combine into an array with two rows: one for names, one for counts
    ## I would prever columns, but...
    data = np.array([names_no_repeats,hits])

    # Write to csv file
    output = 'data-'+input
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    print('Commence data analysis')

    # q1
    # list_of_files = ['q1-accel-defn.csv',
    # 'q1-single-vector-2D.csv',
    # 'q1-single-vector-polar.csv',
    # 'q1-vector-addition.csv',
    # 'q1-vector-subtraction.csv',
    # 'q1-velocity-defn.csv']

    # q2
    # list_of_files = ['q2-E-budget.csv',
    # 'q2-E-cons-defn.csv',
    # 'q2-E-rot-example.csv',
    # 'q2-E-spr-ex.csv',
    # 'q2-I-table.csv',
    # 'q2-Ug.csv',
    # 'q2-Usp.csv',
    # 'q2-down-ramp.csv',
    # 'q2-krot.csv',
    # 'q2-ktrans.csv',
    # 'q2-ugrav-g-defn.csv',
    # 'q2-up-ramp.csv']

    # q3
    # list_of_files=['q3-1Dcoll-ex.csv',
    # 'q3-2Dcoll-defn.csv',
    # 'q3-2Dcoll-ex.csv',
    # 'q3-ball-pend-deriv.csv',
    # 'q3-p-cons-ex1.csv',
    # 'q3-p-cons-ex2.csv',
    # 'q3-p-defn.csv',
    # 'q3-p-symb-ex.csv']

    # q4
    # list_of_files=['q4-3rd-law-ex.csv',
    # 'q4-elevator-ex.csv',
    # 'q4-flower-basket-2d-ex.csv',
    # 'q4-incline-accel-ex.csv',
    # 'q4-incline-static-ex.csv',
    # 'q4-potatoes-2d-ex.csv',
    # 'q4-simple-1d-ex.csv',
    # 'q4-spring-ex.csv']

    # q5
    list_of_files=['q5-box-stack-compare.csv',
    'q5-box-stack-ex.csv',
    'q5-friction-K-only-ex.csv',
    'q5-friction-ramp-ex.csv',
    'q5-spring-quadratic-ex.csv'
    ]

    for i in range(len(list_of_files)):
        print('Analyzing '+list_of_files[i])
        hits(list_of_files[i])

    print('Done. Have a nice day :)')
