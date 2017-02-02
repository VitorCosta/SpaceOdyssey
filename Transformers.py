#Caracterizing Transformers Program


#importing the matemathical library
import math
import matplotlib.pyplot as plt
import numpy as np

# Write the name of the file
filename = 'file-800.txt'


Hcte = 355.8676647
Bcte = 0.501564416

time = []
current = []
voltage = []
Hcamp = []
Bcamp = []


# reading the channels
def DocumentRead():
    for n,line in enumerate(data, 1):
    #    print ('{:2}.'.format(n), line.rstrip())
        parts = line.split(',')
        time.append(parts[:1])
        current.append(parts[1:2])
        voltage.append(parts[2:3])


#opening the data files
with open(filename) as f:
    data = f.readlines()

#main Program

DocumentRead()


Hcamp= np.array(current)
Bcamp = np.array(voltage)

print(Hcamp)
print(type(Hcamp))

# printing the graphics
plt.plot(Hcamp,Bcamp)
plt.show()
