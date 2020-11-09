
import csv, sys

def open_cnv():

	tsv = sys.argv[1]

	if tsv[len(tsv)-3:len(tsv)] == "tsv":
		tsv = open(sys.argv[1])
	else:
		print("incorrect file type")
		sys.exit(0)
	global name_tsv
	name_tsv = str(sys.argv[1])
	return tsv

cnv = open_cnv()


def tai_calculation(chr_end):
    global start
    global end
    global tai
    if int(start) == 0:
        tai += 1
    if int(end) == chr_end:
        tai += 1

def read_cnv():
    global hrd_loh
    hrd_loh = 0
    global lst
    lst = 0
    global tai
    tai = 0
    
    global start
    global end
    chr_cnv_1 = ""
    end_cnv_1 = 0
    
    r = 0
    distance = 0
    
    cnv_tsv = csv.reader(cnv, delimiter="\t")
    for row in cnv_tsv:
        r += 1
        if str(row)[2] != '#':
# LOH bestimmen
                # number of LOH regions that are bigger than 15MB and smaller than the whole chromosome
			
            state = row[6]
            size = int(row[4])
            cnv_type = row[22]
            
            if state == "LOH":
                if size > 15000000 and cnv_type != "chromosome":
                    hrd_loh += 1

# LST  bestimmen
                # chromosome break between two adjacent regions with 10MB at minimum and aa distance between the regions of 3 MB maximum
            chromosome = row[0]
            start = int(row[1])
            end = int(row[2])
            
            if chromosome == chr_cnv_1:
                distance = start - end_cnv_1
            else: 
                distance = 0
            print("chromosome", chromosome)
            print("chr_alt ", chr_cnv_1)
            print("    size", size)
            print("min size", 10000000) 
            print("    distance", distance)
            print("max distance", 3000000)

            print("end_cnv_alt ", end_cnv_1)
            print("start", start)

            
            if chr_cnv_1 != "" and end_cnv_1 != 0:
                if chromosome == chr_cnv_1 and size >= 10000000:
                    distance = start - end_cnv_1
                    if distance <= 3000000:
                        lst += 1
                        chr_cnv_1 = chromosome                                           ##### warum = 0 ??
                        end_cnv_1 = end
            # if size >= 10000000:
                # chr_cnv_1 = chromosome
                # end_cnv_1 = end
            chr_cnv_1 = chromosome                                       ##### warum = 0 ??
            end_cnv_1 = end
            
                  #      print("")
            print("row", r)
            print("Lst", lst)
            print("")

            
# TAI bestimmen
            # number of allelic imbalances that spread to the ends of the telomer of the chromosome,but do not cross the centromer
            # keine sequenzierung der telomere, test ob "ende" des sequenzierten chromosoms erreicht wurde
            # Daten von NCBI (genome browser, GRCh37)            
            
            chr1_end = 249250621
            chr2_end = 243199373
            chr3_end = 198022430
            chr4_end = 191154276
            chr5_end = 180915260
            chr6_end = 171115067
            chr7_end = 159138663
            chr8_end = 146364022
            chr9_end = 141213431
            chr10_end = 135534747
            chr11_end = 135006516
            chr12_end = 133851895
            chr13_end = 115169878
            chr14_end = 107349540
            chr15_end = 102531392
            chr16_end = 90354753
            chr17_end = 81195210
            chr18_end = 78077248
            chr19_end = 59128983
            chr20_end = 63025520
            chr21_end = 48129895
            chr22_end = 51304566
            chrX_end = 155270560
            chrY_end = 59373566

            if chromosome == "chr1":
                tai_calculation(chr1_end)
            if chromosome == "chr2":
                tai_calculation(chr2_end)
            if chromosome == "chr3":
                tai_calculation(chr3_end)
            if chromosome == "chr4":
                tai_calculation(chr4_end)
            if chromosome == "chr5":
                tai_calculation(chr5_end)
            if chromosome == "chr6":
                tai_calculation(chr6_end)
            if chromosome == "chr7":
                tai_calculation(chr7_end)
            if chromosome == "chr8":
                tai_calculation(chr8_end)
            if chromosome == "chr9":
                tai_calculation(chr9_end)                
            if chromosome == "chr10":
                tai_calculation(chr10_end)                
            if chromosome == "chr11":
                tai_calculation(chr11_end)               
            if chromosome == "chr12":
                tai_calculation(chr12_end)                
            if chromosome == "chr13":
                tai_calculation(chr13_end)               
            if chromosome == "chr14":
                tai_calculation(chr14_end)                
            if chromosome == "chr15":
                tai_calculation(chr15_end)                
            if chromosome == "chr16":
                tai_calculation(chr16_end)                
            if chromosome == "chr17":
                tai_calculation(chr17_end)               
            if chromosome == "chr18":
                tai_calculation(chr18_end)                
            if chromosome == "chr19":
                tai_calculation(chr19_end)                
            if chromosome == "chr20":
                tai_calculation(chr20_end)               
            if chromosome == "chr21":
                tai_calculation(chr21_end)                
            if chromosome == "chr22":
                tai_calculation(chr22_end)                
            if chromosome == "chrX":
                tai_calculation(chrX_end) 
            if chromosome == "chrY":
                tai_calculation(chrY_end)                
               


    print("HRD_LOH = ", hrd_loh)
    print("LST = ", lst)
    print("TAI = ", tai)


def output():
    global name_sample
    name_sample = name_tsv[name_tsv.index("DX"):name_tsv.rindex("DX") + (name_tsv.rindex("DX") - name_tsv.index("DX")) -1]
    read_cnv()
    
    output = open("/mnt/share/evaluations/2020_07_08_AHHeinL1_Neoantigens/Bachelorarbeit_git_repository/Output/{}_Output/{}_Output_HRD_Calculation.txt".format(name_sample, name_sample), "w")
    output.write("Loss of Heterozygosity: {} \n".format(hrd_loh))
    #output.write("\n")
    output.write("Large Scale Transitions: {} \n".format(lst))
    output.write("Telomeric allelic imbalance: {} \n".format(tai))
    
    hrd = hrd_loh + lst + tai
    
    output.write("\n")
    output.write("Homologous Recombination Deficiency Score: {}\n".format(hrd))
    
output()
