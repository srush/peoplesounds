import glob
import scikits.audiolab as audiolab
import random
import sys

size = 44100 * 2
outfile = open(sys.argv[2], "a")


def play_rand(file, name):
  sound = audiolab.sndfile(file)
  limit = sound.get_nframes()
  frames = sound.read_frames(sound.get_nframes())  
  if limit < size: return
  for i in range(5):
    start = random.randint(0, limit - size)
    print "Is this a voice? [y, n, s]"
    audiolab.play(frames[start: start + size][:,0])
    while True:
      input = raw_input()
      if input in ["y", "n", "s"]: break
    print >> outfile, name, start, start + size, input

def main(base):
  s = [f for f in glob.glob(base + "*/*/*.wav")]
  while True:
    f = random.sample(s, 1)
    #print f
    play_rand(f[0], f[0][len(base):])


if __name__ == "__main__":
  main(sys.argv[1])
