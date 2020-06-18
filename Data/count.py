import datetime as dt
import numpy as np
import csv

# Load text, slice by name and time
(names,times0) = (np.genfromtxt('VectorAddition.csv',dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(0)),
                  np.genfromtxt('VectorAddition.csv',dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(1)))

# Make array to put dates into, in dateimte format
times = np.empty(len(times0),dtype=object)

# Convert dates to datetime format, populate times array
i = 0
for i in range(len(times)):
    times[i] = dt.datetime.strptime(times0[i],'%Y-%m-%d %H:%M:%S')


# Compare times: flag hits from a given student that are separated by less than 60 s
# Make new arrays for flagged data
names_flagged = np.empty_like(names)
np.copyto(names_flagged,names)
times_flagged = np.empty_like(times)
np.copyto(times_flagged,times)
i = 1 # start at 1 so I can compare to item 0
for i in range(len(times)):
    if i == 0:
        i = 1 # start at 1 so I can compare to item 0
    elif names[i] == names[i-1]:
        if times[i] <= times[i-1] + dt.timedelta(seconds=60):
            names_flagged[i] = 0 # Flag name as 0
            times_flagged[i] = 0 # Flag time as 0

# Removed flagged entries from above
indices = [] # This will be used in the np.delete() function
# i = 0
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
#i = 1 # start at 1 so I can compare to item 0
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
with open("data-VectorAddition.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
