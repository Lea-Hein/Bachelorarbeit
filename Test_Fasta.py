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
            
            if last_chr != chromosome:
                variantlist.append([chromosome, position])
            else:
                l = len(variantlist)
                variantlist[l-1].append(position)
    print(variantlist)






def read_fasta():

    read_vcf()

    x = 23219597
   # print("searched position:", x)
    b_2 = 0
    b_1 = 0
    l = 0
    line = "fastaline"
    
    name_vcf = str(sys.argv[2])
    name_sample = name_vcf[name_vcf.index("DX"):name_vcf.rindex("DX") + (name_vcf.rindex("DX") - name_vcf.index("DX"))-1]
    out = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}_SNP_sequences.fa".format(name_sample), "w")
    print(name_sample)
    print("")
    
    while line != "":
        line = str(fasta.readline())                    # Zeile a
        print("beginn / nach break")
        print(line)
        if line == "":
           break
        if line[0] == ">":
            print(line)                                 # selbe Zeile wie a
            print("number of bases:", b_2)
            b_2 = 0    
            chr_fa = line[1:5]
            print(variantlist)
            for v in variantlist:
                chromosome = v[0]
         #   print(variantlist)
          #  print(chr_fa)
                if chr_fa == chromosome:
                    print(v)
                    i = variantlist.index(v)
                    print(i)
                    print("Test")
                    print(v[i])
                    v.remove(chromosome)
                    v.insert(0,2340)
                    print(v)
                    print(variantlist)
            chromosome = chr_fa
      #  line = str(fasta.readline())
        print("Zeile1")
        print(line)                                     # selbe Zeile wie a
       # line = str(fasta.readline())
        while line != "":
       # print("TEST1")
        #print(line)
        #print("")
            line = str(fasta.readline())
            print(line)                                 # neu, zeile b
            if line[0] == ">":
                print("naechstes Chromosom?")
                print(line)
                break
        #print("Zeile2")
        #print(line)
      #  print("TEST2")
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
       # print("B_1:")
       # print(b_1)
       # print("x", x)
       # print("B_2")
        #print(b_2)
           # print(b_1)
           # print(b_2)
           # print("")
         #   for x in variantlist[i]:
        #print(variantlist[i])
        #for x in variantlist[i]:
         #   print(x)
            y = variantlist[i]
            
            x = y[0]
            print(y)
            print("B_1")
            print(b_1)
            print("B_2")
            print(b_2)
        #print(x)
            if x <= b_2 and x >= b_1:

                print(chromosome)
                print("basen bis zur letzten zeile")
                print(b_1)
                print("gesuchte Position")
                print(x)
                print("basen inkl dieser zeile")
                print(b_2)
                print(line)
                print(l)

                y = x - b_1
                z = line[y -1]
                print(z)
                variantlist[i].remove(x)
                print(variantlist[i])
                print("x gefunden, entfernt")

                out.write(">{} |{} |{}".format(name_sample, chromosome, x))

read_fasta()
