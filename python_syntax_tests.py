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
    global i_pos_stop
    global found_start
    found_start = 0
    global Start_Stop_Positions
    a = ""
    b = ""
    c = ""
    i = 0
  #  print("stop start position", pos_start_stop)
    print(" start CODON SEARCH")
    print("stop position", i_pos_stop)
    print("")
   # i_pos_stop = pos_stop - b_1
    for i in range(i_pos_stop,len(line)-3):
        print("codon_for_schleife   i:", i)
        a = line[i]
        b = line[i + 1]
        c = line[i + 2]
        if c == "N":
            if c == "N" and line[len(line)-2] == "N":   #Passt das so???
                Start_Stop_Positions.write("c == N, {} {} {}, Rest der Zeile == N".format(a,b,c))
                line = str(fasta.readline())
                N_line()
            else:
                Start_Stop_Positions.write("c == N, {} {} {}, suche weiter nach Codon".format(a,b,c))
          #  N_line(), b_1 und b_2 duerfen nicht weitergezaehlt werden
        print(a,b,c)
        # print("")
        global pos_a
        pos_a = b_1 + i + 1
#        print(pos_a)
        search_start(a,b,c,i)
        if found_start == 1:
            break
    if found_start == 0:
        print(line)
        print("")
            # print("start und stop  gefunden --> abbrechen von search_codons")
            # sys.exit()
            
        line = str(fasta.readline())
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        if line == "":
            print("leere Zeile")
            sys.exit()
        if line[0] == ">":
            new_chromosome()
            print("##########################################################################################################################################################################")

        while line[0] == "N" and line[len(line)-2] == "N":
            Start_Stop_Positions.write("Line startet und endet mit N, starte SKRIPT\n")
            line = str(fasta.readline())
            N_line()
        #    skript()
        if line[0] == ">":
               new_chromosome()
        Start_Stop_Positions.write("Line startet mit {}\n".format(line[0]))
        print(line)
        i_pos_stop = 0
        print(line)

        d = b
        e = c
        f = line[0]

        pos_a = b_1 + i + 1
        search_start(d,e,f,58)
        d = c
        e = line[0]
        f = line[1]
 
        pos_a = b_1 + i + 1
        search_start(d,e,f,59)

def search_start(n_1,n_2,n_3,x):
    global stopcodon
    global found_start
    global line
    global b_1
    global b_2
    global l
    global i_pos_stop
    global Start_Stop_Positions
# SEARCH START
    print("SEARCH START", i_pos_stop)
    if n_1 == "A" and n_2 == "T" and n_3 == "G":
        
        print("+ Startcodon gefunden:", n_1,n_2,n_3, "an Position", pos_a)
        Start_Stop_Positions.write("+ Startcodon {}{}{} an Position {}\n".format(n_1,n_2,n_3,pos_a))
        Start_Stop_Positions.write("")
        print(n_1,n_2,n_3)
        print("Position",pos_a)
        print("position", x)
        Start_Stop_Positions.write("i_position: {}\n".format(x))
        Start_Stop_Positions.write("{}\n".format(line))
        print(line)
        print(b_1)
        print(b_2)
        print("")
        stopcodon = 0
        if x == 59:
            search_stop(2)
            found_start = 1
        if x == 58:
            search_stop(1)
            found_start = 1
        if x == 57:
            line = str(fasta.readline())
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            if line == "":
                print("leere Zeile")
                sys.exit()
            if line[0] == ">":
               new_chromosome()
            while line[0] == "N" and line[len(line) -2] == "N":
                Start_Stop_Positions.write("Line startet mit N, starte SKRIPT\n")
            #    skript()
                line = str(fasta.readline())
                N_line()
            if line[0] == ">":
               new_chromosome()
            print(line)
            Start_Stop_Positions.write("Line startet mit {}\n".format(line[0]))
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            
            search_stop(0)
            found_start = 1
            if a == "N" or b == "N" or c == "N":
                Start_Stop_Positions.write("Start suche abbrechen, zurueck ")
                return 1
        else :
            search_stop(x)
            found_start = 1
            if a == "N" or b == "N" or c == "N":
                Start_Stop_Positions.write("Start suche abbrechen, zurueck ")
                return 1
 
