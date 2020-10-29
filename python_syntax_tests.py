import sys
# x = "ashblsiufglsgliuanlsifgleiurnldef"
# # 33
# print(len(x))
# print(x[32])
# print("")
# for i in range(0, len(x)):
	# print(x[i])
    
    
def open_fasta():

    file = sys.argv[1]
    if file[len(file)-3:len(file)] == ".fa":
        fasta = open(sys.argv[1])
    else:
        fasta = ""
        sys.exit(0)

    return fasta

fasta = open_fasta()

line = str(fasta.readline())
while line != "":
       # line = str(fasta.readline())
        while line[0] == ">" or line[0] == "N":
            line = str(fasta.readline())
        print(line)
        for i in range(0,len(line)-3):
            a = line[i]
            b = line[i + 1]
            c = line[i + 2]   
            print(a,b,c)
            print("")
        line = str(fasta.readline())
        if line[0] == ">":
            break
        print(line)
        d = b
        e = c
        f = line[0]
        print(d,e,f)
        print("")
        d = c
        e = line[0]
        f = line[1]
        print(d,e,f)
        print("")
