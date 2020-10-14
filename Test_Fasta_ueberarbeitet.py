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

# open_vcf(): opens the vcf file of the samples that shoul be analyzed 
def open_vcf():
    file = sys.argv[2]
    if file[len(file)-2:len(file)] == "gz":
        vcf =gzip.open(sys.argv[2], 'rt')
    elif file[len(file)-3:len(file)] == "vcf":
        vcf = open(sys.argv[2])
    else:
        vcf = ""
        sys.exit(0)
    return vcf
vcf = open_vcf()


# read_vcf(): reads line by line and stores the chromosomes, the positions of the SNPs and the refernce and alternate bases in a list
def read_vcf():

    chromosome = ""
    global position
    position = 0
    global variantlist 
    variantlist = []
    global baselist
    baselist = []
    c = 0

    line ="variant"
    while line != "":
        line = vcf.readline()
        if line == "":
            break
        if line[0] != "#":
            data = line.split()

            last_chr = chromosome
            chromosome = data[0]
            position = data[1]
            reference = data[3]
            alternate = data[4]
            c +=1
            
            if last_chr != chromosome:
                variantlist.append([chromosome, position])
                baselist.append([reference, alternate])
            else:
                l = len(variantlist)
                variantlist[l-1].append(position)
                baselist.append([reference, alternate])
    baselist.append(c)

    print(variantlist)



# SNP_sameline(): when the Sequence of the first SNP of the List is found in the reference fasta (SNP beginns in line y and neds in line y +1), the method checks, 
#                 if the Positon of the next SNPs in the list are located in the same two lines 
def SNP_sameline():
    global sameline
    #global seq
    sameline = 0
    #seq = ""
    print(firstlist)
    print('b_1:', b_1)
    print('b_2:',b_2)
    print("who is in sameline")
    for i in range(1, len(firstlist),1):
        print(firstlist[i])
        if int(firstlist[i]) <= b_2 or (int(firstlist[i])-15) <= b_2:
            print(firstlist[i], "is in same line")
            sameline += 1
            print("sameline:" ,sameline)
            print("")
    print(sameline)


# Option_sameline():
def Option_sameline(option):
    t = []
    for i in range (1, sameline + 1,1):
                
        t.append(firstlist[i])
        print(t)
        diff = int(firstlist[i]) - int(x)
        print(diff)
        newseq = seq[diff:len(seq)]

        write_fasta(option, firstlist[i])
        out.write("{}".format(newseq))

        print("")
        print(option)
        print("")
        print("b1",b_1)
        print("i-15", int(firstlist[i])-15)
        print("i", firstlist[i])
        print("i+15", int(firstlist[i])+15)
        print("b2",b_2)
       
        print(seq)
        print(newseq)
        print(line)
        for j in range (0, diff,1):
            u = line[j]
            out.write("{}".format(u))
            print(u)
        print("")
    print("firstlist: ",firstlist)    
    firstlist.remove(x)
    print("remove x")
    print("x:", x," gefunden, entfernt")
    print("")
    print("firstlist", firstlist)
    for i in t:
        print("i in t", i)
        firstlist.remove(i)
        print("i:", i, "gefunden, entfernt")


    if firstlist == []:
        variantlist.remove([])



# Option_i_3(): when the searched sequence around the next SNP begins on the current line in the fasta file and ends in the next line
#               calculates how many bases of the sequence are situated in this line, stores the sequece of these bases in the variable seq 
#               skips to the next line in fasta and stores the rest of the sequence
def Option_i_3():                   
# OPTION i-3                                     int(x) - 15 < b_2

    global b_1
    global b_2
    global line
    global seq
     
               
    print("b1",b_1)
    print("x-15", int(x)-15)
    print("x", x)
    print("x+15", int(x)+15)
    print("b2",b_2)
    a = b_2 - (int(x)-15) + 1
    print(a)
    for i in range(0, a, 1):            
        w = int(x) -15 - b_1  - 1
                    #s = b_2 -i
        s = w + i
        print("s",s)
        print("i", i)

        y = line[s]
        seq = seq +y
        print(y)
        print(line)
        out.write("{}".format(y))
                
    line = str(fasta.readline())
    b_1 = b_2
    l = len(line)-1
    b_2 = b_2 + l
    c = (int(x)+15) - b_1 
    for i in range (0, c):
        s = 0 + i
        print("s", s)
        print("i", i)
        y = line[s]
        seq = seq + y
        print(y)
        print(line)
        out.write("{}".format(y))
               
 #   firstlist.remove(x)
    # print("firstlist",firstlist)
    # print("x:", x," gefunden, entfernt")
    # print("")

    # if firstlist == []:
        # variantlist.remove([])
               

                    
