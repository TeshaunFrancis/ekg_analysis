# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:03:59 2022

@author: ninja
"""

#EKG Example
#Teshaun Francis
#Python3 Solution
import numpy
from matplotlib import pyplot
from pathlib import Path
from scipy.signal import find_peaks
 
def ekg1():
    filelocation = input("where is the folder? ex. datafolder : ")
    path_to_filelocation = Path(filelocation)
    raw_file = input("what is the file? ex. data.txt :")
    path_to_file = path_to_filelocation / raw_file
    ekgdata = numpy.loadtxt(path_to_file)
    return ekgdata
 
def ekg2(inputvar):
    return numpy.size(inputvar)
 
def ekg3(inputvar):
    samplingRate = 125 #samples/sec
    numberOfSamples = ekg2(inputvar)
    time = numberOfSamples / samplingRate
    X = numpy.linspace(0,time,numberOfSamples)
    Y = inputvar
    fig, axe = pyplot.subplots()
    axe.plot(X,Y)
    usertitle = input('What is the title? : ')
    axe.set(xlabel='time (s)', ylabel='Amplitude (au)', title=usertitle)
    axe.grid()
    figname = input('Whats the filename? ex. bob.png : ')
    fig.savefig(figname)
    pyplot.show()
 
def ekg4(inputvar):
    samplingRate = 125 #samples/sec
    numberOfSamples = ekg2(inputvar)
    time = numberOfSamples / samplingRate
    X = numpy.linspace(0,time,numberOfSamples)
    Y = inputvar
    fig, axe = pyplot.subplots()
    axe.plot(X,Y)
    r_peaks, _ = find_peaks(inputvar, height=1.5*numpy.mean(inputvar))
    qs_peaks, _ = find_peaks(-inputvar, height=-80)
    q_peaks = qs_peaks[0::2]
    s_peaks = qs_peaks[1::2]
    pyplot.plot(q_peaks/samplingRate, inputvar[q_peaks], "rx")
    pyplot.plot(r_peaks/samplingRate, inputvar[r_peaks], "gx")
    pyplot.plot(s_peaks/samplingRate, inputvar[s_peaks], "bx")
    axe.legend(['EKG','Q','R','S'])
    usertitle = input('What is the title? : ')
    axe.set(xlabel='time (s)', ylabel='Amplitude (au)', title=usertitle)
    axe.grid()
    figname = input('Whats the filename? ex. bob.png : ')
    fig.savefig(figname)
    pyplot.show()
 
def ekg5(inputvar):
    samplingRate = 125 #samples/sec
    numberOfSamples = ekg2(inputvar)
    time = numberOfSamples / samplingRate
    X = numpy.linspace(0,time,numberOfSamples)
    Y = inputvar
    fig, axe = pyplot.subplots()
    axe.plot(X,Y)
    peaks, _ = find_peaks(inputvar, height=1.5*numpy.mean(inputvar))
    pyplot.plot(peaks/samplingRate, inputvar[peaks], "x")
    usertitle = input('What is the title? : ')
    axe.set(xlabel='time (s)', ylabel='Amplitude (au)', title=usertitle)
    axe.grid()
    figname = input('Whats the filename? ex. bob.png : ')
    fig.savefig(figname)
    pyplot.show()
    
def ekg6(inputvar):
    samplingRate = 125 #samples/sec
    peaks, _ = find_peaks(inputvar, height=1.5*numpy.mean(inputvar))
    return numpy.subtract(peaks[1:numpy.size(peaks)],peaks[0:numpy.size(peaks)-1])
 
def ekg7(inputvar):
    RR = ekg6(inputvar)
    return numpy.mean(RR)
