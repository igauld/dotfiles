import os
import sys
from getopt import getopt

def parseLines(lines):
    count = 0
    comments = 0
    defines = 0
    imports = 0

    for line in lines:
        # non-empty only
        if len(line) > 1:
            count += 1
            if line.strip().startswith("#"):
                comments += 1
            """
            if line.strip().startswith("def"):
                defines += 1
            if line.strip().startswith("import") or line.strip("from"):
                imports += 1
            """

    return count, comments

def enumDirectory(directory_path, recursion):
    tot = 0
    totnoempties = 0
    totcomments = 0
    hit = False
    subdirectories = []

    for file in os.listdir(directory_path):
        if os.path.isdir(file) and recursion:
            #enumDirectory(file, recursion)
            subdirectories.append(os.path.join(directory_path, file))
        else:
            ext = file[len(file)-3:]
            if ext == ".py":
                f = open(os.path.join(directory_path, file), mode="r")
                lines = f.readlines()
                linesnoempties, comments = parseLines(lines)
                if hit == False: 
                    print(f"\nDirectory: {directory_path}")
                    hit = True
                print(f"{len(lines)}\t\t{linesnoempties}\t\t{comments}\t\t{file}")
                f.close()

                tot += len(lines)
                totnoempties += linesnoempties
                totcomments += comments
    if tot > 0:
        print(f"\n{tot}\t\t{totnoempties}\t\t{totcomments}\t\tTOTALS")

    for sub in subdirectories:
        subtotal, subnon, subcom = enumDirectory(sub, recursion)
        tot += subtotal
        totnoempties += subnon
        totcomments += subcom


    return tot, totnoempties, totcomments

total = 0
totalnonempty = 0
totalcomments = 0

opts, args = getopt(sys.argv, "r")
recursion = "-r" in args

print("Total\t\tNon-empty\tComments\tFilename")

total_, linesnoempties, comments = enumDirectory(os.curdir, recursion)

total += total_
totalnonempty += linesnoempties
totalcomments += comments

print(f"\n{total}\t\t{totalnonempty}\t\t{totalcomments}\t\tGRAND")
