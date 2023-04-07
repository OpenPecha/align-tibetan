import sys
import pyewts


converter = pyewts.pyewts()
path = sys.argv[1]
result = ""

for line in open(path, "r"):
    line = converter.toWylie(line)
    result += line


with open(path,"w") as outfile:
    outfile.write(result)

    
