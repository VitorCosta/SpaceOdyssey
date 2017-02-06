#Caracterizing Transformers Program


#importing the matemathical library
import math
import matplotlib.pyplot as plt
from numpy import mean, sqrt, square, arange, size
import numpy as np
import scipy.fftpack


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
fourrier = []


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
    plt.grid()
    Med = float(sum(Pot)/len(Pot))
    Rms = float(sqrt(mean(square(Pot))))
    plt.show()
    print("Med Value:  " , Med)
    print("Rms Value:  " , Rms)


#Plot the magnetization curve
def PlotCamps():
    plt.plot(Hcamp,Bcamp)
    plt.xlabel('A/M')
    plt.ylabel('Tesla')
    plt.title('HxB')
    plt.grid()
    plt.show()

def Fft():
    sample = current
    L = len(sample)
    print(L)
    Y = scipy.fftpack.fft(sample)/L
    u = L/2
    #print(Y)
    xdft = Y[0:251]
    print(len(xdft))
    freq = np.linspace(0,L/2+1,L/2+1)
    print(len(freq))
    ampl_fft = 2 * np.absolute(xdft)
    #print (ampl_fft)
    plt.bar(freq,ampl_fft)
    plt.grid()
    plt.show()



#main Program

#opening the data files
with open(filename) as f:
    data = f.readlines()

DocumentRead()
Fft()
#PlotCurrentVoltage()
#PlotPotency()
#PlotCamps()
