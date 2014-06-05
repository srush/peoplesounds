import glob
import subprocess
import sys

base = sys.argv[1]
for f in glob.glob(base + "/*/*.mp3"):
    subprocess.call(["lame", "--decode", f])
