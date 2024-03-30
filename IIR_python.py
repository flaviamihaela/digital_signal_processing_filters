#IIR Filter
import matplotlib.pyplot as plt
from numba import njit
import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import numba as nb

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

def to_fixed(f):
    a = f* (2**14)
    b = int(round(a))
    if a < 0:
        # next three lines turns b into it's 2's complement.
        b = abs(b)
        b = ~b
        b = b + 1
    return b

def is_float(n):
    try:
        float(n)
        return True
    except:
        return False
#Implement IIR filter

def iir_filter(Sound,zeros_real,zeros_imaginary,poles_real, poles_imaginary):
    N1=len(Sound)
    y=np.zeros(N1)
    x=Sound.copy()
    num=1
    for m in range(2):
        a0=zeros_real[m]
        b0=zeros_imaginary[m]
        a1=poles_real[m]
        b1=poles_imaginary[m]
        e0=(a0*a0+b0*b0)
        e1=(a1*a1+b1*b1)
        coef1=1
        coef2=((-2)*a0)
        coef3=e0
        coef4=(-2)*a1
        coef5=e1
        for n in range(2,N1):
            y[n]=(coef1*x[n]+coef2*x[n-1]+coef3*x[n-2]-coef4*y[n-1]-coef5*y[n-2])
            print(y[n])
        for n in range(N1):
            x[n]=y[n]
    return y

#fs, unfil_sig_int16= wavfile.read("new.wav")
#plt.plot(unfil_sig_int16)


#Read WAV file and store header and audio into different arrays
binarySound = {}
binaryHeader = {}
song = {}

with open("test2.wav",'rb') as f:
        buffer = f.read(44)
        Header = np.frombuffer(buffer,dtype=np.int16)
        buffer = f.read()
        Sound = np.frombuffer(buffer,dtype=np.int16)
  
    
#Read poles and zeros from file and store into array as 'float64'
with open("IIR1", 'rb') as f:
        lines = f.readlines()
        numbers = [float(n) for n in lines if is_float(n)]
        zeros_real = np.array(numbers[0:4])
        zeros_imaginary = np.array(numbers[4:8])
        poles_real = np.array(numbers[8:12])
        poles_imaginary = np.array(numbers[12:16])


#Filter sound with IIR filter
maxi=np.max(abs(Sound))
Sound=Sound/maxi
filtered_sound=iir_filter(Sound, zeros_real, zeros_imaginary, poles_real, poles_imaginary)
filtered_sound=np.asarray(filtered_sound, dtype=np.int16)

#Write to new file
with open("header.bin","wb") as f:
        f.write(Header)

with open("data.bin","wb") as f:
        f.write(filtered_sound)

with open("header.bin","rb") as h:
        song = h.read()
        with open("data.bin","rb") as d:
                song += d.read()

with open("new_IIR.wav","wb") as f:
        song = np.array(song)
        f.write(song.tobytes())
