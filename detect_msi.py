import subprocess
import sys


mantis = "/home/lea/MANTIS/mantis.py"

bedfile = sys.argv[1]

genome = sys.argv[2]

normal = sys.argv[3]

tumor = sys.argv[4]

output = sys.argv[5]

#exome_parameters = " -mrq 20 -mlq 25 -mlc 20 -mrr 1"
mrq = "20"
mlq = "25"
mlc = "20"
mrr = "1"


subprocess.run(["python", mantis, "--bedfile", bedfile, "--genome", genome, "-n", normal, "-t", tumor, "-o", output, "-mrq", mrq, "-mlq", mlq, "-mlc", mlc, "-mrr", mrr])



