

# isinstance(objektname,Klassenname

class Sequence_variant():
	def __init__(self, vtype, vcount, vname):
		self.vtype = vtype
		self.vcount = vcount
		self.vname = vname

class Functional_effect_variant(Sequence_variant):
	pass
function_uncertain_variant = Functional_effect_variant("function_uncertain_variant", 0, "function uncertain variant")
functionally_normal = Functional_effect_variant("functionally_normal", 0, "functionally normal")
functionally_abnormal = Functional_effect_variant("functionally_abnormal", 0, "functionally abnormal")

class Functionally_abnormal(Functional_effect_variant):
	pass
loss_of_function_variant = Functionally_abnormal("loss_of_function_variant", 0, "loss of function variant")
dominant_negative_variant = Functionally_abnormal("dominant_negative_variant", 0, "dominant negative variant")
loss_of_heterozygosity = Functionally_abnormal("loss_of_heterozygosity", 0, "loss of heterozygosity")
translational_product_function_variant = Functionally_abnormal("translational_product_function_variant", 0, "translational product function variant")
transcript_function_variant = Functionally_abnormal("transcript_function_variant", 0,"transcript function variant")
gain_of_function_variant = Functionally_abnormal("gain_of_function_variant", 0, "gain of function variant")
null_mutation = Functionally_abnormal("null_mutation", 0, "null mutation")
lethal_variant = Functionally_abnormal("lethal_variant", 0, "lethal variant")

class Transcript_function_variant(Functionally_abnormal):
	pass
transcript_processing_variant = Transcript_function_variant("transcript_processing_variant", 0, "transcript processing variant")
level_of_transcript_variant = Transcript_function_variant("level_of_transcript_variant", 0, "level of transcript variant")
transcription_variant = Transcript_function_variant("transcription_variant", 0, "transcription variant")
transcript_stability_variant = Transcript_function_variant("transcript_stability_variant", 0, "transcript stability variant")

class Transcription_variant(Transcript_function_variant):
	pass
rate_of_transcription_variant = Transcription_variant("rate_of_transcription_variant", 0, "rate of transcription variant")

class Rate_of_transcription_variant(Transcription_variant):
	pass


class Transcript_stability_variant(Transcript_function_variant):
	pass
decreased_transcript_stability_variant = Transcript_stability_variant("decreased_transcript_stability_variant", 0, "decreased transcript stability variant")
increased_transcript_stability_variant = Transcript_stability_variant("increased_transcript_stability_variant", 0, "increased transcript stability variant")


class Structural_variant(Sequence_variant):
	pass

feature_amplification = Structural_variant("feature_amplification", 0, "feature amplification")
feature_fusion = Structural_variant("feature_fusion", 0, "feature fusion")
feature_ablation = Structural_variant("feature_ablation", 0, "feature ablation")
sequence_length_variant = Structural_variant("sequence_length_variant", 0, "sequence length variant")
feature_variant = Structural_variant("feature_variant", 0, "feature variant")
feature_translocation = Structural_variant("feature_variant", 0, "feature variant")

class Feature_amplification(Structural_variant):
	pass
regulatory_region_amplification = Feature_amplification("Regulatory_variant", 0, "Regulatory variant")
transcript_amplification = Feature_amplification("transcript_amplification", 0, "transcript amplification")

class Regulatory_region_amplification(Feature_amplification):
	pass
tfbs_amplification = Regulatory_region_amplification("tfbs_amplification", 0, "TFBS amplification")

class Feature_fusion(Structural_variant):
	pass
transcript_fusion = Feature_fusion("transcript_fusion", 0, "transcript fusion")
regulatory_region_fusion = Feature_fusion("regulatory_region_fusion", 0, "regulatory region fusion")
gene_fusion = Feature_fusion("gene_fusion", 0, "gene fusion")
transcript_regulatory_region_fusion = Feature_fusion("transcript_regulatory_region_fusion", 0, "transcript regulatory region fusion")

class Regulatory_region_fusion(Feature_fusion):
	pass
tfbs_fusion = Regulatory_region_fusion("tfbs_fusion", 0, "TFBS fusion")

class Feature_ablation(Structural_variant):
	pass
