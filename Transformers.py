#Caracterizing Transformers Program


#importing the matemathical library
import math
import matplotlib.pyplot as plt
from numpy import mean, sqrt, square, arange


# Write the name of the file5
filename = 'file-800.txt'



time = []
current = []
voltage = []
Hcamp = []
Bcamp = []
Pot = []
Hcte = 355.8676647
Bcte = 0.501564416


# reading the channels and access the string item, get the first element and append to an array
def DocumentRead():
    for n,line in enumerate(data, 1):
        #print ('{:2}.'.format(n), line.rstrip())
        parts = line.split(',')
        time.append(parts[:1][0])
        current.append(float(parts[1:2][0]))
        voltage.append(float(parts[2:3][0]))
        Hcamp.append(float(parts[1:2][0]) * Hcte)
        Bcamp.append(float(parts[2:3][0]) * Bcte)


#plot the read current and voltage
def PlotCurrentVoltage():
    plt.plot(time,current, label='Current')
    plt.plot(time,voltage, label='Voltage')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Timex.current.voltage')
    plt.grid()
    plt.legend()
    plt.show()

#Plot the potency graphic
def PlotPotency():
    Pot = [current*voltage for current,voltage in zip(current,voltage)]
    plt.plot(time,Pot)
    plt.xlabel('time')
    plt.ylabel('Amplitude[W]')
    plt.title('PotxTime')
    Med = float(sum(Pot)/len(Pot))
    Rms = float(sqrt(mean(square(Pot))))
    plt.show()
    print(Med)
    print(Rms)


#Plot the magnetization curve
def PlotCamps():
    plt.plot(Hcamp,Bcamp)
    plt.xlabel('A/M')
    plt.ylabel('Tesla')
    plt.title('HxB')
    plt.show()

#opening the data files
with open(filename) as f:
    data = f.readlines()

#main Program

DocumentRead()
PlotCurrentVoltage()
PlotPotency()
PlotCamps()
