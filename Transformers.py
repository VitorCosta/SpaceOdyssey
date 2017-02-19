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
Hcte = 285.93
Bcte = 0.8705483323911815
fourrier = []


# reading the channels and access the string item, get the first element and append to an array
def DocumentRead(x):
    data = pd.read_csv(x)
    return data





#plot the read current and voltage
def PlotCurrentVoltage():
    fig = plt.figure()

    axes1 = fig.add_axes([0.1,0.1,0.5,0.5])
    axes2 = fig.add_axes([0.88,0.1,0.5,0.5])
    axes1.plot(time,current,color = 'red',label='Current')
    axes1.set_title('Time versus Current')
    axes1.set_ylabel('Amplitude')
    axes1.set_xlabel('Time')
    axes1.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
    axes2.plot(time,voltage,color = 'black',label='Voltage')
    axes1.legend(loc=0)
    axes2.set_xlabel('Time')
    axes2.set_ylabel('Amplitude')
    axes2.grid(color='b',alpha=0.5,linestyle='dashed',lw=0.5)
    axes2.set_title('Voltage versus Time')
    axes2.legend(loc=0)
    CurrentRms = np.sqrt(np.mean(np.square(current)))
    VoltageRms = np.sqrt(np.mean(np.square(voltage)))
    print('The Rms Current is: {}'.format(CurrentRms))
    print('The Rms Voltage is: {}'.format(VoltageRms))
    plt.show(fig)

#lot the potency graphic
def PlotPotency():
    Pot = voltage * current
    fig = plt.figure()
    axes = fig.add_axes([0,0,2.0,1])
    axes.plot(time,Pot,'purple')
    axes.set_xlabel('Time')
    axes.set_ylabel('Potency[W]')
    axes.set_title('Pot versus Time')
    axes.grid()
    Med = float(np.absolute(np.mean(Pot)))/2
    Rms = float(np.sqrt(np.mean(np.square(Pot))))/2
    print('The Med Value is: {}'.format(Med))
    print('The Rms Value is: {}'.format(Rms))
    plt.show()


#Plot the magnetization curve
def PlotCamps():
    fig = plt.figure()
    axes = fig.add_axes([0,0,1,1])
    axes.plot(Hcamp,Bcamp,'grey')
    plt.xlabel('A/M')
    plt.ylabel('Tesla')
    plt.title('HxB')
    plt.grid()
    plt.show()
    Energy = np.trapz(Bcamp,Hcamp,dx=0.1,axis=0)
    print('The Energy Value is: {}'.format(abs(Energy)))
    #vol=0.000142738;
    vol = 0.0018559999999999996
    Pfe = abs(Energy) * vol * 60
    print('The Potency Value is: {}'.format(abs(Pfe)))

def Fft():
    sample = current
    L = len(sample)
    print(L)
    Y = scipy.fftpack.fft(sample)/L
    xdft = Y[0:L/2+1]
    print(len(xdft))
    freq = np.linspace(0,L/2,L/2+1)
    print(len(freq))
    ampl_fft = 2 * np.absolute(xdft)
    FFTfigure = plt.figure()
    axes = FFTfigure.add_axes([0,0,2.0,1.0])
    plt.bar(freq,ampl_fft)
    plt.axis([0,50,0,1.5])
    axes.set_xticks(np.arange(0,51,1))
    plt.grid()
    plt.show()
    x = 0
    while x<=10:
        print('Fft amplitude:{} - {}'.format(x,ampl_fft[x]))
        x = x + 1
    x  = 2
    somv = 0
    while x<=50:
        somv = somv + (np.absolute(ampl_fft[x]**2))
        x = x + 1
    THD = 100 * np.sqrt(somv)/(np.absolute(ampl_fft[1]))
    print('THD: {} '.format(THD))



#main Program


h = 210
df = DocumentRead('TEK.csv')
time = df['TIME'][:h]
current = df['CH1'][:h]
voltage = df['CH3'][:h] * 4
Hcamp = df['CH1'][:h] * Hcte
Bcamp = df['CH2'][:h] * Bcte

Fft()
PlotCurrentVoltage()
PlotPotency()
PlotCamps()