def search_stop(i):
    global line
    global b_1
    global b_2
    global l
    global pos_a
    global pos_stop
    global i_pos_stop
    global stopcodon
    global a
    global b
    global c
    global Start_Stop_Positions
    print("search Stop gestartet")
    #print(i)

    while stopcodon == 0:
 #       print("search_stop: while schleife")
        
        if i < 55:
            for i in range(i +3,len(line)-3,3):
                a = line[i]
                b = line[i + 1]
                c = line[i + 2]
                if a == "N" and b == "N" and c == "N":
                    Start_Stop_Positions.write("a, b und c == N, {} {} {}, break und return 1\n".format(a,b,c))

                    Start_Stop_Positions.write("{}\n".format(line))             ### warum???
                    line = str(fasta.readline())
                    N_line()
                    Start_Stop_Positions.write("{}\n".format(line))
                    return 1
                  #  break
                    #skript()
          # falls restliche zeile nur noch N lauft die schleife durch und nichts passiert
                    # line = str(fasta.readline())
                    # if line[0] == ">":
                        # new_chromosome()
                    # while line[0] == "N" and line[len(line) -1] == "N":
                        # Start_Stop_Positions.write("Line startet mit N, starte SKRIPT\n")

                        # N_line()
                if a == "N" or b == "N" or c == "N":
                    Start_Stop_Positions.write("a,b,c = N:  {} {} {}, naechsten codon suchen\n".format(a,b,c))
                else:
# SEARCH STOP 1
                    print("SEARCH STOP 1")
                    Start_Stop_Positions.write("SEARCH STOP 1\n")
        # print(a, b, c)
                    pos_stop = b_1 + i + 1
                    i_pos_stop = i
                    if a == "T" and b == "A" and c == "A":
                        print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                        Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                        Start_Stop_Positions.write("")
                        print(pos_stop)
                        print(i_pos_stop)
                        print("")
                        stopcodon += 1
                        break
                    elif a == "T" and b == "A" and c == "G":
                        print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                        Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                        Start_Stop_Positions.write("")
                        print(pos_stop)
                        print(i_pos_stop)
                        print("")
                        stopcodon += 1
                        break
                    elif a == "T" and b == "G" and c == "A":
                        print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                        Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                        Start_Stop_Positions.write("")
                        print(pos_stop)
                        print(i_pos_stop)
                        print("")
                        stopcodon += 1
                        break
                    if stopcodon > 0:
                        print("stopcodon > 0")
                        break
# TEst ob druchlauft in chr 9 nachdem N-Sequenz aufgetrete n ist
        # if line[0] == "N" and line[len(line)-2] == "N":
                # Start_Stop_Positions.write("Line startet und endet mit N \n")
                # line = str(fasta.readline())
                # N_line()
                # return 1
        if stopcodon == 0 and line[len(line)-2] =="N":
            return 1
            Start_Stop_Positions.write("zeile endet mit N, Stop suche wird abgebrochen")
            line = str(fasta.readline())
            N_line()
            if line[0] == ">":
                new_chromosome()
            while line[0] == "N" and line[len(line) -1] == "N":
                Start_Stop_Positions.write("Line startet mit N und endet mit N, return 1\n")
                line = str(fasta.readline())
                N_line()
            return 1    
                
 # SEARCH STOP 2               
        if stopcodon == 0 and a == line[57]:
            line = str(fasta.readline())
            if line == "":
                print("leere Zeile")
                sys.exit()
            print(line)
            Start_Stop_Positions.write("Line startet mit {}\n".format(line[0]))
            if line[0] == ">":
                new_chromosome()
            if line[0] == "N":
                Start_Stop_Positions.write("Line startet mit N, return 1\n")
              #  N_line()
                return 1
            if line[0] == ">":
               new_chromosome()
            print(line)
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
           # print(line)

            print("SEARCH STOP 2")
            Start_Stop_Positions.write("SEARCH STOP 2 -> search stop 1\n")
            Start_Stop_Positions.write("{}\n".format(line))     
            search_stop(0)
            if search_stop == True:
                Start_Stop_Positions.write("rueckgabe 1 == true")
                return 1
            
        elif stopcodon == 0 and a == line[56]:
        
            a = line[59]
            
            line = str(fasta.readline())
            if line == "":
                print("leere Zeile")
                sys.exit()
            Start_Stop_Positions.write("Line startet mit {}\n".format(line[0]))
            print(line)
            if line[0] == ">":
                new_chromosome()
            if line[0] == "N":
                Start_Stop_Positions.write("Line startet mit N,\n")
                
            if line[0] == ">":
               new_chromosome()
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            print(line)
            
            b = line[0]
            c = line[1]
