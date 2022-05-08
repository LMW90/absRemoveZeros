#! python3
# program removes preceding zeros in numbered files ie. 'foo0042.txt' into 'foo42.txt'

import re
import os
import shutil
# compile regex
zeroesRE = re.compile(r'''
                    ^(.*?) # part of name preceding zeroes
                    ([0]+)      # part matches all zeroes
                    (.*)$       # part matches all remaining chars
                    ''', re.VERBOSE)

# loop through files in cwd
for file in os.listdir('.'):
    mo = zeroesRE.search(file)
    # skip filenames not matching regex
    if mo == None or mo.group(2) == None:
        continue
    prePart = mo.group(1)
    sucPart = mo.group(3)
    newName = prePart + sucPart
    print(newName)
    absCWD = os.path.abspath('.')
    oldFilePath = os.path.join(absCWD, file)
    newFilePath = os.path.join(absCWD, newName)
    print(f'Converting <{oldFilePath}> into <{newFilePath}>.')
    # shutil.move(oldFilePath, newFilePath)