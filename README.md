# GEOparse-query-
Gene expression Omnibus data pulling

1. Open the GEO - NCBI webstie
https://www.ncbi.nlm.nih.gov/geo/

2. Search your research interest.
e.g. DNA methylation, transcriptomics, metabolomics, etc.

3. Find open sources projects of your interest and copy the GSE/GEO project number
e.g. GSE118260
Please note that you have enough size of RAM. DNA methylation data is usually as large as (450k by # of observations) in case that they used Infinium HumanMethylation 450 BeadChip. If a project used Infinium MethylationEPIC Kit, the DNA methylation data will be 850k by # of observations.


### R
4-1. Start a R session

4-2. Install the R package "GEOquery" through bioconductor.

4-3. Install the R pacakge "feather" using install.packages command. The feather format can handle a large dataset faster than csv or Rdata (rda) format.

4-4. Run the enclosed R code after replacing the pre-selected GEO number with yours.

### Python
5-1. Install the Python package GEOparse through pip or conda installer.
For conda users, use this command to install. "conda install -c hcc geoparse"

5-2. Install the Python package feather through pip or conda installer.
Again, the feather format import huge datasets amazingly fast.

5-3. Run the enclosed Python code after replacing the pre-selected GEO number with yours.


### NOTE: Selection between R and Python.
Both work well if you have enough RAM on your local computer. However, we do not usually want to or sometimes too poor to afford high RAM. Rather, we often benefit cloud or cluster computing system which can provide with high RAM or many CPUs. In case that you have access to cluster or cloud and want to collect genomic data from GEO repository, you must check whether the cloud or cluster has internet connections (They mostly do, but some isolated clusters do not due to data security issues). Then, I recommend to use GEOparse (python-based) over GEOquery (R-based). I found that clusters lost connections to GEO database when GEOquery (R-based) is a work horse.

