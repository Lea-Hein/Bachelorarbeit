import sys
# x = "ashblsiufglsgliuanlsifgleiurnldef"
# # 33
# print(len(x))
# print(x[32])
# print("")
# for i in range(0, len(x)):
	# print(x[i])
    
def search_codons():
    global line
    global b_1
    global b_2
    global l
    for i in range(0,len(line)-3):
        a = line[i]
        b = line[i + 1]
        c = line[i + 2]
        # print(a,b,c)
        # print("")
        global pos_a
        pos_a = b_1 + i + 1
#        print(pos_a)
        search_start(a,b,c,i)
    line = str(fasta.readline())
#     if line[0] == ">":
#        break
    b_1 = b_2
    l = len(line)-1
    b_2 = b_2 + l
#    print(line)
    
    d = b
    e = c
    f = line[0]
    # print(d,e,f)
    # print("")
    pos_a = b_1 + i + 1
    search_start(d,e,f,i)
    d = c
    e = line[0]
    f = line[1]
    # print(d,e,f)
    # print("") 
    pos_a = b_1 + i + 1
    search_start(d,e,f,i)

def search_start(n_1,n_2,n_3,i):
    global stopcodon
# SEARCH START
    print("SEARCH START")
    if n_1 == "A" and n_2 == "T" and n_3 == "G":
        print("Startcodon gefunden:", n_1,n_2,n_3, "an Position", pos_a)
        Start_Stop_Positions.write("Startcodon {}{}{} an Position {}\n".format(n_1,n_2,n_3,pos_a))
        Start_Stop_Positions.write("")
        print(n_1,n_2,n_3)
        print("Position",pos_a)
        print("position", i)
        print("")
        stopcodon = 0
        search_stop(i)
 
def search_stop(i):
    global line
    global b_1
    global b_2
    global l
    global pos_a
    global stopcodon
    global a
    global b
    global c
    print("search Stop gestartet")
    #print(i)

    while stopcodon == 0:
        print("search_stop: while schleife")
        for i in range(i +3,len(line)-3,3):
            a = line[i]
            b = line[i + 1]
            c = line[i + 2]
        # print("")
# SEARCH STOP 1
            print("SEARCH STOP 1")
        # print(a, b, c)
            pos_a = b_1 + i + 1
            if a == "T" and b == "A" and c == "A":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "A" and c == "G":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "G" and c == "A":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            if stopcodon > 0:
                break
        
        if a == line[57]:
            line = str(fasta.readline())
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            print(line)
# SEARCH STOP 2
            print("SEARCH STOP 2")
            search_stop(0)
        elif a == line[56]:
        
            a = line[59]
            
            line = str(fasta.readline())
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            print(line)
            
            b = line[0]
            c = line[1]
# SEARCH STOP 3
            print("SEARCH STOP 3")            
            pos_a = b_1 + i + 1
            if a == "T" and b == "A" and c == "A":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "A" and c == "G":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "G" and c == "A":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            if stopcodon > 0:
                break
            search_stop(2)
            
        elif a == line[55]:
            
            a = line[58]
            b = line[59]
            
            line = str(fasta.readline())
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            print(line)
            
            c = line[0]
 # SEARCH STOP 4
            print("SEARCH STOP 4")           
            pos_a = b_1 + i + 1
            if a == "T" and b == "A" and c == "A":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "A" and c == "G":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "G" and c == "A":
                print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                stopcodon += 1
                break
            if stopcodon > 0:
                break
            search_stop(1)
            
        

 
def open_fasta():

    global b_1
    b_1 = -1
    global b_2
    b_2 = -1
    global l
    l = 0

    file = sys.argv[1]
    if file[len(file)-3:len(file)] == ".fa":
        fasta = open(sys.argv[1])
    else:
        fasta = ""
        sys.exit(0)

    return fasta

fasta = open_fasta()

def skript():
    global line
    line = str(fasta.readline())
    global Start_Stop_Positions
    while line != "":
       # line = str(fasta.readline())
        if line[0] == ">":
            splittedline = line.split(" ")
            chr_fa = splittedline[0][1:len(splittedline[0])]              
            Start_Stop_Positions = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/GRCh37_start_stop_new_{}.txt".format(chr_fa), "w")
            Start_Stop_Positions.write("Chromosome:  {}".format(chr_fa))
            Start_Stop_Positions.write("\n")
            Start_Stop_Positions.write("#################################################################################################\n")
            Start_Stop_Positions.write("")
            
            line = str(fasta.readline())
            b_1 = 0
            b_2 = 0
        while line[0] == "N":
            line = str(fasta.readline())
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
        print(line)
        search_codons()

skript()