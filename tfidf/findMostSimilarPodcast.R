#!/usr/bin/env Rscript
args <- commandArgs(trailingOnly=TRUE)
args <- tolower(args)

setwd("~/peasInACast/tfidf")
load("matrix.Rdata")
args = strsplit(args, split=",")[[1]]

searchVec <- rep(0, ncol(tf_idf_mat))

for (arg in args) {
  if(arg %in% colnames(tf_idf_mat)) {
    searchVec[which(colnames(tf_idf_mat) == arg)] = 1
  }
}

library(proxy)
podcastDist <- dist(x=tf_idf_mat, y=t(searchVec), method = 'cosine')
ranking <- order(podcastDist)
results <- paste(labels(podcastDist)[[1]][ranking], 
                 podcastDist[ranking], sep=', ')
#cat(paste0(results[1:10], collapse='\n'))

englishWords <- readLines('wordsEn.txt')

for(i in 1:10) {
  cat(results[i])
  cat(",")
  podcastWords <- tf_idf_mat[ranking[i],]
  cat(names(podcastWords[order(-podcastWords)][1:5]))
  if(i != 10) {cat('\n')}
}

q()

