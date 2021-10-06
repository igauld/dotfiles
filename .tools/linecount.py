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

def listDirectory(directory_path):
    try:
        for file in os.listdir(directory_path):
            yield file
    except:
        return

def enumDirectory(directory_path, recurse):
    tot = 0
    totnoempties = 0
    totcomments = 0
    hit = False
    subdirectories = []
        
    #for file in os.listdir(directory_path):
    for file in listDirectory(directory_path):
        if os.path.isdir(file) and recurse:
            subdirectories.append(os.path.join(directory_path, file))
        else:
            ext = file[len(file)-3:]
            if ext == ".py":
                f = open(os.path.join(directory_path, file), mode="r")
                lines = f.readlines()
                linesnoempties, comments = parseLines(lines)
                if hit == False: 
                    print(f"Total\t\tNon-empty\tComments\t{directory_path}")
                    hit = True
                print(f"{len(lines)}\t\t{linesnoempties}\t\t{comments}\t\t{file}")
                f.close()
                tot += len(lines)
                totnoempties += linesnoempties
                totcomments += comments

    if tot > 0:
        print(f"\n{tot}\t\t{totnoempties}\t\t{totcomments}\t\tTOTALS\n")

    for sub in subdirectories:
        subtotal, subnon, subcom = enumDirectory(sub, recurse)
        tot += subtotal
        totnoempties += subnon
        totcomments += subcom

    return tot, totnoempties, totcomments

opts, args = getopt(sys.argv, "r")
recurse = "-r" in args

total, linesnoempties, comments = enumDirectory(os.curdir, recurse)

print(f"{total}\t\t{linesnoempties}\t\t{comments}\t\tGRAND")
