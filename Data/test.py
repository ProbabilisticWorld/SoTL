from datetime import datetime
import numpy as np
#import matplotlib.pyplt as plt

# Load text, slice by name and time
names = np.genfromtxt('SingleVector2D.csv',dtype=str,delimiter=',',skip_header=2,encoding=None,usecols=(0))

str2date = lambda x: datetime.strptime(x.decode("utf-8"), '%Y-%m-%d %H:%M:%S')
times = np.genfromtxt('SingleVector2D.csv',dtype=None,delimiter=',',skip_header=2,encoding=None,usecols=(1),converters = {0: str2date})

print(names)
print(times)
