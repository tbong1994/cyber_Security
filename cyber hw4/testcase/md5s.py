import sys, hashlib
infile = open(sys.argv[1], 'r')
ofile = open('Q4in.txt', 'w')

m = hashlib.md5()

for line in infile:
    m = hashlib.md5()
    m.update(line.strip())
    print>>ofile, m.hexdigest()