# Option_i_1(): the sequence around the nSNP in the list is located on the current line
def Option_i_1():
# OPTION i-1                       int(j)+15 <= b_2 and int(j)-15 >= b_1

    print("b1",b_1)
    print("x-15", int(x)-15)
    print("x", x)
    print("x+15", int(x)+15)
    print("b2",b_2)

    for i in range(15, -16, -1):             # looping over each of the 31 bases of the sequence around the SNP: (15 bases in each direction + SNP)  
                                                     # writing down each base of the searched sequence
                                                     
        w = int(x) - b_1 - 1                 # w = position of the SNP in current line where       
        s = w-i                              # s = position of the current base
        print("s",s)
        print("i", i)
        y = line[s]                          # y = current base
        print(y)
        print(line)

        out.write("{}".format(y))            # adding the current base to the sequence in the fasta output file
    firstlist.remove(x)                      # removing the first / current SNP of the list -> so the next SNP is now on first place in the list and his position can be searched
    print(firstlist)
    print("x:", x," gefunden, entfernt")
    print("")
    if firstlist == []:                        # if list of the current chromosome is empty, list will be removed so it can be continued with the SNPs of the next chromosome
        variantlist.remove([])



def Option_i_2():
# Option_i_2
    global b_1
    global b_2
    global line
    global seq
    global l
    
    print("")
    print("b1",b_1)
    print("x-15", int(x)-15)
    print("x", x)
    print("x+15", int(x)+15)
    print("b2",b_2)
    for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

        w = int(x) - b_1 - 1
        s = w-i
        print("w", w)
        print("s",s)
        print("i", i)
        if s == str(b_2)[-2:len(str(b_2)) ]:
            rest = i -1                     #rest = wieviele der 15 zeilen sind in der naechsten zeile?
            print("rest", rest)
            break
        if s == l:
            rest = i + 16
            print("rest", rest)
            print("")
            break
        y = line[s]
        print(y)
        print(line)
        seq = seq + y
        out.write("{}".format(y))
    if rest != 0:
        line = str(fasta.readline())
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        for i in range (0, rest):
            print("")
            print("Rest nicht 0")
            print("x", x)
            print("b1",b_1)

            print("x+15", int(x)+15)
            print("b2",b_2)
            w = int(x) - b_1 - 1
            s = 0 + i
            print("s",s)
            print("i", i)
                    
            y = line[s]
            print(y)
            print(line)
            out.write("{}".format(y))
            seq = seq + y

                
                
# check_options(): checks for the remaining SNPs on the current chromosome if they are identical to the current SNP,
#                  if they are completely located on the current line of the fasta, or
#                  if the sequence around them begins on the current line of the fasta and end on the following
def check_options():

    global m
    global o
    m = 0
    n = 0
    o = 0
    for j in firstlist: # for all remaining SNPs on the current chromosome
        print("b_1", b_1)
        print(j)
        print("b_2", b_2)
        print("")
        if j == x:                  # current and next SNP are on the same position, so the sequence around them is identical
            out.write("\n")
            out.write("> {} {} |{} |{}:{} \n".format(chr_list, x, name_sample, (int(x)-15),(int(x)+15)))
            out.write("{}".format(seq))
            print("j == x")
            print(firstlist)
            firstlist.remove(x)
            print(firstlist)
            print("x:", x, "gefunden,entfernt")
            print("")
                    
        elif (int(j)+15) <= b_2 and (int(j)-15) >= b_1:        # next SNP is completey located on the current line of the fasta
                                                               # --> Option_i_1
            m += 1
            print(b_1)
            print(j)
            print(b_2)
            print("m",m)
        elif (int(j) - 15) < b_2:            # sequence around the next SNP begins on the current line of the fasta
                                             # --> Option_i_3
            o += 1
            print(b_1)
            print(j)
            print(b_2)
            print("o",o)
                # elif int(j) <= b_2 and int(j) >= b_1:
                    # n += 1
                    # print(b_1)
                    # print(j)
                    # print(b_2)
                    # print("n",n)
    if m == 0 and o == 0: # and n == 0:
        print("alle drei gleich 0")
    print("") 
    print("check_options")    
    print("m", m)
    print("o", o)
    return m,o