transcript_ablation = Feature_ablation("transcript_ablation", 0, "transcript ablation")
regulatory_region_ablation = Feature_ablation("regulatory_region_ablation", 0, "regulatory region ablation")

class Regulatory_region_ablation(Feature_ablation):
	pass
tfbs_ablation = Regulatory_region_ablation("tfbs_ablation", 0, "TFBS ablation")

class Feature_translocation(Structural_variant):
	pass
regulatory_region_translocation = Feature_translocation("regulatory_region_translocation", 0, "regulatory region translocation")
transcript_translocation = Feature_translocation("transcript_translocation", 0, "transcript translocation")

class Regulatory_region_translocation(Feature_translocation):
	pass
tfbs_translocation = Regulatory_region_translocation("tfbs_translocation", 0, "TFBS translocation")

class Sequence_length_variant(Structural_variant):
	pass
short_tandem_repeat_change = Sequence_length_variant("short_tandem_repeat_change", 0, "short tandem repeat change")
copy_number_change = Sequence_length_variant("copy_number_change", 0, "copy number change")

class Copy_number_change(Sequence_length_variant):
	pass
copy_number_increase = Copy_number_change("copy_number_increase", 0, "copy number increase")
copy_number_decrease = Copy_number_change("copy_number_increase", 0, "copy number increase")

class Short_tandem_repeat_change(Sequence_length_variant):
	pass
short_tandem_repeat_expansion = Short_tandem_repeat_change("short_tandem_repeat_expansion", 0, "short tandem repeat expansion")
short_tandem_repeat_contraction = Short_tandem_repeat_change("short_tandem_repeat_contraction", 0, "short tandem repeat contraction")

class Short_tandem_repeat_expansion(Short_tandem_repeat_change):
	pass
trinucleotide_repeat_expansion = Short_tandem_repeat_expansion("trinucleotide_repeat_expansion", 0, "trinucleotide repeat expansion")

class Feature_variant(Structural_variant):
	pass
intergenic_variant = Feature_variant("intergenic_variant", 0, "intergenic variant")
feature_elongation = Feature_variant("feature_elongation", 0, "feature_elongation")
gene_variant = Feature_variant("gene_variant", 0, "gene variant")
regulatory_region_variant = Feature_variant("regulatory_region_variant", 0, "regulatory region variant")
feature_truncation = Feature_variant("feature_truncation", 0, "feature truncation")
silent_mutation = Feature_variant("silent_mutation", 0, "silent mutation")

class Feature_truncation(Feature_variant):
	pass
stop_gained = Feature_truncation("stop_gained", 0, "stop gained") ####
frameshift_truncation = Feature_truncation("frameshift_truncation", 0, "frameshift truncation")
inframe_deletion = Feature_truncation("inframe_deletion", 0, "inframe deletion")

class Inframe_deletion(Feature_truncation):
	pass
disruptive_inframe_deletion = Inframe_deletion("disruptive_inframe_deletion", 0, "disruptive inframe deletion")
conservative_inframe_deletion = Inframe_deletion("conservative_inframe_deletion", 0, "conservative inframe deletion")

class Regulatory_region_variant(Feature_variant, Feature_translocation):
	pass
tf_binding_site_variant = Regulatory_region_variant("tf_binding_site_variant", 0, "TF binding site variant")

class Feature_elongation(Feature_variant):
	pass
stop_lost = Feature_elongation("stop_lost", 0, "stop lost")
internal_feature_elongation = Feature_elongation("internal_feature_elongation", 0, "internal feature elongation")

class Internal_feature_elongation(Feature_elongation):
	pass
frameshift_elongation = Internal_feature_elongation("frameshift_elongation", 0, "frameshift elongation")
inframe_insertion = Internal_feature_elongation("inframe_insertion", 0, "inframe insertion")

class Intergenic_variant(Feature_variant):
	pass
