import scikits.audiolab as audiolab
import scikits.talkbox.features as features
import scikits.talkbox as talkbox
import pylab as plt

class LabeledData:
    def __init__(self, file, start, stop, label):
      self.file = file
      self.start = int(start)
      self.stop = int(stop)
      self.label = label

    @staticmethod
    def from_handle(handle):
      for l in handle:
        yield LabeledData(*([" ".join(l.split(" ")[:-3])] + l.split(" ")[-3:]))


class SoundManager:
  def __init__(self, base):
    self.base = base

  def play(self, example):
    sound = audiolab.sndfile(self.base + example.file)
    frames = sound.read_frames(sound.get_nframes()) * 0.8
    
    audiolab.play(frames[example.start: example.stop][:,0])
        

  def show(self, example):
    sound = audiolab.sndfile(self.base + example.file)
    frames = sound.read_frames(sound.get_nframes()) * 0.8
    mfcc = features.mfcc(frames[example.start: example.stop:2], fs=41000)
    print mfcc[0].shape
    fig = plt.figure()
    fig.set_size_inches(20, 20)
    ax = fig.add_subplot(111)
    ax.imshow(mfcc[0].transpose()[:, :100])
    
  def vectors(self, example):
    mfcc = features.mfcc(frames[example.start: example.stop:2], fs=41000)
    return mfcc[0]
    
if __name__ == "__main__":
  examples = LabeledData.from_handle(open("/home/srush/Projects/peoplesounds/data/run2.txt"))
  manager = SoundManager("/home/dancor/")
  for example in examples:
    
    print example
    manager.play(example)
