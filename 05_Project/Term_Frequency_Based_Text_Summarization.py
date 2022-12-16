import os
import glob
import pandas as pd
import numpy as np
import rouge
from rouge import Rouge

import nltk


def tokeniser(t):
    return nltk.sent_tokenize(t)

def word_frequency(many_sent):
    word_frequencies = {}
    for sentence in many_sent:
      words = nltk.word_tokenize(sentence)
      for word in words:
        if word not in word_frequencies.keys():
          word_frequencies[word] = 1
        else:
          word_frequencies[word] += 1
    return word_frequencies
   

def summarize_text(text, count_sent):
    # Tokenizing the text into sentences
    sentences = tokeniser(text)
    
    # Check if the number of sentences requested is valid
    if count_sent > len(sentences):
      return "ERROR: The text does not have that many sentences."

    # Compute the word frequencies    
    word_frequencies=word_frequency(sentences)
    
        
    # Compute the maximum word frequency
    maximum_frequency = max(word_frequencies.values())
    
    # Compute the weighted frequencies
    for word in word_frequencies.keys():
      word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    
    # Compute the sentence scores
    sentence_scores = {}
    for sentence in sentences:
      words = nltk.word_tokenize(sentence)
      score = 0
      for word in words:
        if word in word_frequencies.keys():
          score += word_frequencies[word]
      sentence_scores[sentence] = score
    
    # Get the top N sentences with the highest scores
    summary_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:count_sent]
    
    # Sort the sentences in the original order
    summary_sentences.sort(key=lambda x: sentences.index(x[0]))
    
    # Generate the summary
    summary = " ".join([x[0] for x in summary_sentences])
    return summary


os.chdir(r"C:\Key files- GNA\Indiana University\Computation and Linguistic Analysis\Project\LSTM_model_data")
test_dataset=pd.read_csv('test_dataset.csv',encoding='iso-8859-1').reset_index(drop=True)

predicted=[]
for each_text in test_dataset['text']:
    predicted.append(summarize_text(each_text, 1))
    
test_dataset['predicted_summary']=predicted
 
rouge = Rouge()    
scores = rouge.get_scores(test_dataset['predicted_summary'], test_dataset['headlines'], avg=True)    
scores