# SEARCH STOP 3
            print("SEARCH STOP 3")  
            Start_Stop_Positions.write("SEARCH STOP 3\n") 
            Start_Stop_Positions.write("{}\n".format(line))            
            pos_stop = b_1 + i + 1
            i_pos_stop = i
            if a == "T" and b == "A" and c == "A":
                print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                Start_Stop_Positions.write("")
                print(pos_stop)
                print(i_pos_stop)
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "A" and c == "G":
                print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                Start_Stop_Positions.write("")
                print(pos_stop)
                print(i_pos_stop)
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "G" and c == "A":
                print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                Start_Stop_Positions.write("")
                print(pos_stop)
                print(i_pos_stop)
                print("")
                stopcodon += 1
                break
            if stopcodon > 0:
                break
            search_stop(2)
            
        elif stopcodon == 0 and a == line[55]:
            
            a = line[58]
            b = line[59]
            
            line = str(fasta.readline())
            if line == "":
                print("leere Zeile")
                sys.exit()
            Start_Stop_Positions.write("Line startet mit {}\n".format(line[0]))
            print(line)
            if line[0] == ">":
                new_chromosome()
            if line[0] == "N":
                Start_Stop_Positions.write("Line startet mit N, starte SKRIPT\n")
                skript()
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            print(line)
            
            c = line[0]
 # SEARCH STOP 4
            print("SEARCH STOP 4")
            Start_Stop_Positions.write("SEARCH STOP 4\n")
            Start_Stop_Positions.write("{}\n".format(line))     
            pos_stop = b_1 + i + 1
            i_pos_stop = i
            if a == "T" and b == "A" and c == "A":
                print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                Start_Stop_Positions.write("")
                print(pos_stop)
                print(i_pos_stop)
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "A" and c == "G":
                print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                Start_Stop_Positions.write("")
                print(pos_stop)
                print(i_pos_stop)
                print("")
                stopcodon += 1
                break
            elif a == "T" and b == "G" and c == "A":
                print("- Stopcodon gefunden:", a,b,c, "an Position", pos_stop)
                Start_Stop_Positions.write("- Stopcodon {}{}{} an Position {}\n".format(a,b,c,pos_stop))
                Start_Stop_Positions.write("")
                print(pos_stop)
                print(i_pos_stop)
                print("")
                stopcodon += 1
                break
            if stopcodon > 0:
                break
            search_stop(1)
            
        
def new_chromosome():
    global line
    global Start_Stop_Positions
    global pos_start
    global pos_stop
    global i_pos_stop
    global b_1
    global b_2
    global l
    i_pos_stop = 0
    pos_stop = 0
    pos_start = 0
    splittedline = line.split(" ")
    chr_fa = splittedline[0][1:len(splittedline[0])]              
    Start_Stop_Positions = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/GRCh37_start_stop_new_{}.txt".format(chr_fa), "w")
    Start_Stop_Positions.write("Chromosome:  {}".format(chr_fa))
    Start_Stop_Positions.write("\n")
    Start_Stop_Positions.write("#####################################################################################################################################\n")
    print("")
    print("##########################################################################################################################################################################\n")
    print("new chromosome", chr_fa)
    print("")
    
    Start_Stop_Positions.write("")
            
    line = str(fasta.readline())
    i_pos_stop = 0
    b_1 = 0
    b_2 = 0

def N_line():

    global b_1
    global b_2
    global l
  #  line = str(fasta.readline())
    i_pos_stop = 0
    b_1 = b_2
    l = len(line)-1
    b_2 = b_2 + l
    Start_Stop_Positions.write("\n")
    Start_Stop_Positions.write("B1: {}\n".format(b_1))
    Start_Stop_Positions.write("B2: {}\n".format(b_2))
    Start_Stop_Positions.write("{}".format(line))
    # Start_Stop_Positions.write("zeilenende: {}\n".format(line[len(line) -1]))
    # Start_Stop_Positions.write("zeilenende: {}\n".format(line[len(line) -2]))
 
 
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
    line = "Line"
   # line = str(fasta.readline())
    global Start_Stop_Positions
    global pos_start
    global pos_stop
    global i_pos_stop
    global b_1
    global b_2
    global l
    i_pos_stop = 0
    pos_stop = 0
    pos_start = 0
    while line != "":
##### while line entfernen ????
        line = str(fasta.readline())
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        if line == "":
           break
        if line[0] == ">":
            new_chromosome()
        while line[0] == "N" and line[len(line)-2  ] == "N":                # line[len(line)-2] gibt das letzte zeichen der zeile an
            Start_Stop_Positions.write("Chromosom startet mit N, skippe Zeilen, bis zu ende")
            print("Chromosom startet mit N, skippe Zeilen, bis zu ende")
            line = str(fasta.readline())
            N_line()
        if line[0] == ">":
            new_chromosome()
        print(line)
        print("start_skript")
        print("")
        search_codons()

skript()