downstream_gene_variant = Intergenic_variant("downstream_gene_variant", 0, "downstream gene variant")
intergenic_1kb_variant = Intergenic_variant("intergenic_1kb_variant", 0, "intergenic 1kb variant")
upstream_transcript_variant = Intergenic_variant("upstream_transcript_variant", 0, "upstream transcript variant")
conserved_intergenic_variant = Intergenic_variant("conserved_intergenic_variant", 0, "conserved intergenic variant")
upstream_gene_variant = Intergenic_variant("upstream_gene_variant", 0, "upstream gene variant")
downstream_transcript_variant = Intergenic_variant("downstream_transcript_variant", 0, "downstream transcript variant")

class Upstream_gene_variant(Intergenic_variant):
	pass
two_kb_upstream_variant = Upstream_gene_variant("2kb_upstream_variant", 0, "2kb upstream variant")
five_kb_upstream_variant = Upstream_gene_variant("5kb_upstream_variant", 0, "5kb upstream variant")

class Downstream_gene_variant(Intergenic_variant):
	pass
two_kb_downstream_variant = Downstream_gene_variant("2kb_downstream_variant", 0, "2kb downstream variant")
five_kb_downstream_variant = Downstream_gene_variant("5kb_downstream_variant", 0, "5kb downstream variant")
fivehundred_b_downstream_variant = Downstream_gene_variant("500b_downstream_variant", 0, "500b downstream variant")

class Gene_variant(Feature_variant):
	pass
genic_downstream_transcript_variant = Gene_variant("genic_downstream_transcript_variant", 0, "genic downstream transcript variant")
transcript_variant = Gene_variant("transcript_variant" ,0, "transcript variant")
gene_fusion = Gene_variant("gene_fusion", 0, "gene fusion")
genic_upstream_transcript_variant = Gene_variant("genic_upstream_transcript_variant", 0, "genic upstream transcript variant")
translational_product_structure_variant = Gene_variant("translational_product_structure_variant", 0, "translational product structure variant")

class Gene_fusion(Gene_variant):
	pass
unidirectional_gene_fusion = Gene_fusion("unidirectional_Gene_fusion", 0, "unidirectional Gene fusion")
bidirectional_gene_fusion = Gene_fusion("bidirectional_gene_fusion", 0, "bidirectional gene fusion")

class Translational_product_structure_variant(Gene_variant):
	pass
polypeptide_sequence_variant = Translational_product_structure_variant("polypeptide_sequence_variant", 0, "polypeptide sequence variant")

class Polypeptide_sequence_variant(Translational_product_structure_variant):
	pass
amino_acid_deletion = Polypeptide_sequence_variant("amino_acid_deletion", 0, "amino-acid deletion")
polypeptide_truncation = Polypeptide_sequence_variant("polypeptide_truncation", 0, "polypeptide truncation")
polypeptide_fusion = Polypeptide_sequence_variant("polypeptide_fusion", 0, "polypeptide_fusion")
amino_acid_insertion = Polypeptide_sequence_variant("amino_acid_insertion", 0, "amino-acid insertion")
elongated_polypeptide = Polypeptide_sequence_variant("elongated_polypeptide", 0, "elongated polypeptide")
amino_acid_substitution = Polypeptide_sequence_variant("amino_acid_substitution", 0, "amino-acid substitution")

class Elongated_polypeptide(Polypeptide_sequence_variant):
	pass
elongated_polypeptide_c_terminal = Elongated_polypeptide("elongated_polypeptide_c_terminal", 0, "elongated polypeptide C-terminal")
elongated_polypeptide_n_terminal = Elongated_polypeptide("elongated_polypeptide_n_terminal", 0, "elongated polypeptide N-terminal")

class Elongated_polypeptide_n_terminal(Elongated_polypeptide):
	pass
elongated_in_frame_polypeptide_n_terminal = Elongated_polypeptide_n_terminal("elongated_in_frame_polypeptide_n_terminal", 0, "elongated in frame polypeptide N-terminal")
elongated_out_of_frame_polypeptide_n_terminal = Elongated_polypeptide_n_terminal("elongated_out_of_frame_polypeptide_n_terminal", 0, "elongated out of frame polypeptide N-terminal")

class Elongated_polypeptide_c_terminal(Elongated_polypeptide):
	pass
