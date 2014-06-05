#!/usr/bin/env python
import sys
import pylab as plt
import scikits.audiolab as audiolab
import scikits.talkbox.features as talkfeat
import struct

def show_specgram(speech):
    sound = audiolab.sndfile(speech, 'read')
    sound_info = sound.read_frames(sound.get_nframes())

    #spectrogram = plt.specgram(sound_info)
    mfcc = talkfeat.mfcc(sound_info)

    #print mfcc
    plt.imshow(mfcc[0].transpose())
    plt.title('Spectrogram of %s' % sys.argv[1])
    plt.show()
    sound.close()

file = sys.argv[1]
show_specgram(file)
