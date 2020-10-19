import sys


def open_netMHC_output():

    global peptides
    peptides = open(sys.argv[1])
    print("")

    return peptides
	
peptides = open_netMHC_output()


def detect_binders():
    global peptides
    line = "peptides"
    # line = peptides.readline()
    # print(line)
    # data = line.split()
    # print(len(data))
    # line = peptides.readline()
    # print(line)
    # data = line.split()
    # print(len(data))
    
    global name_file     # name of the netMHC output file
    global name_sample  # name of the analysed samples
    global HLA_Allele
    name_file = str(sys.argv[1])
    name_file_splitted = name_file.split("_")
    name_sample = name_file[name_file.index("DX"):name_file.rindex("DX") + (name_file.rindex("DX") - name_file.index("DX"))-1]
    HLA_Allele = name_file_splitted[len(name_file_splitted)-1]
    
    global output
    output = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/mantis_test/{}/{}_netMHC_binding_peptides_{}.txt".format(name_sample,name_sample,HLA_Allele), "w")
    
    count = 0 # number of potential binder
    hb_count = 0 # number of strong binder
    
    HLA_molecules = peptides.readline()
    HLA_molecules_splitt = HLA_molecules.split()
    print(HLA_molecules_splitt)
    number_HLA_molecules = len(HLA_molecules.split())
    print(HLA_molecules)
    print(number_HLA_molecules)
    output.write("{}".format(HLA_molecules))
    
    header = peptides.readline()
    print(header)
    output.write("{}".format(header))
    output.write("\n")
    
    while line != "":

        line = peptides.readline()
        #number_MHC_molecules = len(line)
        if line == "":
            break
        #print(line)
        data = line.split()
        position = data[0]
        peptide = data[1]
        ID = data[2]
        n_binders = data[len(data)-1]
        h_avg_ranks = data[len(data)-2]
        

        if data[len(data)-1] != "0":
            count += 1
            

            for i in range(0,number_HLA_molecules):
                # nM_i = data[3 + i * 3]
                # rank_i = data[4 + i * 3]
                # core_i = data[5 + i * 3]
                if float(data[4 + i * 3]) < 0.5:
                    print(line)
  #              output.write("{}\n".format(line))

                    output.write("%rank: {} for {} and {}\n".format(data[4 + i * 3], peptide, HLA_molecules_splitt[i]))
                    output.write("\n")
                    output.write("{}".format(line))
                    output.write("\n")
                    hb_count += 1

    output.write("\n")    
    output.write("nummber of binder: {}".format(count)) 
    output.write("\n")    
    output.write("nummber of strong binder: {}".format(hb_count))    
    print("number of binder:", count)
    print("number of strong binder:", hb_count)


detect_binders()
	
