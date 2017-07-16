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

source("HavenAPI.R")
getPodcastTranscripts("podcastJobIdMap.txt")

readFile(podcastJobIdMap.txt)

episodes <- list.files("Data")
podcastData <- sapply(episodes, function(x) paste(readLines(paste0("Data/",x), encoding="UTF-8"), collapse=' '))

set.seed(1300)

corpus <- VCorpus(VectorSource(podcastData[9])) %>%
  tm_map(x = ., FUN = PlainTextDocument) %>%
  tm_map(x = ., FUN = removePunctuation) %>%
  tm_map(x = ., FUN = removeNumbers) %>%
  tm_map(x = ., FUN = removeWords, stopwords(kind = 'en')) %>%
  tm_map(x = ., FUN = stripWhitespace)

doc_term <- DocumentTermMatrix(corpus)
doc_term$dimnames$Docs <- c("episode 620", "episode 109")

tf_idf <- weightTfIdf(m = doc_term, normalize = TRUE)
tf_idf_mat <- as.matrix(tf_idf)

tf_idf_mat







