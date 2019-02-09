rm(list=ls())
require(GEOquery)
require(feather)
### Your working directory
setwd("C://Users/kekem/Desktop/GEO_data/")



target="GSE118260"
gse=getGEO(target,GSEMatrix = T)
print(gse)
expr=t(assayData(gse[[1]])$exprs)
expr=data.frame(SampleID=rownames(expr), expr)
info=pData(phenoData(gse[[1]]))

print(target)
print(dim(expr))
print(dim(info))

write_feather(info,paste(target,"_info.feather",sep=""))
write_feather(data.frame(expr),paste(target,"_expr.feather",sep=""))

rm(list=setdiff(ls(),"target"))








