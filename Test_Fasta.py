import sys


def open_fasta():

    file = sys.argv[1]
    if file[len(file)-3:len(file)] == ".fa":
        fasta = open(sys.argv[1])
    else:
        fasta = ""
        sys.exit(0)

    return fasta

fasta = open_fasta()

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


#global chromosome
#chromosome = ""
#global position
#position = 0
#global variantlist
#variantlist = []

def read_vcf():

#    global chromosome
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
    # variantlist = variantlist[2:3]
    # # # print(variantlist)
    # variantlist[0].remove('')
    # variantlist[0].remove('2366893')
    # variantlist[0].remove('2492166')
    # variantlist[0].remove('6214773')
    # variantlist[0].remove('6257784')
    # variantlist[0].remove('8074217')
    # variantlist[0].remove('9778896')
    # variantlist[0].remove('9781209')
    # variantlist[0].remove('11175116')
    # variantlist[0].remove('11184386')
    # variantlist[0].remove('11187845')
    # variantlist[0].remove('11293367')
    # variantlist[0].remove('11850618')
    # variantlist[0].remove('16248728')
    # variantlist[0].remove('16258888')
    # variantlist[0].remove('16262233')
    # variantlist[0].remove('16695981')
    # variantlist[0].remove('24078403')
    # variantlist[0].remove('27100330')
    # variantlist[0].remove('27107263')
    # variantlist[0].remove('28929961')
    # variantlist[0].remove('38185704')
    # variantlist[0].remove('44083248')
    # variantlist[0].remove('45976928')
    # variantlist[0].remove('65310328')
    # variantlist[0].remove('65339266')
    # variantlist[0].remove('78415120')
    # variantlist[0].remove('78432647')
    # variantlist[0].remove('79216389')
    # variantlist[0].remove('5835335')
    # variantlist[0].remove('6636748')
    # variantlist[0].remove('10269544')
    # variantlist[0].remove('25523021')
    # variantlist[0].remove('26373130')
    # variantlist[0].remove('29450422')
    # variantlist[0].remove('36353029')
    # variantlist[0].remove('39240584')
    # variantlist[0].remove('39262296')
    # variantlist[0].remove('39499689')
    # variantlist[0].remove('39530391')
    # variantlist[0].remove('42488637')
    # variantlist[0].remove('44293374')
    # variantlist[0].remove('47600581')
    # variantlist[0].remove('47641563')
    # variantlist[0].remove('48027998')
    # variantlist[0].remove('52799612')
    # variantlist[0].remove('58392720')
    # variantlist[0].remove('58453823')
    # variantlist[0].remove('73518960')
    # variantlist[0].remove('107049476')
    # variantlist[0].remove('107315189')
    # variantlist[0].remove('108476169')
    # variantlist[0].remove('108479392')
    # variantlist[0].remove('111881263')
    # variantlist[0].remove('113610974')
    # variantlist[0].remove('122466739')
    # variantlist[0].remove('128975102')
    # variantlist[0].remove('140992512')
    # variantlist[0].remove('141294285')
    # variantlist[0].remove('141607887')
    # variantlist[0].remove('141625630')
    # variantlist[0].remove('148680747')
    # variantlist[0].remove('148683685')
    # variantlist[0].remove('155534991')
    # variantlist[0].remove('157184342')
    # variantlist[0].remove('158595327')
    # variantlist[0].remove('158637138')
    # variantlist.insert(0, ['chr2', '233164652', '233306655', '233306685'])
    print(variantlist)






def read_fasta():

    read_vcf()

    b_2 = 0                             #number of bases inclusive the current line
    b_1 = 0                             #number of bases exclusive the current line
    l = 0                               # number of lines
    line = "fastaline"
    
    global name_vcf
    global name_sample
    name_vcf = str(sys.argv[2])
    name_sample = name_vcf[name_vcf.index("DX"):name_vcf.rindex("DX") + (name_vcf.rindex("DX") - name_vcf.index("DX"))-1]

    global out
    out = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_SNP_sequences.fa".format(name_sample,name_sample), "w")  # output: fasta file containing the sequence around the snps
    out.write("{}".format(baselist))
    

    
    while line != "":
 #       if (variantlist[0][0]).isdigit() and int(variantlist[0][0])-15 <= b_2:
  #          continue
        # elvariantlist[0][0][0:3] == 'chr':
         #   continue
 #       else:
        line = str(fasta.readline())                    # Zeile a
        b_1 = b_2
        l = len(line)-1
        b_2 = b_2 + l
        #print("start")
