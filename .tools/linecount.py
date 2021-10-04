import os

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
            if line.strip().startswith("def"):
                defines += 1
            if line.strip().startswith("import") or line.strip("from"):
                imports += 1

    return count, comments

total = 0
totalnonempty = 0
totalcomments = 0

for file in os.listdir():
    
    ext = file[len(file)-3:]
    if ext == ".py":
        f = open(file, mode="r")
        lines = f.readlines()
        linesnoempties, comments = parseLines(lines)
        
        total += len(lines)
        totalnonempty += linesnoempties
        totalcomments += comments
        print(f"{len(lines)}\t\t\t{linesnoempties}\t\t\t{comments}\t\t{file}")

print(f"Total lines: {total} non-empty: {totalnonempty} comments: {totalcomments}")