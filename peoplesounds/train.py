import glob
import scikits.audiolab as audiolab
import os
import random
import sys

size = 44100 * 2
outfile = open(sys.argv[2], "a")


def play_rand(file, name):
    sound = audiolab.sndfile(file)
    limit = sound.get_nframes()
    frames = sound.read_frames(sound.get_nframes()) * 0.8
    if limit < size: return
    for i in range(5):
        start = random.randint(0, limit - size)
        print("Is this a voice? [(y)es, (n)o, " +
            "(s)kip/significant-portions-of-both/can't-tell, (r)eplay]")
        audiolab.play(frames[start: start + size][:,0])
        while True:
            input = raw_input()
            if input == "r":
                audiolab.play(frames[start: start + size][:,0])
            elif input in ["y", "n", "s"]:
                break
        print >> outfile, name, start, start + size, input

def main(base):
    s = [f for f in glob.glob(os.path.join(base, "*/*/*.wav"))]
    while True:
        f = random.sample(s, 1)
        play_rand(f[0], f[0][len(base):])


if __name__ == "__main__":
    main(sys.argv[1])
