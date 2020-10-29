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
    
#    Start_Stop_Positions = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/GRCh37_start_stop.txt", "w")
    
    
    while line != "":
        line = str(fasta.readline())                  
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        if line == "":
           break
        if line[0] == ">":                              # checking if line is header --> start of a new hromosome
            # print("line begins with >")
            # print(line)                              
            # print("number of bases:", b_2)

            b_2 = 0
            b_1 = -1
            splittedline = line.split(" ")
            chr_fa = splittedline[0][1:len(splittedline[0])]              
            Start_Stop_Positions = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/GRCh37_start_stop_new_{}.txt".format(chr_fa), "w")
             
            print("chromosome:", chr_fa)
            print("") 
            print("###########################################################################################################")
            print("")
            Start_Stop_Positions.write("Chromosome:  {}".format(chr_fa))
            Start_Stop_Positions.write("\n")
            Start_Stop_Positions.write("#################################################################################################\n")
            Start_Stop_Positions.write("")
        for i in range(0,len(line)-2):
            a = line[i]
            b = line[i + 1]
            c = line[i + 2]
            #print("a", a)
            pos_a = b_1 + i + 1
            if a == "A" and b == "T" and c == "G":
                print("Startcodon gefunden:", a,b,c, "an Position", pos_a)
                Start_Stop_Positions.write("Startcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                Start_Stop_Positions.write("")
                print("")
                for j in range(c + 1, l
                        
                        
                        
 # STOP CODONS :
            if a == "T" and b == "A" and c == "A":
                        print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                        Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                        Start_Stop_Positions.write("")
                        # print(line)
                        # print(b_1)
                        # print(pos_a)
                        # print(b_2)
                        print("")
                                    
            if a == "T" and b == "A" and c == "G":
                        print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                        Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                        Start_Stop_Positions.write("")
                        # print(line)
                        # print(b_1)
                        # print(pos_a)
                        # print(b_2)
                        print("")
                                    
            if a == "T" and b == "G" and c == "A":
                        print("Stopcodon gefunden:", a,b,c, "an Position", pos_a)
                        Start_Stop_Positions.write("Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_a))
                        Start_Stop_Positions.write("")
                        # print(line)
                        # print(b_1)
                        # print(pos_a)
                        # print(b_2)
                        print("")
                                                  

    


read_fasta()