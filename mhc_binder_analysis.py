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
    
    HLA_molecules = peptides.readline()
    number_HLA_molecules = len(HLA_molecules.split())
    print(HLA_molecules)
    print(number_HLA_molecules)
    
    header = peptides.readline()
    print(header)
    
    while line != "":

        line = peptides.readline()
        #number_MHC_molecules = len(line)
        if line == "":
            break
        #print(line)
        data = line.split()
        position = data[0]
        peptide_ID = data[1]
        n_binders = data[len(data)-1]
        h_avg_ranks = data[len(data)-2]
        

        print("")
        print("alle die binden")
        if data[len(data)-1] != "0":
            print(line)
            print("N_binders", data[len(data)-1])
            print("")
        
        
        


detect_binders()
	
