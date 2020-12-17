import datetime as dt
import numpy as np
import csv

# Plan for Version 2.1:
## Fixing error where some hits aren't counted
## Referencing by ID (int) instead of Name (str) so I can make one single array to use
## Turning timestamps into ints instead of...whatever dtype datetime.datetime is
## Combining two separate arrays into one

def dt_to_int(dt_time): # https://stackoverflow.com/a/28154159 # I know this is **very bad**, but I don't care--I'm ultimately just using it to compare two times that are close in time, and to facilitate using arrays of numbers instead of objects and/or strings
    '''
    Convert datetime to an integer
    Input is in datetime.datetime format
    '''
    return 10**10*dt_time.year + 10**8*dt_time.month + 10**6*dt_time.day + 10**4*dt_time.hour + 10**2*dt_time.minute + 1*dt_time.second

def hits(input):
    '''
    For given page, count unique hits from each student.

    input is a csv file. Must be input as 'filename.csv' (including quotes)
    The csv file must be formatted as follows: Two header rows (these get ignored); first column has names, second column has timestamps
    '''
    # Load text, slice by name and time
    (names,times0) = (np.genfromtxt(input,dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(0)),
                      np.genfromtxt(input,dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(1)))

    # Array of IDs insetad of names:
    ids = np.empty(len(names),dtype=int)
    for i in range(len(ids)):
        ids[i] = name_to_id[names[i]]

    # Make array to put dates into int format
    times = np.empty(len(times0),dtype=int)

    # Convert dates to datetime format, populate times array
    for i in range(len(times)):
        # use dummy variable put into datetime format
        thedonald = dt.datetime.strptime(times0[i],'%Y-%m-%d %H:%M:%S')
        # put into array as int
        times[i] = dt_to_int(thedonald)

    # Combine into one array
    combined = np.empty([len(ids),2],dtype=int)
    for i in range(len(ids)):
        combined[i][0] = ids[i]
        combined[i][1] = times[i]

    # Compare times: If two timestamps are separated by less than 60s, make the second one zero (must do the same for both names and times arrays)
    time_compare = np.empty_like(combined) # define new array
    np.copyto(time_compare,combined) # copy data to new array

    for i in range(len(ids)):
        if combined[i][0] == combined[i-1][0]: # comparing to [i - 1] is fine; it wraps to the end of the array
            if combined[i][1] <= combined[i-1][1] + 60:
                time_compare[i][1] = 0 # Flag time as 0

    # Removed flagged entries from above
    ## identify which entries along axis 1 (i.e. across all rows of each column) are nonzero; return array with only rows that have all nonzero entries
    cropped = time_compare[np.all(time_compare != 0, axis = 1)]

    output = 'tmp.csv'
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cropped)

    # Count hits for each name
    # Make empty for final data: one for names, one for count
    ids_no_repeats = []
    names_no_repeats = []
    hits = []

    s = 1 # start counting at 1
    for i in range(len(cropped)):
        ip1 = i + 1
        mod = ip1 % len(cropped) # (i + 1) modulo array length
        if cropped[i][0] == cropped[mod][0]: # use [(i+1) mod len] so the index wraps around; this ensures that the last student in the list is not skipped
            s = s + 1
        else:
            ids_no_repeats.append(cropped[i][0])
            names_no_repeats.append(id_to_name[cropped[i][0]])
            hits.append(s)
            s = 1

    # Combine into an array with three columns: names, IDs, hits
    data = np.column_stack((names_no_repeats,ids_no_repeats,hits))

    # Write to csv file
    output = 'data-'+input
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == '__main__':
    print('Commence data analysis')

    # Reference of ID for each name:
    name_to_id = {
        'Abby Sutherland': 201515011,
        'Alina Lim': 201500584,
        'Andrew': 201499497, # myccn
        'Andrew Mora':201499497, # full name
        'Anna McIntosh': 201508822,
        'Anthony Solis': 201545546,
        'Ashley': 100000000, # dropped
        'Auden': 201498462,
        'Bailey Claudon': 201496159,
        'Daniel Bailey': 201500188,
        'Daniel Hawn': 201494782,
        'Daphne Wingard': 201497072,
        'David Morales': 201497245,
        'David Westermann': 201495199,
        'Duy-hung': 201508575,
        'Elijah Schramek': 201538806,
        'Emily Zell': 201508795,
        'Erin Shelton': 201495412,
        'Garrett Lawson': 201540213,
        'Gie Coulibaly': 201233574,
        'Grace Martinson': 201523037,
        'Hanchi Chen': 101020516,
        'Jacob McDowell': 201510623,
        'Jacob Zoulek': 201503783,
        'James Sharitt': 201494141,
        'Jessica Baker': 201496822,
        'Joey Roman': 201539664,
        'Kashon Tate': 200000000, # dropped
        'Kaylee Ludwig': 201536715,
        'Kenton Weaver': 201507647,
        'Lauren Phillips': 201519429,
        'Luke Sparks': 201515722,
        'Madison Pope': 201544516,
        'Matthew Logan Motley': 201538801,
        'Matthew Murray': 201495622,
        'Michael Dean': 201495825,
        'Michael Pontius': 201513844,
        'Naomi-Lynn Miller': 201495516,
        'Olivia Schmitt': 201538576,
        'Rashun Oliver': 201505281,
        'Sam Hanson': 201534052,
        'samantha obie': 201497686,
        'Samuel Lowery': 201518059,
        'Tea Hickerson': 201541216,
        'William': 201540998, # myccn
        'William Anderson': 201540998, # full name
        'William Quick': 201544933
    }

    # reference of name for each ID
    id_to_name = dict(map(reversed,name_to_id.items())) # from https://therenegadecoder.com/code/how-to-invert-a-dictionary-in-python/


    list_of_files = [
    # q1
        'q1-accel-defn.csv',
        'q1-single-vector-2D.csv',
        'q1-single-vector-polar.csv',
        'q1-vector-addition.csv',
        'q1-vector-subtraction.csv',
        'q1-velocity-defn.csv',
    # q2
        'q2-E-budget.csv',
        'q2-E-cons-defn.csv',
        'q2-E-rot-example.csv',
        'q2-E-spr-ex.csv',
        'q2-I-table.csv',
        'q2-Ug.csv',
        'q2-Usp.csv',
        'q2-down-ramp.csv',
        'q2-krot.csv',
        'q2-ktrans.csv',
        'q2-ugrav-g-defn.csv',
        'q2-up-ramp.csv',
    # q3
        'q3-1Dcoll-ex.csv',
        'q3-2Dcoll-defn.csv',
        'q3-2Dcoll-ex.csv',
        'q3-ball-pend-deriv.csv',
        'q3-p-cons-ex1.csv',
        'q3-p-cons-ex2.csv',
        'q3-p-defn.csv',
        'q3-p-symb-ex.csv',
    # q4
        'q4-3rd-law-ex.csv',
        'q4-elevator-ex.csv',
        'q4-flower-basket-2d-ex.csv',
        'q4-incline-accel-ex.csv',
        'q4-incline-static-ex.csv',
        'q4-potatoes-2d-ex.csv',
        'q4-simple-1d-ex.csv',
        'q4-spring-ex.csv',
    # q5
        'q5-box-stack-compare.csv',
        'q5-box-stack-ex.csv',
        'q5-friction-K-only-ex.csv',
        'q5-friction-ramp-ex.csv',
        'q5-spring-quadratic-ex.csv'
    ]

    for i in range(len(list_of_files)):
        print('Analyzing '+list_of_files[i])
        hits(list_of_files[i])

    print('Done. Have a nice day :)')
