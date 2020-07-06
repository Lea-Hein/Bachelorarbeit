
import csv, sys
import Gene_lists

hrgenes_list = Gene_lists.hrgenes_list
resistance_genes_list = Gene_lists.resistance_genes_list

def open_cnv():

	tsv = sys.argv[1]
	#tsv = sys.argv[2]

	if tsv[len(tsv)-3:len(tsv)] == "tsv":
		tsv = open(sys.argv[1])
	else:
		print("incorrect file type")
		sys.exit(0)
	return tsv

tsv = open_cnv()


def read_cnv():

	global size
	global complete_genome
	global cnv
	global deletion
	global amplification
	global loh
	cnv = 0
	deletion = 0
	amplification = 0
	loh = 0
	chromosom = ""
	size = 0
	complete_genome = 3.1 	# GRCh37: chromosome length total 3.1 Gb
	CN_genes = [[" ",0," "]]
	count = 0
	reihe = 0
	c = 0

	read_tsv = csv.reader(tsv, delimiter="\t")
	for row in read_tsv:
		reihe += 1
		
		if str(row)[2] != '#':
			print(row, "\n")
			cnv = cnv + 1			# count number of CNVs
			chromosom = row[0]
			cnv_size = int(row[4])		# size of of the CNV

			size = size + cnv_size		# count number of bases of all CNVS

			state = row[6]			# state of the CNV: Deletion, AMplification, Loss of Heterozygosity
			if state == "DEL":
				deletion += 1
			elif state == "AMP":
				amplification += 1
			elif state == "LOH":
				loh += 1

			genes = (row[25]).split(",")			# affected genes

			for CGI_gene in genes:
				if CGI_gene != "":

				# is affected gene a gene that can result in Resistance to ICB?
					for gene_info in resistance_genes_list:
						for gene_name in gene_info:
							if CGI_gene == gene_name:
								i_tupel = resistance_genes_list.index(gene_info)	
								i_name = 0
								i_count = 1
								i_type = 2
						
								resistance_genes_list[i_tupel][i_count] += 1	
								info = resistance_genes_list[i_tupel]
								info.append(state)


					for gene_info in hrgenes_list:
						for gene_name in gene_info:
							if CGI_gene == gene_name:
								i_tupel = hrgenes_list.index(gene_info)	
								i_name = 0
								i_count = 1
								i_type = 2
						
								hrgenes_list[i_tupel][i_count] += 1	
								info = hrgenes_list[i_tupel]
								info.append(state)

def output():

	read_cnv()

	size_kb = size / 10000	
	size_mb = size / 1000000
	size_gb = size / 1000000000
	cnv_load = size_gb / complete_genome # percentage of the genome that is 'covered' with CNVs

	o = open("CNV_output.txt", "w")

	print(cnv, "Copy number variants:", deletion, "Deletions,", amplification, "Amplifications, ", loh, "Losses of heterozygosity",)
	o.write("{} Copy number variants: 	{}, {} Amplifications, {} Losses of heterozygosity \n".format(cnv, deletion, amplification, loh))
	print("size of all CNVs:", size, "bases =", size_gb, "gb")
	o.write("size of all CNVs: {} bases = {} gb \n".format(size, size_gb))
	print("CNV load:", cnv_load)
	o.write("CNV load: {}\n".format(cnv_load))
	print("\n")
	o.write("\n")

	print("resistance_genes:  \n")

	print(resistance_genes_list)
	o.write("resistance genes: \n")
	o.write("\n")
	for gene_info in resistance_genes_list:
		gene_count = gene_info[1]
		if gene_count > 0:
			gene_name = gene_info[0]
			o.write('{}:	{} Copy number variation \n'.format(gene_name, gene_count))
			


	print("\n")
	o.write("\n")
	print("hrgenes:\n")
	print(hrgenes_list)
	o.write("homologous recombination genes: \n")
	o.write("\n")
	for gene_info in hrgenes_list:
		gene_count = gene_info[1]
		if gene_count > 0:
			gene_name = gene_info[0]
			o.write('{}:	{} Copy number variation \n'.format(gene_name, gene_count))
			


	tsv.close()


# starts the script
#read_cnv()
output()