elongated_in_frame_polypeptide_c_terminal = Elongated_polypeptide_n_terminal("elongated_in_frame_polypeptide_c_terminal", 0, "elongated in frame polypeptide C-terminal")
elongated_out_of_frame_polypeptide_c_terminal = Elongated_polypeptide_n_terminal("elongated_in_frame_polypeptide_c_terminal", 0, "elongated out of frame polypeptide C-terminal")


class Amino_acid_substitution(Polypeptide_sequence_variant):
	pass
non_conservative_amino_acid_substitution = Amino_acid_substitution("non_conservative_amino_acid_substitution", 0, "non conservative amino-acid substitution")
conservative_amino_acid_substitution = Amino_acid_substitution("conservative amino_acid_substitution", 0, "conservative amino-acid substitution")



class Transcript_variant(Gene_variant):
	pass
nmd_transcript_variant = Transcript_variant("nmd_transcript_variant", 0, "NMD transcript variant")
intron_variant = Transcript_variant("intron_variant", 0, "intron variant")
incomplete_transcript_variant = Transcript_variant("incomplete_transcript_variant", 0, "incomplete transcript variant")
intragenic_variant = Transcript_variant("intragenic-variant", 0, "intragenic variant")
non_coding_transcript_variant = Transcript_variant("non_coding_transcript_variant", 0, "non coding transcript variant")
exon_variant = Transcript_variant("exon_variant", 0, "exon variant")
complex_transcript_variant = Transcript_variant("complex_transcript_variant", 0, "complex transcript variant")
coding_transcript_variant = Transcript_variant("coding_transcript_variant", 0, "coding transcript variant")
splicing_variant = Transcript_variant("splicing_variant", 0, "splicing variant")
transcript_secondary_structure_variant = Transcript_variant("transcript_secondary_structure_variant", 0, "transcript secondary structure variant")

class Transcript_secondary_structure_variant(Transcript_variant):
	pass
compensatory_transcript_secondary_structure_variant = Transcript_secondary_structure_variant("compensatory_transcript_secondary_structure_variant", 0, "compensatory transcript secondary structure variant")

class Splicing_variant(Transcript_variant):
	pass
intron_gain_variant = Splicing_variant("intron_gain_variant", 0, "intron gain variant")
splice_polypirimidine_tract_variant = Splicing_variant("splice polypyrimidine tract variant", 0, "splice polypyrimidine tract variant")
extended_intronic_splice_region_variant = Splicing_variant("extended_intronic_splice_region_variant", 0, "extended intronic splice region variant")
exon_loss_variant = Splicing_variant("exon_loss_variant", 0, "exon loss variant")
splice_site_variant = Splicing_variant("splice_site_variant", 0, "splice site variant")
cryptic_splice_site_variant = Splicing_variant("cryptic_splice_site_variant", 0, "cryptic splice site variant")
splice_region_variant = Splicing_variant("splice_region_variant", 0, "splice region variant")

class Splice_region_variant(Splicing_variant):
	pass
splice_donor_region_variant = Splice_region_variant("splice_donor_region_variant", 0, "splice donor region variant")
non_coding_transcript_splice_region_variant = Splice_region_variant("non_coding_transcript_aplice_region_variant", 0, "non coding transcript aplice region variant")
exonic_splice_region_variant = Splice_region_variant("exonic_splice_region_variant", 0, "exonic splice region variant")

class Cryptic_splice_site_variant(Splicing_variant):
	pass
cryptic_splice_acceptor = Cryptic_splice_site_variant("cryptic_splice_acceptor", 0, "cryptic splice acceptor")
cryptic_splice_donor = Cryptic_splice_site_variant("cryptic_splice_donor", 0, "cryptic splice donor")

class Splice_site_variant(Splicing_variant):
	pass
splice_acceptor_variant = Splice_site_variant("splice_acceptor_variant", 0, "splice acceptor variant")
splice_donor_5th_base_variant = Splice_site_variant("splice_donor_5th_base_variant", 0, "splice donor 5th base variant")
splice_donor_variant = Splice_site_variant("splice_donor_variant", 0, "splice donor variant")

class Coding_transcript_variant(Transcript_variant):
	pass
