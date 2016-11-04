import sys, math, io, hashlib
import time

infile = open(sys.argv[1], 'r')


def Q1A(ifile):
    ofile = open('Q1A.txt', 'wr')
    dic = {}
    output = {}
    cnt = 0
    for line in ifile:
        cnt = cnt + 1
        line = line.rstrip()
        if line in dic:
            dic[line] = dic[line] + 1
        else:
            dic[line] = 1
    for key in sorted(dic.keys()):
        print>>ofile, key+"\t"+str(dic[key])+"\t"+str(round((float(dic[key]))/cnt, 10))
        output[key] = [dic[key], round(float(dic[key])/cnt, 10)]
    ofile.flush()
    ofile.close()
    return output

def Q1B(dic):
    ofile = open('Q1B.txt', 'w')
    d = {}
    chars = 0
    for word in dic:
        for ch in word:
            if ch.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                chars = chars + 1
        #chars = chars + len(word)
        for ch in word.rstrip().upper():
            if ch in d:
                d[ch] = d[ch] +1
            else:
                d[ch] = 1
    dx = {}
    for ch in sorted(d.keys()):
        ch = ch.upper()
        if ch in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            dx[d[ch]] = ch
    for freq in sorted(dx.keys(),reverse=True):
        print>>ofile, dx[freq]+"\t"+str(freq)+"\t"+str(round(float(freq)/chars*100,2))

def Q2A(dic):
    ofile = open('Q2A.txt','w')
    ent = 0.0
    for word in dic:
        ent = ent + float(dic[word][1] * math.log(dic[word][1],2))
    ent = -1.0*round(ent,3)
    print>>ofile, ent

def Q2B(dic):
    ofile = open('Q2B.txt', 'w')
    total = 0
    for word in dic:
        total = total+dic[word][0]
    print>>ofile, round(math.log(total,2),3)

def Q3A(dic):
    ofile = open('Q3A.txt', 'w')
    words = {}
    ent = 0.0
    for word in dic:
        words[word] = round(float(1)/len(dic), 10)
    for word in words:
        p = words[word]
        ent = float(ent) + float(p * math.log(p, 2))
    ent = round(-1.0*ent,3)
    print>>ofile, round(ent,3)

def Q3B(dic):
    ofile = open('Q3B.txt', 'w')
    print>> ofile, round(math.log(len(dic), 2), 3)

def Q4(dic):
    ofile = open('Q4.txt','w')
    ifile = open('Q4in.txt','r')
    #prepare the dictionary for search:
    newdic = {}
    dicX = {}
    index = 0
    for word in dic:
        freq = dic[word][0]
        if freq in newdic:
            newdic[freq].append(word)
        else:
            newdic[freq] = []
            newdic[freq].append(word)
    for freq in sorted(newdic.keys(), reverse=True):
        for word in sorted(newdic[freq]):
            index = index + 1
            dicX[index] = word
    
    #m = hashlib.md5()
    for line in ifile:
        flag = False
        for index in dicX:
            m = hashlib.md5()
            m.update(dicX[index])
            if m.hexdigest() == line.rstrip():
                print>>ofile, line.rstrip()+"\t"+dicX[index]+"\t"+str(index)
                flag = True
        if flag is False:
            print line.rstrip()+"\t couldn't be cracked"
            #print line.rstrip()+" not found"
            

def main():
    s = time.time()
    dic = Q1A(infile)
    e = time.time()
    print "Q1A:\t"+str(e-s)
    s =time.time()
    Q1B(dic)
    e =time.time()
    print "Q1B:\t"+str(e-s)
    s =time.time()
    Q2A(dic)
    e =time.time()
    print "Q2A:\t"+str(e-s)
    s =time.time()
    Q2B(dic)
    e =time.time()
    print "Q2B:\t"+str(e-s)
    s =time.time()
    Q3A(dic)
    e =time.time()
    print "Q3A:\t"+str(e-s)
    s =time.time()
    Q3B(dic)
    e =time.time()
    print "Q3B:\t"+str(e-s)
    s =time.time()
    Q4(dic)
    e =time.time()
    print "Q4:\t"+str(e-s)



main()
