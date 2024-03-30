#FIR Filter
import matplotlib.pyplot as plt
from numba import njit
import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import numba as nb

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


'''
#Implement FIR filter

def fir_filter2(padded, impulse_response_rev):
    result=np.zeros(len(padded)-len(impulse_response_rev)+1)
    num=1
    for i in range(len(padded)-len(impulse_response_rev)+1):
        result[i]=np.dot(impulse_response_rev, padded[i:i+len(impulse_response_rev)])
        print(num)
        num+=1
    return result

#fs, unfil_sig_int16= wavfile.read("new.wav")
#plt.plot(unfil_sig_int16)

binarySound = {}
binaryHeader = {}
song = {}

#Read WAV file and store header and audio into different arrays
with open("test1.wav",'rb') as f:
        buffer = f.read(44)
        Header = np.frombuffer(buffer,dtype=np.int16)
        buffer = f.read()
        Sound = np.frombuffer(buffer,dtype=np.int16)
  
#Read coefficients from file and store into array as 'double'
with open("FIR1", 'rb') as f:
        n=f.readlines()
        impulse_response=np.array(n, dtype=np.float64)
        

L=len(impulse_response)-1
vector=np.zeros(L).astype(np.int16)
padded=np.concatenate((Sound,vector))
N=len(padded)
impulse_response_rev=np.flip(impulse_response)
filtered_sound=fir_filter2(padded, impulse_response)


filtered_sound=np.asarray(filtered_sound, dtype=np.int16)

with open("header.bin","wb") as f:
        f.write(Header)

with open("data.bin","wb") as f:
        f.write(filtered_sound)

with open("header.bin","rb") as h:
        song = h.read()
        with open("data.bin","rb") as d:
                song += d.read()

with open("new.wav","wb") as f:
        song = np.array(song)
        f.write(song.tobytes())
        '''

def fir_filter2(padded, impulse_response_rev):
    result=np.zeros(len(padded)-len(impulse_response_rev)+1)
    num=1
    for i in range(len(padded)-len(impulse_response_rev)+1):
        result[i]=np.dot(impulse_response_rev, padded[i:i+len(impulse_response_rev)])
        print(num)
        num+=1
    return result

window = Tk()

window.title("FIR")

window.geometry('350x200')

flag = 0

def openwav():
    binarySound = {}
    binaryHeader = {}
    song = {}
    global flag
    global Sound
    global Header
    filename = askopenfilename()
    with open(filename,'rb') as f:
        buffer = f.read(44)
        Header = np.frombuffer(buffer,dtype=np.int16)
        buffer = f.read()
        Sound = np.frombuffer(buffer,dtype=np.int16)
        flag = 1
      
def import_coef():
    filename = askopenfilename()
    with open(filename, 'rb') as f:
        n=f.readlines()
        global impulse_response
        impulse_response=np.array(n, dtype=np.float64)
        flag = 2
def filterwav():
    global flag
    global Sound
    global impulse_response
    if flag == 0:
        messagebox.showinfo("Error!", "Import necessary files first")
    else:
        L=len(impulse_response)-1
        vector=np.zeros(L).astype(np.int16)
        padded=np.concatenate((Sound,vector))
        N=len(padded)
        impulse_response_rev=np.flip(impulse_response)
        global filtered_sound
        filtered_sound=fir_filter2(padded, impulse_response)
    
        filtered_sound=np.asarray(filtered_sound, dtype=np.int16)
        flag = 3
    

        
def savewav():
    global flag
    if flag == 3:
        global filtered_sound
        global Header
        with open("header.bin","wb") as f:
            f.write(Header)
    
        with open("data.bin","wb") as f:
                f.write(filtered_sound)
        
        with open("header.bin","rb") as h:
                song = h.read()
                with open("data.bin","rb") as d:
                        song += d.read()
        
        with open("new.wav","wb") as f:
                song = np.array(song)
                f.write(song.tobytes())
    else:
        messagebox.showinfo("Error!", "File not filtered")

btn_openwav = Button(window, text="OPEN WAV FILE", command=openwav, height = 5, width = 24)

btn_openwav.grid(column=1, row=0)

btn_filterwav = Button(window, text="FILTER WAV FILE", command=filterwav, height = 5, width = 24)

btn_filterwav.grid(column=1, row=1)

btn_import_coef = Button(window, text="IMPORT FIR COEFFICIENTS", command=import_coef, height = 5, width = 24)

btn_import_coef.grid(column=2, row=0)

btn_savewav = Button(window, text="SAVE FILTERED WAV FILE", command=savewav, height = 5, width = 24)

btn_savewav.grid(column=2, row=1)



window.mainloop()


        
