#!/usr/bin/env python
import sys
from scipy import *
from pylab import *
from numpy import *
import scikits.audiolab as audiolab
import struct

def show_Specgram(speech):
    '''
    Reads .wav file from STDIN and plots the spectrogram
    '''
    sound = audiolab.sndfile(speech,'read')
    # Reads wav file with audiolab
    sound_info = sound.read_frames(sound.get_nframes())
    # Extracts feature info from sound file with scipy module
    spectrogram = specgram(sound_info)
    #Generates soectrogram with matplotlib specgram
    title('Spectrogram of %s'%sys.argv[1])
    show()
    sound.close()
    return spectrogram

file = sys.argv[1]
show_Specgram(file)
