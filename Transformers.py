#Caracterizing Transformers Program


#importing the matemathical library
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import pandas as pd


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
def DocumentRead(x):
    data = pd.read_csv(x)
    return data





#plot the read current and voltage
def PlotCurrentVoltage():
    GraphCV = plt.figure()
    axes = GraphCV.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(time,current,color = 'red',label='Current')
    axes.plot(time,voltage,color = 'black',label='Voltage')
    axes.set_title('Time versus Current and Voltage')
    axes.set_xlabel('Amplitude')
    axes.set_ylabel('Time')
    axes.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
    axes.legend(loc=(1.01,1.01))
    CurrentRms = np.sqrt(np.mean(np.square(current)))
    VoltageRms = np.sqrt(np.mean(np.square(voltage)))
    print('The Rms Current is: {}'.format(CurrentRms))
    print('The Rms Voltage is: {}'.format(VoltageRms))
    plt.show(GraphCV)

#lot the potency graphic
def PlotPotency():
    Pot = voltage * current
    plt.plot(time,Pot)
    plt.xlabel('time')
    plt.ylabel('Amplitude[W]')
    plt.title('PotxTime')
    plt.grid()
    Med = float(np.sum(Pot)/len(Pot))
    Rms = float(np.sqrt(np.mean(np.square(Pot))))
    print('The Med Value is: {}'.format(Med))
    print('The Rms Value is: {}'.format(Rms))
    plt.show()


#Plot the magnetization curve
def PlotCamps():
    plt.plot(Hcamp,Bcamp)
    plt.xlabel('A/M')
    plt.ylabel('Tesla')
    plt.title('HxB')
    plt.grid()
    plt.show()
    Energy = np.trapz(Bcamp,Hcamp,dx=0.01,axis=0)
    print('The Energy Value is: {}'.format(abs(Energy)))
    vol=0.000142738;
    Pfe = abs(Energy) * vol * 60
    print('The Potency Value is: {}'.format(abs(Pfe)))

def Fft():
    sample = current
    L = len(sample)
    print(L)
    Y = scipy.fftpack.fft(sample)/L
    #print(Y)
    xdft = Y[0:L/2+1]
    print(len(xdft))
    freq = np.linspace(0,L/2,L/2+1)
    print(len(freq))
    ampl_fft = 2 * np.absolute(xdft)
    #print (ampl_fft)
    plt.bar(freq,ampl_fft)
    plt.axis([0,50,0,1.5])
    plt.grid()
    plt.show()
    print(freq)



#main Program


df = DocumentRead('60Hz800.csv')

time = df['TIME']
current = df['CH1']
voltage = df['CH2']
Hcamp = df['CH1'] * Hcte
Bcamp = df['CH2'] * Bcte

#Fft()
PlotCurrentVoltage()
PlotPotency()
PlotCamps()