# write_fasta(): writes the sequences around tht SNPs in a fasta file
def write_fasta(option_type, position):
    out.write("\n")
    out.write("{}".format(option_type))
  #              out.write("\n b_1: {}  x: {}   b_2: {}".format(b_1, x, b_2)) 
    out.write("\n")
    out.write("> {} {} |{} |{}:{} \n".format(chr_list, position, name_sample, (int(position)-15),(int(position)+15)))


# read_fasta(): reads the fasta file of the refernce sequence line by line and searches the Positions of the SNPs in the List
def read_fasta():

    read_vcf()
    
    
    global line
    global b_1                             #number of bases exclusive the current line --> number of the last base of the latest line
    global b_2                             #number of bases inclusive the current line --> number of the last base of the current line
    global l                               # number of lines
    
    b_2 = -1
    b_1 = -1
    l = 0
    line = "fastaline"
    
        
    global m            # counts for all remaining SNPs on the current chromosome, if the SNP is completey located on the current line of the fasta
    global o            # counts for all remaining SNPs on the current chromosome, if the sequence around the next SNP begins on the current line of the fasta

    
    global name_vcf     # name of the vcf file
    global name_sample  # name of the analysed samples
    name_vcf = str(sys.argv[2])
    name_sample = name_vcf[name_vcf.index("DX"):name_vcf.rindex("DX") + (name_vcf.rindex("DX") - name_vcf.index("DX"))-1]

    global out          # output file --> fasta file with the sequences around the SNPs
    out = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_SNP_sequences_1.fa".format(name_sample,name_sample), "w")  # output: fasta file containing the sequence around the snps
    out.write("{}".format(baselist))
    
    global chr_list
    chr_list = []

    
    while line != "":
        line = str(fasta.readline())                  
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        if line == "":
           break
        if variantlist == []:
            break
        if variantlist[0] == []:        
            variantlist.remove([])
        if variantlist[0][0][0:3] == 'chr':
        
            chr_list = variantlist[0][0]
            print("chromosome: ",chr_list)
            print("")
            while line[0] !=">":
                line = str(fasta.readline())   
                b_1 = b_2
                l = len(line)-1
                b_2 = b_2 + l
            if line[0] == ">":                              # checking if line is header --> start of a new hromosome
                print("line begins with >")
                print(line)                              
                print("number of bases:", b_2)
                b_2 = 0
                b_1 = -1
                splittedline = line.split(" ")
                chr_fa = splittedline[0][1:len(splittedline[0])]               
                print("fasta chromosome:", chr_fa)
                print("variantlist chromosome", chr_list)
                print("")
                        
                if chr_fa == chr_list:          # checking if the chromosome in the first list is the same as the chromosome in the current fasta header
                    print("")
                    print(variantlist)
                    variantlist[0].remove(chr_list)     #remove chromosome of the list
                    
                    print("")
                    print(variantlist)
                    line = str(fasta.readline())
                    b_1 = b_2
                    l = len(line)-1
                    b_2 = b_2 + l
                    continue
                continue

        


        global firstlist
        firstlist = variantlist[0]              # variantlist: list with lists for each chromosome that contain the SNPs of the samples
                                                # firstlist: first list in the variantlist, contains the SNPs for the currrent chromosome

        if variantlist[0] == []:                #if firstlist is empty, the list is deleted
            variantlist.remove([])
            break                
        
        global x
        x = firstlist[0]                        # current SNP Position in list (no integer is saved as string!)

        rest = 0


        # searching the SNPs of the current chromosome and the sequence around --> starting with SNP -15 and ending with SNP + 15
        # testing, if the sequence of the first (current) SNP in the list starts in the current line of the reference fasta
        if int(x)-15 <= b_2 and int(x)-15 >= b_1:
        
