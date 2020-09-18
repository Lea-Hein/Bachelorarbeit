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



x = "345678"


def read_fasta():

    read_vcf()
   # print("searched position:", x)
    b_2 = 0
    b_1 = 0
    l = 0
    line = "fastaline"
    
    name_vcf = str(sys.argv[2])
    name_sample = name_vcf[name_vcf.index("DX"):name_vcf.rindex("DX") + (name_vcf.rindex("DX") - name_vcf.index("DX"))-1]
    out = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}_SNP_sequences.fa".format(name_sample), "w")
    print(name_sample)

    
    while line != "":
        line = str(fasta.readline())
        if line == "":
            break
        if line[0] == ">":
            print(line)
            print("number of bases:", b_2)
            b_2 = 0    
            chr_fa = line[1:3]
            for v in variantlist:
                chromosome = v[0]
                if chr_fa == v[0]:
                    i = variantlist.index(v)

        if line[0] != ">":
            b_1 = b_2
            l = len(line)-1
            b_2 = b_2 + l
            
           # print(b_1)
           # print(b_2)
           # print("")
            for x in variantlist[i]:

                if x <= b_2 and x >= b_1:
                    print("basen bis zur letzten zeile")
                    print(b_1)
                    print("gesuchte Position")
                    print(x)
                    print("basen inkl dieser zeile")
                    print(b_2)
                    print(line)
            #    print(str(line))
            #    p = []
            #    for i in range(0,len(line)):
            #        p.append(line[i])
            #    print(p)
                    print(l)
            #    print("letzte Base der Zeile",line[l-1])
            #cccccnnnnnnnn    print("vorletzte Base der Zeile", line[l-2])
                    y = x - b_1
                    z = line[y -1]
                    print(z)

                    out.write(">{} |{} |{}".format(name_sample, chromosome, x))
read_fasta()