coding_transcript_intron_variant = Coding_transcript_variant("coding_transcript_intron_variant", 0, "coding transcript intron variant")
coding_sequence_variant = Coding_transcript_variant("coding_sequence_variant", 0, "coding sequence variant")
utr_variant = Coding_transcript_variant("utr_variant", 0, "UTR variant")

class Coding_transcript_intron_variant(Coding_transcript_variant):
	pass
five_prime_utr_intron_variant = Coding_transcript_intron_variant("five_prime_utr_intron_variant", 0, "5 prime UTR intron variant")
three_prime_utr_intron_variant = Coding_transcript_intron_variant("three_prime_utr_intron_variant", 0, "3 prime UTR intron variant") #####

class Non_coding_transcript_variant(Transcript_variant):
	pass
non_coding_transcript_splice_region_variant = Non_coding_transcript_variant("non_coding_transcript_splice_region_variant", 0, "non coding transcript splice region variant")
non_coding_transcript_exon_variant = Non_coding_transcript_variant("non_coding_transcript_exon_variant", 0, "non coding transcript exon variant")
mature_miRNA_variant = Non_coding_transcript_variant("mature_mirna_variant", 0, "mature miRNA variant")
non_coding_transcript_intron_variant = Non_coding_transcript_variant("non_coding_transcript_intron_variant",0, "non coding transcript intron variant")

class Incomplete_transcript_variant(Transcript_variant):
	pass
incomplete_transcript_splice_region_variant = Incomplete_transcript_variant("incomplete_transcript_splice_region_variant", 0, "incomplete transcript splice region variant")
incomplete_transcript_exonic_variant = Incomplete_transcript_variant("incomplete_transcript_exonic_variant", 0, "incomplete transcript exonic variant")
incomplete_transcript_5UTR_variant = Incomplete_transcript_variant("incomplete_transcript_5_UTR_variant", 0, "incomplete transcript 5 UTR variant")
incomplete_transcript_intronic_variant = Incomplete_transcript_variant("incomplete_transcript_intronic_variant", 0, "incomplete transcript intronic variant")
incomplete_transcript_CDS = Incomplete_transcript_variant("incomplete_transcript_CDS", 0, "incomplete transcript CDS")
incomplete_transcript_3UTR_variant = Incomplete_transcript_variant("incomplete_transcript_3_UTR_variant", 0, "incomplete transcript 3 UTR variant")

class Incomplete_transcript_splice_region_variant(Incomplete_transcript_variant):
	pass
incomplete_transcript_coding_splice_variant = Incomplete_transcript_splice_region_variant("incomplete_transcript_coding_splice_variant", 0, "incomplete transcript coding splice variant")


class Intron_variant(Transcript_variant):
	pass
coding_transcript_intron_variant = Intron_variant("coding_transcript_intron_variant", 0, "coding transcript intron variant")
splice_site_variant = Intron_variant("splice_site_variant", 0, "splice site variant")
conserved_intron_variat = Intron_variant("conserved_intron_variant", 0, "conserved intron variant")
non_coding_transcript_intron_variant = Intron_variant("non_coding_transcript_intron_variant", 0, "non coding transcript intron variant")

class Splice_site_variant(Intron_variant):
	pass
splice_acceptor_variant = Splice_site_variant("splice_acceptor_variant", 0, "splice acceptor variant")
splice_donor_5th_base_variant = Splice_site_variant("splice_donor_5th_base_variant", 0, "splice donor 5th base variant")
splice_donor_variant = Splice_site_variant("splice_donor_variant", 0, "splice donor variant")

class Coding_transcript_intron_variant(Intron_variant):
	pass
five_prime_utr_intron_variant = Coding_transcript_intron_variant("5_prime_utr_intron_variant", 0, "5 prime UTR intron variant")
three_prime_utr_intron_variant = Coding_transcript_intron_variant("3_prime_utr_intron_variant", 0, "3 prime utr intron variant")#####

class Coding_transcript_variant(Transcript_variant):
	pass
class Exon_variant(Transcript_variant):
	pass
coding_sequence_variant = Exon_variant("coding_sequence_variant", 0, "coding sequence variant")
non_coding_transcript_exon_variant = Exon_variant("non_coding_transcript_exon_variant", 0, "non coding transcript exon variant")
utr_variant = Exon_variant("utr_variant", 0, "UTR variant")

