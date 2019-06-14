import glob
import os

lst = glob.glob("./img/*")
for l in lst:
    if len(l) > 18:
        os.remove(l)
        print("deleted" + l)
