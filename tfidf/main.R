setwd("~/peasInACast/tfidf")

library(stringr)
library(plyr)
library(dplyr)
library(magrittr)
library(tm)
library(proxy)
library(ggplot2)
library(RColorBrewer)
library(wordcloud)

podcastData <- read.csv("transcriptions.csv", stringsAsFactors=FALSE)

set.seed(1300)

corpus <- VCorpus(VectorSource(podcastData$transcript)) %>%
  tm_map(x = ., FUN = PlainTextDocument) %>%
  tm_map(x = ., FUN = removePunctuation) %>%
  tm_map(x = ., FUN = removeNumbers) %>%
  tm_map(x = ., FUN = removeWords, stopwords(kind = 'en')) %>%
  tm_map(x = ., FUN = stripWhitespace)

doc_term <- DocumentTermMatrix(corpus)
doc_term$dimnames$Docs <- podcastData$episode

tf_idf <- weightTfIdf(m = doc_term, normalize = TRUE)
tf_idf_mat <- as.matrix(tf_idf)
save(tf_idf_mat, file="matrix.Rdata")
tf_idf_df <- as.data.frame(tf_idf_mat)

library(MASS)
#write.table(tf_idf_mat, file='tfidf_Data.csv', row.names = TRUE, col.names = TRUE)
write.csv(tf_idf_df, file='tfidf_Data.csv')


podcastWords <- tf_idf_mat[ranking[i],]
cat(names(podcastWords[order(-podcastWords)][1:5]))

library(SnowballC)

drawPCHisto <-function(PCNumber, theTitle) {
  keyWords <- c('startup', 'hire', 'hiring', 'hired', 'investors')
  
  podcastWords <- tf_idf_mat[PCNumber,]
  specialKeywords <- names(podcastWords[order(-podcastWords)][1:10])
  words <- strsplit(podcastData$transcript[PCNumber], ' ')[[1]]
  whichWords <- which(wordStem(words, language="porter")
                      %in% wordStem(c(keyWords, specialKeywords), language="porter")) / length(words)
  hist(whichWords, xlab='', ylab='Freq', main=theTitle, breaks=10)
  frame()
  mtext(paste0("Podcast keywords:\n", 
               paste(specialKeywords[1:5], specialKeywords[6:10], collapse='\n')),
        line=-3, cex=0.7)
}
drawPCHisto_v2 <-function(PCNumber, theTitle) {
  keyWords <- c('startup', 'hire', 'hiring', 'hired', 'investors')
  
  podcastWords <- tf_idf_mat[PCNumber,]
  specialKeywords <- names(podcastWords[order(-podcastWords)][1:10])
  words <- strsplit(podcastData$transcript[PCNumber], ' ')[[1]]
  whichWords <- which(wordStem(words, language="porter")
                      %in% wordStem(c(keyWords, specialKeywords), language="porter")) / length(words)
  frame()
  mtext(paste0("Podcast keywords:\n", 
               paste(specialKeywords[1:5], specialKeywords[6:10], collapse='\n')),
        line=-3, cex=0.7)
  hist(whichWords, xlab='', ylab='Freq', main=theTitle, breaks=10)
}


# For our sanity, let's remove non-english words
englishWords <- readLines('wordsEn.txt')
tf_idf_mat <- tf_idf_mat[,(colnames(tf_idf_mat) %in% englishWords)]

png('podcastView.png', width = 5, height = 8.5, units = 'in', res = 300)
par(mfrow = c(3,2))
par(mar=c(5.1,4.1,8.1,1.1))
drawPCHisto_v2(29, "Masters of Scale:\nBeauty of a Bad Idea")
drawPCHisto(28, "How I Built This:\nWhole Foods Market")
drawPCHisto_v2(14, "Smart Passive Income:\nHow to Avoid the Slimy Sell")
mtext("When keywords are spoken during podcasts", side = 3, line = -2, outer = TRUE)

dev.off ()


