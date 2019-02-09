# GEOparse-query-
Gene expression Omnibus data pulling

1. Open the GEO - NCBI webstie
https://www.ncbi.nlm.nih.gov/geo/

2. Search your research interest.
e.g. DNA methylation, transcriptomics, metabolomics, etc.

3. Find open sources projects of your interest and copy the GSE/GEO project number
e.g. GSE118260
Please note that you have enough size of RAM. DNA methylation data is usually as large as (450k by # of observations) in case that they used Infinium HumanMethylation 450 BeadChip. If a project used Infinium MethylationEPIC Kit, the DNA methylation data will be 850k by # of observations.

4-1. Start a R session

4-2. Install the R package "GEOquery" through bioconductor.

4-3. Install the R pacakge "feather" using install.packages command. The feather format can handle a large dataset faster than csv or Rdata (rda) format to my experience.

4-4. Run the enclosed R code after replacing the pre-selected GEO number with yours.


5-1. Install the Python package GEOparse through pip or conda command.

5-1. Start a python session

