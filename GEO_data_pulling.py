import GEOparse
import pandas as pd

working_dir="/home/yunsunglee/data/second_project/"

target='GSE118260'
gse=GEOparse.get_GEO(target, destdir=working_dir)


### Pull phenotype data
info=gse.phenotype_data

### Stack genomic data 
for one_person in info.index:
    if one_person == info.index[0]:
        expr=gse.gsms[one_person].table[['ID_REF','VALUE']]
        expr.columns=['ID_REF',one_person]
    else:
        t1=gse.gsms[one_person].table[['ID_REF','VALUE']]
        t1.columns=['ID_REF',one_person]
        expr=expr.merge(t1,on="ID_REF", how="left")
    print(one_person)

### Save the resulting data in your working directory
feather.write_dataframe(expr, dest=working_dir+target+"_expr.feather")
feather.write_dataframe(info, dest=working_dir+target+"_info.feather")
