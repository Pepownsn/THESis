# OS Module (Miscellaneous operating system)
import os
import time
curDir = os.getcwd()  ##find address floder
print(curDir)
os.mkdir('newfloder1')  ## create floder
time.sleep(2)

os.rename('newfloder1','new2')  # rename floder
time.sleep(2)
os.rmdir('new2')     # remove floder
os.rmdir('newfloder')