# OPTION 1:  The sequence of the SNP is completely located on the current line
                  
           if int(x)+15 <= b_2 and int(x)+15 >= b_1:
            print("OPTION1")
            write_fasta("OPTION 1",x)               # writing the fasta header information in the output file
            
            Option_i_1()
            
            m = 0
            n = 0
            o = 0
            for j in firstlist:                     # checking for all SNPs in the current chromosome list, if they are completely or begin in the current line
                if (int(j)+15) <= b_2 and (int(j)-15) >= b_1:
                    m += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("m",m)
                elif int(j) <= b_2 and int(j) >= b_1:
                    n += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("n",n)
                # if int(j) > b_2:
                    # o += 1
                    # print(b_1)
                    # print(j)
                    # print(b_2)
                    # print("o",o)
            if m == 0 and n == 0: # and o == 0:
                print("alle drei gleich 0")
                continue
            
            while m > 0:
# OPTION 1-1                        int(j)+15 <= b_2 and int(j)-15 >= b_1
                x = firstlist[0]

                write_fasta("OPTION 1-1", x)
            
                print("option 1-1")
            
                Option_i_1()
                
                m -= 1    
            
            while n > 0:
# OPTION 1-2                            int(x) <= b_2 and int(x) >= b_1
                x = firstlist[0]
                
                write_fasta("OPTION 1-2", x)
                
                print("option 1-2")
                
                Option_i_2()

                firstlist.remove(x)
                print(firstlist)
                print("x:", x," gefunden, entfernt")
                print("")

                if firstlist == []:
                    variantlist.remove([])
                n -= 1
    
           elif int(x) <= b_2 and int(x) >= b_1:
# OPTION 2
            print("OPTION2")

            write_fasta("OPTION 2", x)
            
            # sameline = 0
            global seq
            seq = ""
            
            SNP_sameline()
            
            Option_i_2()

 

#OPTION2-1


            Option_sameline("OPTION 2-1")


            m = 0
            o = 0
            check_options()
           
           
            
            while m > 0:
# OPTION 2-2                        
# int(j)+15 <= b_2 and int(j)-15 >= b_1

                x = firstlist[0]
                
                write_fasta("OPTION 2-2", x)
            
                print("option 2-2")
            
                Option_i_1()
                m -= 1
            
   
            
            while o > 0:                    
# OPTION 2-3                                     
# int(x) - 15 < b_2

                x = firstlist[0]
                print("")
                print("OPTION2-3")

                write_fasta("OPTION 2-3", x)
                
                Option_i_3()
                firstlist.remove(x)
                print("firstlist",firstlist)
                print("x:", x," gefunden, entfernt")
                print("")
                if firstlist == []:
                    variantlist.remove([])
                o -= 1
                print(line)
               

           
                    
           elif int(x) > b_2:
# OPTION 3
              seq = ""
              print("OPTION3")

              write_fasta("OPTION 3", x)

              
              SNP_sameline()
              
              

              Option_i_3()
   
              

#OPTION3-1
             
              Option_sameline("OPTION 3-1")

              
  

              check_options()

              print("")  
              print("m", m)
              print("o", o)
              
              
              while m > 0:
# OPTION 3-2                        
# int(j)+15 <= b_2 and int(j)-15 >= b_1

                x = firstlist[0]

                write_fasta("OPTION 3-2", x)
                print("option 3-2")
                
                
                Option_i_1()
                m -= 1
            
 
              
              while o > 0:                    
# OPTION 3-3                                     
# int(x) - 15 < b_2

                x = firstlist[0]
                print("OPTION3-3")

                write_fasta("OPTION 3-3", x)
                
                Option_i_3()
                firstlist.remove(x)
                print("firstlist", firstlist)
                print("x:", x," gefunden, entfernt")
                print("")
                if firstlist == []:
                    variantlist.remove([])
                o -= 1
                print(line)
               

    out.close()



read_fasta()


def insert_snps():
    print("insert SNPs")
    out = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_SNP_sequences_1.fa".format(name_sample,name_sample), "r")
    sequences = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_SNP_sequences_output_1.fa".format(name_sample,name_sample), "w")
    q = 0
    line = "fasta"
    while  line != "":
        #print(line)
        line = str(out.readline())
        #print(line)
        q += 1
        if line == "":
            break
        if line[0] == ">":
            sequences.write("{}\n".format(line))
            print(line)
        if line[0] == "A" or line[0] == "T" or line[0] == "G" or  line[0] == "C":
            end = len(line)

            sequences.write("{}".format(line[0:15]))

            l = len(baselist[0][0])

            sequences.write("{}{}\n".format((baselist[0][1]), line[15+l:len(line)]))

            h = baselist[0]
            baselist.remove(h)
            
                
    sequences.close()    

insert_snps()