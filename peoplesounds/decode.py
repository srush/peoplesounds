import glob
import sys,os
base = sys.argv[1]
for f in glob.glob(base + "/*/*/*.mp3"):
  os.system("lame --decode '%s'"%f)
