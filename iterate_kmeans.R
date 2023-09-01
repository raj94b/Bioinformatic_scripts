library(adegenet)
hal<-read.genetix("snps.gtx")
pca= 75
iter=100
nclust=50
for(i in 1:iter){
grp <- find.clusters(hal, max.n.clust = nclust, n.pca = pca, choose.n.clust = FALSE)
if(i==1){
  k<-grp$Kstat
}
  else{
    k<-rbind(k, grp$Kstat)
}
}
p<-as.data.frame(k)
colnames(p)<- c(1:nclust)
rownames(p)<-c()

m<-c()
se<-c()

for(i in 1:iter){
  v<-p[,i]
  m<-append(m, mean(as.numeric(v)))
  se<-append(se, 3*sd(v))
  #se2<-append(se2, 3*sd(v))
}
k_means<-data.frame(m, se)
ggplot(k_means, aes(x=1:clust,y=m)) + geom_line() +  geom_errorbar(width=.1, aes(ymin=m-se, ymax=m+se)) + geom_point() + ggtitle("Value of BIC versus number of clusters") + ylab("Value of BIC") + xlab("Number of Clusters") + theme_minimal()