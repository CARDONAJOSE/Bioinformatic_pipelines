#Attention pour travailler il faut la version de python 3.7
''' cette archive se base en l'iteration et extraction des données comment nom, position reference etc'''
#!pip install pyvcf pysam


#Lecture de archives VCF

import vcf

vcf_reader = vcf.Reader(open('example.vcf', 'r'))

for record in vcf_reader:
    print(record.CHROM, record.POS, record.ID, record.REF, record.ALT)



# Lecture archives BAM

import pysam

samfile = pysam.AlignmentFile("example.bam", "rb")

for read in samfile.fetch():
    print(read.query_name, read.reference_start, read.mapping_quality)

samfile.close()


#visualitation de donnée biologique


from Bio.Graphics import GenomeDiagram
from reportlab.lib import colors
from reportlab.lib.units import cm

gd_diagram = GenomeDiagram.Diagram("Example Diagram")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

# Add a feature to show with a label
feature = SeqFeature(FeatureLocation(100, 200), strand=+1)
gd_feature_set.add_feature(feature, name="Example Feature", label=True, color=colors.red)

gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm, 20*cm), start=0, end=200, circle_core=0.7)
gd_diagram.write("genome_plot.pdf", "PDF")