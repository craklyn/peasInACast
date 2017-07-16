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
