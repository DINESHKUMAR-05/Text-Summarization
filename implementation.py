import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

def read_para(string):
    article = string.split(". ")
    sentences = []
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    return sentences

def similarity_in_sentences(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for w1 in range(len(sentences)):
        for w2 in range(len(sentences)):
            if w1 == w2: 
                continue 
            similarity_matrix[w1][w2] = similarity_in_sentences(sentences[w1], sentences[w2], stop_words)
    return similarity_matrix

def summary(txt, top_n=5):
    stop_words = stopwords.words('english')
    summarized_text = []
    sentences =  read_para(txt)
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    for i in range(top_n):
        summarized_text.append(" ".join(ranked_sentence[i][1]))
    return(". ".join(summarized_text))


    
import streamlit as st
st.title("Text Summarizer using Streamlit")
file = st.file_uploader("Upload file", type=["txt"])
no_para=st.text_input("Enter the size of summarized paragraph :")
if file is not None:
    if no_para is not None and len(no_para)>0:
        content = file.read().decode("utf-8")
        st.subheader("Summarized Text : ")
        st.markdown(summary(content,int(no_para)))
