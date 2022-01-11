# Characterizing the microbiota of the threatened southern sea otter (_Enhydra lutris nereis_) to enhance conservation practice

This repository contains R version 3.6.1 and python version 3.7.6 implementations of analyses described in:

Dudek, N.K., Switzer, A.D., Costello, E.K., Murray, M.J., Tomoleoni, J.A., Staedler, M.M., Tinker, M.T., Relman, D.A. Characterizing the microbiota of the threatened southern sea otter (_Enhydra lutris nereis_) to enhance conservation practice. In press at Conservation Science and Practice (2022).

Southern sea otters are a threatened keystone sub-species in coastal ecosystems. To understand better the role of diet, monitor health, and enhance management of this and other marine mammal species, we characterized the oral and distal gut microbiota of 158 wild southern sea otters (_Enhydra lutris nereis_) living off the coast of central California, USA, 12 captive sea otters (some of which participated in a diet shift experiment), and 17 otters from three other otter species.

### Data

Sequencing data for this project is available through NCBI BioProject [PRJNA726636](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA726636/). Raw reads for the amplicon survey and the shotgun sequencing analysis were deposited to SRA and are associated with BioSamples SAMN19311023 - SAMN19311742. 

For maximum reproducibility, the following phyloseq objects have been upload to the repo: 
- physeq_lane1.rds represents all samples sequenced on lane 1. All analyses focused on the microbiota of wild sea otters use this phyloseq object
- physeq_spp_compare.rds consists of samples sequenced on lane2. It is used for analyses focused on comparing the distal gut microbiota of different otter species
- physeq_mba_diet.rds consists of samples sequenced on lane2. It is used for analysis of the MBA diet shift experiment

### Installation

For python script: pip install requirements.txt  

### How to run

**To characterize the taxonomic structure of gingival and rectal microbiotas from wild sea otters:**
- community_composition_p1.py: 
  -  For gingival and rectal samples, plots barplot showing taxa on the x-axis and relative abundance in samples on the y-axes (Figure 2A,B)
- community_composition_p2.Rmd: 
  - Plots an ordination of gingival, rectal, and otter-associated seawater samples and performs significance testing (Figure 2C)
  - Plots a Venn diagram showing for sets of gingival, rectal, and otter-associated seawater ASVs (Figure 2D)

**To perform comparisons of the distal gut microbiota of different otter species:**
- spp_comparisons.Rmd: 
  - Plot ordinations of distal gut samples from different otter species (Figures 3, S3)
  - Perform a bootstrap test to investigate whether the average Unifrac distance between distal gut specimens within a species is significantly lower than the average distance between samples from sea otters vs North American river otters
  - Perform differential abundance testing on sea otter vs North American river otter samples to probe how the composition of their microbiotas are distinct

**To investigate the effect of diet on the sea otter microbiota:**
- MBA diet shift experiment - diet_shift.Rmd
  - Plot PCoA of the microbiota structure of captive sea otters before and after a diet intervention (Figures 4B, S4)
  - Perform differential abundance analysis to see which ASVs change in abundance between pre- and post- diet shift states
- Wild sea otters - diet_wild.Rmd
  - Plot PCoA of the microbiota structure of wild sea otters with well characterized diets (Figures 4C, S5)

**To characterize and investigate structure within the gingival microbiota of wild sea otters:**
- gingival.Rmd:
  - Perform k-mediods clustering on gingival samples - clusters will be called community profiles (CPs)
  - Perform and plot RDA analysis to visualize CPs (Figure S2A)
  - Compare alpha diversity of different CPs
  - Perform differential abundance testing to see which ASVs differ between CPs and visualize results (Figure S2B)
  - Investigate potential correlations between CPs and metadata (sampling time, sampling location)