class Non_coding_transcript_exon_variant(Exon_variant, Coding_transcript_variant):
	pass


class Utr_variant(Exon_variant, Coding_transcript_variant):
	pass
three_prime_utr_variant = Utr_variant("3_prime_UTR_variant", 0, "3 prime UTR variant")
five_prime_utr_variant = Utr_variant("5_prime_UTR_variant", 0, "5 prime UTR variant")


class Three_prime_utr_variant(Utr_variant):
	pass
three_prime_utr_elongation = Three_prime_utr_variant("3_prime_utr_elongation", 0,"3 prime utr elongation")
three_prime_utr_exon_variant = Three_prime_utr_variant("3_prime_utr_exon_variant", 0, "3 prime utr exon variant")
three_prime_utr_intron_variant = Three_prime_utr_variant("3_prime_utr_intron_variant", 0, "3 prime utr intron variant")
three_prime_utr_truncation = Three_prime_utr_variant("3_prime_UTR_truncation", 0,"3 prime UTR truncation")

class Five_prime_utr_variant(Utr_variant):
	pass

five_prime_utr_elongation = Five_prime_utr_variant("5_prime_utr_elongation", 0, "5 prime UTR elongation")
five_prime_utr_premature_start_codon_variant = Five_prime_utr_variant("5_prime_utr_premature_start_codon_variant", 0, "5 prime UTR premature start codon variant")
five_prime_UTR_exon_variant = Five_prime_utr_variant("5_prime_utr_exon_variant", 0, "5 prime UTR exon variant")
five_prime_utr_truncation = Five_prime_utr_variant("5_prime_utr_truncation", 0, "5 prime UTR truncation")

class Five_prime_utr_premature_start_codon_variant(Five_prime_utr_variant):
	pass
five_prime_utr_premature_start_codon_gain_variant = Five_prime_utr_premature_start_codon_variant("5_prime_utr_premature_start_codon_gain_variant", 0, "5 prime UTR premature start codon gain variant")
five_prime_utr_premature_start_codon_loss_variant = Five_prime_utr_premature_start_codon_variant("5_prime_utr_premature_start_codon_loss_variant", 0, "5 prime UTR premature start codon loss variant")

five_prime_utr_premature_start_codon_location_variant = Five_prime_utr_premature_start_codon_variant("5_prime_utr_premature_start_codon_location_variant", 0, "5 prime UTR premature start codon location variant")

class Coding_sequence_variant(Exon_variant, Coding_transcript_variant):
	pass
protein_altering_variant = Coding_sequence_variant("protein_altering_variant", 0, "protein altering variant")
initiator_codon_variant = Coding_sequence_variant("initiator_codon_variant", 0, "initiator codon variant")
terminator_codon_variant = Coding_sequence_variant("terminator_codon_variant", 0, "terminator codon variant")
synonymous_variant = Coding_sequence_variant("synonymous_variant", 0, "synonymous variant")

class Synonymous_variant(Coding_sequence_variant):
	pass
start_retained_variant = Synonymous_variant("start_retained_variant", 0, "start retained variant")
stop_retained_variant = Synonymous_variant("stop_retained_variant", 0, "stop retained variant")



class Terminator_codon_variant(Coding_sequence_variant):
	pass
#stop_retained_variant = Terminator_codon_variant("stop retained variant", 0)
#stop_lost = Terminator_codon_variant("stop lost", 0)
#incomplete_terminal_codon_variant = Terminator_codon_variant("incomplete terminal codon variant", 0)

class Initiator_codon_variant(Coding_sequence_variant):
	pass
#start_retained_variant = Initiator_codon_variant("start retained variant", 0)
#start_lost = Initiator_codon_variant("start lost", 0)

class Protein_altering_variant(Coding_sequence_variant):
	pass
frameshift_variant = Protein_altering_variant("frameshift_variant", 0, "frameshift variant")
inframe_variant = Protein_altering_variant("inframe_variant", 0, "inframe variant")

class Frameshift_variant(Protein_altering_variant):
	pass