#        print(line)
        if line == "":
           break
        if variantlist == []:
            break
        if variantlist[0] == []:
            variantlist.remove([])
        if variantlist[0][0][0:3] == 'chr':
            chr_list = variantlist[0][0]
            print("ist ein chromosom")
            print("")
            while line[0] !=">":
                line = str(fasta.readline())   
                b_1 = b_2
                l = len(line)-1
                b_2 = b_2 + l
            if line[0] == ">":                              # checking if line is header -> for which chromosome ?
                print("beginnt line mit >")
                print(line)                                 # selbe Zeile wie a
                print("number of bases:", b_2)
                b_2 = 0
                b_1 = 0
                splittedline = line.split(" ")
                chr_fa = splittedline[0][1:len(splittedline[0])]               
                #chr_fa = line[1:5]
                print("fasta chromosom:", chr_fa)
                print("listen chromosom", chr_list)
                print("")
                        
                if chr_fa == chr_list:
                    print("")
                    print(variantlist)
                    variantlist[0].remove(chr_list)
                    
                    print("")
                    print(variantlist)
                    line = str(fasta.readline())
                    b_1 = b_2
                    l = len(line)-1
                    b_2 = b_2 + l
                    continue
                continue

                
                                         # selbe Zeile wie a
        


       
        firstlist = variantlist[0]


        if variantlist[0] == []:
            variantlist.remove([])
            break                            #???????????
                        
        x = firstlist[0]                # SNP Position in list, no integer is saved as string!
       
#        print("statuspunkt 1")
        rest = 0

        if int(x)-15 <= b_2 and int(x)-15 >= b_1:
# OPTION 1       
           if int(x)+15 <= b_2 and int(x)+15 >= b_1:
            print("OPTION1")
            out.write("\n")
            out.write("OPTION 1")
            out.write("\n")
            out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
            
            print("b1",b_1)
            print("x-15", int(x)-15)
            print("x", x)
            print("x+15", int(x)+15)
            print("b2",b_2)
            for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                w = int(x) - b_1 - 1                        # 2 ?????
                s = w-i
                print("s",s)
                print("i", i)
                y = line[s]
                print(y)
                print(line)

                out.write("{}".format(y))
            firstlist.remove(x)
            print(firstlist)
            print("x:", x," gefunden, entfernt")
            print("")
            if firstlist == []:
                variantlist.remove([])
                continue
            m = 0
            n = 0
            o = 0
            for j in firstlist:
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
                out.write("\n")
                out.write("OPTION 1-1")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
            
                print("option 1-1")
            
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                    w = int(x) - b_1 - 1                        # 2 ?????
                    s = w-i
                    print("s",s)
                    print("i", i)
                    y = line[s]
                    print(y)
                    print(line)
                    out.write("{}".format(y))
                firstlist.remove(x)
                print(firstlist)
                print("x:", x," gefunden, entfernt")
                print("")
                if firstlist == []:
                    variantlist.remove([])
                m -= 1    
            
            while n > 0:
# OPTION 1-2                            int(x) <= b_2 and int(x) >= b_1
                x = firstlist[0]
                out.write("\n")
                out.write("OPTION 1-2")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
                print("option 1-2")
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                    w = int(x) - b_1 - 1
                    s = w-i
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
            out.write("\n")
            out.write("OPTION 2")
            out.write("\n")
            out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
            sameline = 0
            seq = ""
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
            t = []
            for i in range (1, sameline + 1,1):
                
                t.append(firstlist[i])
                print(t)
                diff = int(firstlist[i]) - int(x)
                print(diff)
                newseq = seq[diff:len(seq)]
                out.write("\n")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, firstlist[i], (int(firstlist[i])-15),(int(firstlist[i])+15)))
                out.write("{}".format(newseq))

                
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
            print("firstlist", firstlist)
            for i in t:
                print("i in t", i)
                firstlist.remove(i)
                print("i:", i, "gefunden, entfernt")
            print("firstlist",firstlist)
            print("x:", x," gefunden, entfernt")
            print("")

            if firstlist == []:
                variantlist.remove([])


            m = 0
            n = 0
            o = 0
            for j in firstlist:
                print("b_1", b_1)
                print(j)
                print("b_2", b_2)
                if (int(j)+15) <= b_2 and (int(j)-15) >= b_1:
                    m += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("m",m)

                elif (int(j) - 15) < b_2:
                    o += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("o",o)
                elif int(j) <= b_2 and int(j) >= b_1:
                    n += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("n",n)
            if m == 0 and n == 0 and o == 0:
                print("alle drei gleich 0")
                continue
            
            while m > 0:
# OPTION 2-1                        int(j)+15 <= b_2 and int(j)-15 >= b_1
                x = firstlist[0]
                out.write("\n")
                out.write("OPTION 2-1")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
            
                print("option 2-1")
            
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                    w = int(x) - b_1 - 1                        # 2 ?????
                    s = w-i
                    print("s",s)
                    print("i", i)
                    y = line[s]
                    print(y)
                    print(line)
                    out.write("{}".format(y))
                firstlist.remove(x)
                print(firstlist)
                print("x:", x," gefunden, entfernt")
                print("")
                if firstlist == []:
                    variantlist.remove([])
                m -= 1    
            
            while o > 0:                    
# OPTION 2-2                                     int(x) - 15 < b_2
                x = firstlist[0]
                print("")
                print("OPTION2-2")
                out.write("\n")
                out.write("OPTION 2-2")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
               
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                a = b_2 - (int(x)-15) + 1
                print(a)
                for i in range(0, a, 1):                 # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden
                    w = int(x) -15 - b_1  - 1
                    #s = b_2 -i
                    s = w + i
                    print("s",s)
                    print("i", i)
                # if s == str(b_2)[-2:len(str(b_2)) ]:
                    # rest = i -1                     #rest = wieviele der 15 zeilen sind in der naechsten zeile?
                    # print("rest", rest)
                    # break
                # if s == l:
                    # rest = i + 16
                    # print("rest", rest)
                    # print("")
                    # break
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
               
                firstlist.remove(x)
                print("firstlist",firstlist)
                print("x:", x," gefunden, entfernt")
                print("")

                if firstlist == []:
                    variantlist.remove([])
               
                o -= 1
                print(line)
                
                
            while n > 0:
# OPTION 2-3                            int(x) <= b_2 and int(x) >= b_1
                x = firstlist[0]
                out.write("\n")
                out.write("OPTION 2-3")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
                print("option 1-2")
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                    w = int(x) - b_1 - 1
                    s = w-i
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
                firstlist.remove(x)
                print(firstlist)
                print("x:", x," gefunden, entfernt")
                print("")

                if firstlist == []:
                    variantlist.remove([])
                n -= 1


            print("statuspunkt 1")
           
                    
           elif int(x) > b_2:
# OPTION 3
              seq = ""
              print("OPTION3")
              out.write("\n")
              out.write("OPTION 3")
              out.write("\n")
              out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
              
              sameline = 0
              seq = ""
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
            
              print("b1",b_1)
              print("x-15", int(x)-15)
              print("x", x)
              print("x+15", int(x)+15)
              print("b2",b_2)
              a = b_2 - (int(x)-15) + 1
              print(a)
              for i in range(0, a, 1):                 # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden
                
                w = int(x) -15 - b_1  - 1
                #s = b_2 -i
                s = w + i
                print("s",s)
                print("i", i)
                # if s == str(b_2)[-2:len(str(b_2)) ]:
                    # rest = i -1                     #rest = wieviele der 15 zeilen sind in der naechsten zeile?
                    # print("rest", rest)
                    # break
                # if s == l:
                    # rest = i + 16
                    # print("rest", rest)
                    # print("")
                    # break
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
              
              t = []
              for i in range (1, sameline + 1,1):
                
                t.append(firstlist[i])
                print(t)
                diff = int(firstlist[i]) - int(x)
                print(diff)
                newseq = seq[diff:len(seq)]
                out.write("\n")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, firstlist[i], (int(firstlist[i])-15),(int(firstlist[i])+15)))
                out.write("{}".format(newseq))

                
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
              print("firstlist", firstlist)
              for i in t:
                print("i in t", i)
                firstlist.remove(i)
                print("i:", i, "gefunden, entfernt")
              print("firstlist",firstlist)
              print("x:", x," gefunden, entfernt")
              print("")

              if firstlist == []:
                variantlist.remove([])
                
                
              m = 0
              n = 0
              o = 0
              for j in firstlist:
                print("b_1", b_1)
                print(j)
                print("b_2", b_2)
                print("")
                if j == x:
                    out.write("\n")
                    out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
                    out.write("{}".format(seq))
                    print("j == x")
                    print(firstlist)
                    firstlist.remove(x)
                    print(firstlist)
                    print("x:", x, "gefunden,entfernt")
                    print("")
                    
                elif (int(j)+15) <= b_2 and (int(j)-15) >= b_1:
                    m += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("m",m)
                elif (int(j) - 15) < b_2:
                    o += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("o",o)
                elif int(j) <= b_2 and int(j) >= b_1:
                    n += 1
                    print(b_1)
                    print(j)
                    print(b_2)
                    print("n",n)

              if m == 0 and n == 0 and o == 0:
                print("alle drei gleich 0")
                continue
            
              while m > 0:
# OPTION 3-1                        int(j)+15 <= b_2 and int(j)-15 >= b_1
                x = firstlist[0]
                out.write("\n")
                out.write("OPTION 3-1")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
            
                print("option 3-1")
            
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                    w = int(x) - b_1 - 1                        # 2 ?????
                    s = w-i
                    print("s",s)
                    print("i", i)
                    y = line[s]
                    print(y)
                    print(line)
                    out.write("{}".format(y))
                firstlist.remove(x)
                print(firstlist)
                print("x:", x," gefunden, entfernt")
                print("")
                if firstlist == []:
                    variantlist.remove([])
                m -= 1    
            
              
              while o > 0:                    
# OPTION 3-2                                     int(x) - 15 < b_2
                x = firstlist[0]
                print("OPTION3-2")
                out.write("\n")
                out.write("OPTION 3-2")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
               
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                a = b_2 - (int(x)-15) + 1
                print(a)
                for i in range(0, a, 1):                 # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden
                    w = int(x) -15 - b_1  - 1
                    #s = b_2 -i
                    s = w + i
                    print("s",s)
                    print("i", i)
                # if s == str(b_2)[-2:len(str(b_2)) ]:
                    # rest = i -1                     #rest = wieviele der 15 zeilen sind in der naechsten zeile?
                    # print("rest", rest)
                    # break
                # if s == l:
                    # rest = i + 16
                    # print("rest", rest)
                    # print("")
                    # break
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
               
                firstlist.remove(x)
                print("firstlist",firstlist)
                print("x:", x," gefunden, entfernt")
                print("")

                if firstlist == []:
                    variantlist.remove([])
               
                o -= 1
                print(line)
              
              while n > 0:
# OPTION 3-3                            int(x) <= b_2 and int(x) >= b_1
                seq = ""
                x = firstlist[0]
                out.write("\n")
                out.write("OPTION 3-3")
                out.write("\n")
                out.write("> {} |{} |{} |{}:{} \n".format(name_sample, chr_list, x, (int(x)-15),(int(x)+15)))
                print("option 3-3")
                print("b1",b_1)
                print("x-15", int(x)-15)
                print("x", x)
                print("x+15", int(x)+15)
                print("b2",b_2)
                for i in range(15, -16, -1):                   # alle 15 zeichen vor snp eintragen, falls in der zeile vorhanden

                    w = int(x) - b_1 - 1
                    s = w-i
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
                    seq = seq + y
                    print(y)
                    print(line)

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
                        seq = seq + y
                        print(y)
                        print(line)
                        out.write("{}".format(y))
                firstlist.remove(x)
                print(firstlist)
                print("x:", x," gefunden, entfernt")
                print("")

                if firstlist == []:
                    variantlist.remove([])
                n -= 1


 
           print("statuspunkt 2")

    out.close()



read_fasta()


def insert_snps():
    print("insert SNPs")
    out = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_SNP_sequences.fa".format(name_sample,name_sample), "r")
    sequences = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_SNP_sequences_output.fa".format(name_sample,name_sample), "w")
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
            #print(end)
            sequences.write("{}".format(line[0:15]))
            #print(line[0:15])
            #print("baselist")
            #print(baselist)
            #sequences.write("baselist: {}".format(baselist))
            #print("")
            l = len(baselist[0][0])
            #print(l)
            #print(baselist[0])
            #print(baselist[0][0])
            sequences.write("{}{}\n".format((baselist[0][1]), line[15+l:len(line)]))
            #print(baselist[0][1])
            #print(line[15+l:len(line)])
            h = baselist[0]
            baselist.remove(h)
            
                
    sequences.close()    

insert_snps()