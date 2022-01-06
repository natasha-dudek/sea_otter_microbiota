# Characterizing the microbiota of the threatened southern sea otter (_Enhydra lutris nereis_) to enhance conservation practice

This repository contains the R version 3.6.1 and python version 3.7.6 implementations of the analysis described in:

Dudek, N.K., Switzer, A.D., Costello, E.K., Murray, M.J., Tomoleoni, J.A., Staedler, M.M., Tinker, M.T., Relman, D.A. Characterizing the microbiota of the threatened southern sea otter (_Enhydra lutris nereis_) to enhance conservation practice. Under review at Conservation Science and Practice (2021).

Southern sea otters are a threatened keystone sub-species in coastal ecosystems. To understand better the role of diet, monitor health, and enhance management of this and other marine mammal species, we characterized the oral and distal gut microbiota of 158 wild southern sea otters (_Enhydra lutris nereis_) living off the coast of central California, USA, 13 captive sea otters (some of which participated in a diet shift experiment), and 17 otters from three other otter species.

### Installation

Coming soon...

### How to run

To characterize the taxonomic structure of gingival and rectal microbiotas from wild sea otters:
- community_composition_p1.py: 
  -  For gingival and rectal samples, plots barplot showing taxa on the x-axis and relative abundance in samples on the y-axes (Figure 2A,B)
- community_composition_p2.Rmd: 
  - Plots an ordination of gingival, rectal, and otter-associated seawater samples and performs significance testing (Figure 2C)
  - Plots a Venn diagram showing for sets of gingival, rectal, and otter-associated seawater ASVs (Figure 2D)

To perform comparisons of the distal gut microbiota of different otter species:
- spp_comparisons.Rmd: 
  - Plot ordinations of distal gut samples from different otter species (Figures 3, S3)
  - Perform a bootstrap test to investigate whether the average Unifrac distance between distal gut specimens within a species is significantly lower than the average distance between samples from sea otters vs North American river otters
  - Perform differential abundance testing on sea otter vs North American river otter samples to probe how the composition of their microbiotas are distinct

More coming soon...