plus_1_frameshift_variant = Frameshift_variant("plus_1_frameshift_variant", 0, "plus 1 frameshift variant")
minus_1_frameshift_variant = Frameshift_variant("minus_1_frameshift_variant", 0, "minus 1 frameshift variant")
plus_2_frameshift_variant = Frameshift_variant("plus_2_frameshift_variant", 0, "plus 2 frameshift variant")
minus_2_frameshift_variant = Frameshift_variant("minus_2_frameshift_variant", 0, "minus 2 frameshift variant")
frameshift_truncation = Frameshift_variant("frameshift_truncation", 0, "frameshift truncation")
frameshift_elongation = Frameshift_variant("frameshift_elongation", 0, "frameshift elongation")
frame_restoring_variant = Frameshift_variant("frame_restoring_variant", 0, "frame restoring variant")

class Inframe_variant(Protein_altering_variant):
	pass
nonsynonymous_variant = Inframe_variant("nonsynonymous_variant", 0, "nonsynonymous variant")
inframe_indel = Inframe_variant("inframe_indel", 0, "inframe indel")
incomplete_terminal_codon_variant = Inframe_variant("incomplete_terminal_codon_variant", 0, "incomplete terminal codon variant")

class Incomplete_terminal_codon_variant(Inframe_variant, Terminator_codon_variant):
	pass

class Inframe_indel(Inframe_variant):
	pass
inframe_deletion = Inframe_indel("inframe_deletion", 0, "inframe deletion")
inframe_insertion = Inframe_indel("inframe_insertion", 0, "inframe insertion")

class Inframe_deletion(Inframe_indel, Feature_truncation):
	pass
conservative_inframe_deletion = Inframe_deletion("conservative_inframe_deletion", 0, "conservative inframe deletion")
disruptive_inframe_deletion = Inframe_deletion("disruptive_inframe_deletion", 0, "disruptive inframe deletion")

class Inframe_insertion(Inframe_indel, Internal_feature_elongation):
	pass
conservative_inframe_insertion = Inframe_insertion("conservative_inframe_insertion", 0, "conservative inframe insertion")
disruptive_inframe_insertion = Inframe_insertion("disruptive_inframe_insertion", 0, "disruptive inframe insertion")

class Nonsynonymous_variant(Inframe_variant):
	pass
missense_variant = Nonsynonymous_variant("missense_variant", 0, "missense variant")
start_lost = Nonsynonymous_variant("start_lost", 0, "start lost")
stop_lost = Nonsynonymous_variant("stop_lost", 0, "stop lost")
stop_gained = Nonsynonymous_variant("stop_gained", 0, "stop gained")
redundant_inserted_stop_gained = Nonsynonymous_variant("redundant_inserted_stop_gained", 0, "redundant inserted stop gained")


class Start_lost(Nonsynonymous_variant, Initiator_codon_variant):
	pass

class Stop_lost(Nonsynonymous_variant, Feature_elongation, Terminator_codon_variant):
	pass

class Stop_gained(Nonsynonymous_variant, Feature_truncation):
	pass

class Redundant_inserted_stop_gained(Nonsynonymous_variant):
	pass


class Missense_variant(Nonsynonymous_variant):
	pass
conservative_missense_variant = Missense_variant("conservative_missense_variant", 0, "conservative missense variant")
non_conservative_missense_variant = Missense_variant("non_conservative_missense_variant", 0, "non conservative missense variant")

class Conservative_missense_variant(Missense_variant):
	pass
class Non_conservative_missense_variant(Missense_variant):
	pass





#print(nonsynonymous_variant.vtype)


nonsynonymous = [[nonsynonymous_variant.vtype, nonsynonymous_variant.vcount], [missense_variant.vtype, missense_variant.vcount], [start_lost.vtype, start_lost.vcount], [stop_lost.vtype, stop_lost.vcount], [stop_gained.vtype, stop_gained.vcount], [redundant_inserted_stop_gained.vtype, redundant_inserted_stop_gained.vcount]]

synonymous = [[synonymous_variant.vtype, synonymous_variant.vcount], [start_retained_variant.vtype, start_retained_variant.vcount], [stop_retained_variant.vtype, stop_retained_variant.vcount]]




