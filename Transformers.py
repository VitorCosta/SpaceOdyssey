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
        parts = line.split(',')

        # Access the string item, get the first element and append to an array
        time.append(parts[:1][0])
        current.append(float(parts[1:2][0]) * Hcte)
        voltage.append(float(parts[2:3][0]) * Bcte)

def Plotcurrentvoltage():
    plt.plot(time,current, label='Current')
    plt.plot(time,voltage, label='Voltage')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Timex.current.voltage')
    plt.grid()
    plt.legend()
    plt.show()


#opening the data files
with open(filename) as f:
    data = f.readlines()

#main Program

DocumentRead()
Plotcurrentvoltage()

Hcamp= np.array(current)
Bcamp = np.array(voltage)

print(Hcamp)
print(type(Hcamp))

# printing the graphics
#plt.plot(Hcamp,Bcamp)
#plt.show()
