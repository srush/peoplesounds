#!/usr/bin/env python
import sys
from scipy import *
from pylab import *
from numpy import *
import scikits.audiolab as audiolab
import struct

def show_specgram(speech):
    sound = audiolab.sndfile(speech, 'read')
    sound_info = sound.read_frames(sound.get_nframes())
    spectrogram = specgram(sound_info)
    title('Spectrogram of %s'%sys.argv[1])
    show()
    sound.close()
    return spectrogram

file = sys.argv[1]
show_specgram(file)
