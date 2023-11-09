#after use this code you will find between two line
# a blancket line with this code u will sort out the prob
fhand =open ("read_file.2.py")
for line in fhand:
    line = line.rstrip()
    if line.startswith("x"):
        print(line)