import sys

# open_fasta(): opens the fasta file of the refernece genome as 'fasta;
def open_fasta():

    file = sys.argv[1]
    if file[len(file)-3:len(file)] == ".fa":
        fasta = open(sys.argv[1])
    else:
        fasta = ""
        sys.exit(0)

    return fasta

fasta = open_fasta()

def read_fasta():
    global b_1
    b_1 = -1
    global b_2
    b_2 = -1
    global l
    l = 0
    global line
    line = "sequence"
    
    while line != "":
        line = str(fasta.readline())                  
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        if line == "":
           break
        for i in range(0,len(line)-2):
            a = line[i]
            b = line[i + 1]
            c = line[i + 2]
            print("a", a)
            if a == "A":
                print("a ist A")
                if b == "T" or b == "U":
                    if c == "G":
                        print("Startcodon gefunden:", a,b,c)
                        print("Position of a:", b_2 - i)

        


read_fasta()