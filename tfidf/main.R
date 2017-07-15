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

podcastData <- c(paste(readLines('Data/620.txt'), collapse=' '))

set.seed(1300)

corpus <- VCorpus(VectorSource(podcastData)) %>%
  tm_map(x = ., FUN = PlainTextDocument) %>%
  tm_map(x = ., FUN = removePunctuation) %>%
  tm_map(x = ., FUN = removeNumbers) %>%
  tm_map(x = ., FUN = removeWords, stopwords(kind = 'en')) %>%
  tm_map(x = ., FUN = stripWhitespace)

doc_term <- DocumentTermMatrix(corpus)
doc_term$dimnames$Docs <- "episode 620"

tf_idf <- weightTfIdf(m = doc_term, normalize = TRUE)
tf_idf_mat <- as.matrix(tf_idf)

tf_idf_mat







