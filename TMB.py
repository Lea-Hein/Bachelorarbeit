import gzip, sys


global vcf
global bed
global sequenced_bases


def open_bed():
	bed = open(sys.argv[3])
	return bed

bed = open_bed()


def read_files():

	file = sys.argv[1]
	bed = sys.argv[3]
	

	if file[len(file)-2:len(file)] == "gz":
		vcf = gzip.open(sys.argv[1], 'rt')

	elif file[len(file)-3:len(file)] == "vcf":
		vcf = open(sys.argv[1])

	else:
		print("incorrect file type for the first argument")
		sys.exit(0)
		

	if bed[len(bed)-3:len(bed)] == "bed":
		bed = open(sys.argv[3])

	else:
		print("incorrect file type for the second argument")
		sys.exit(0)
		

	return vcf

vcf = read_files()

# count the number of sequenced bases
def count_bases():
	line = "sequenced"
	sequenced_bases = 0


	while line != "":
		line = bed.readline()
		if line == "":
			break
		data = line.split()
		start = int(data[1]) # sequence start 
		end = int(data[2]) # sequence end
		bases = end - start # number of sequenced bases 
		sequenced_bases = sequenced_bases + bases
	return(sequenced_bases)

sequenced_bases = count_bases()



# read in all variants,line by line
def count_variants():
	line2 = "variant"
	v = 0

	while line2 != "":
		line2 = vcf.readline()			
		if line2 == "":
			break
		if line2[0] != "#": 			
			v += 1				
	return(v)

v = count_variants()


# naive calculation of Tumor Mutational Burden TMB
def TMB():
	#print("TMB =",count_variants()/count_bases())
	print("TMB = ", v/sequenced_bases)

TMB()

bed.close()
vcf.close()

