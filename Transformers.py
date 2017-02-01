#Caracterizing Transformers Program


#importing the matemathical library
import math
import matplotlib.pyplot as plt

filename = 'file-800.txt'
time = []
current = []
voltage = []
#opening the data files
with open(filename) as f:
    data = f.readlines()

# reading the channels
for n,line in enumerate(data, 1):
    print ('{:2}.'.format(n), line.rstrip())
    parts = line.split(',')
    time.append(parts[:1])
    current.append(parts[1:2])
    voltage.append(parts[2:3])
print(time)
print(current)
print(voltage)

# printing the graphics
plt.plot(time,current)
plt.show()
