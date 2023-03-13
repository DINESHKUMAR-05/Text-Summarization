It is hard for humans to manually extract the summary of a really large documents. So in those cases we can use text summarizers . Text summarizer identifies the meaningful information in a document and summarizes it by preserving the overall meaning. This code presents a shorter version of the original text while preserving the semantics of the whole document. Cosine Distance is used as similarity measure to identify the similarity between two sentences. By this way a similarity matrix is created. Using the similarity matric the Top k important sentences are taken to form a summary of the whole text.

We have used Streamlit Framework to present the summarizer with a attractive UI.



This project implements a summary generator using the concept of Cosine Similarity. It reads a text file, generates a similarity matrix across the sentences in the file, ranks the sentences based on their similarity score, and returns the top n sentences as the summary of the input text file.



Libraries used:
  - nltk
  - numpy
  - networkx
  - streamlit


Functions:

1) read_para(file_name):
    This function reads a text file and returns the sentences in it.

2) sentence_similarity(sent1, sent2, stopwords):
    This function takes two sentences and a list of stopwords as input and returns the cosine similarity score between the two sentences.

3) build_similarity_matrix(sentences, stop_words):
    This function builds a similarity matrix between all the sentences in the text file using the sentence_similarity() function.

4) summary(file_name, top_n):
    This function takes a text file name and the number of top sentences to be included in the summary as input. It uses all the above functions to generate a summary of the input text file.



How to use:

- Import the required libraries.
- Define the input file name and the number of top sentences to include in the summary.
- Call the summary() function with the input file name and the number of sentences required as input.

Example:
            summary( "article.txt", 2)
            
This will generate a summary of the file "article.txt" consisting of the top 2 sentences.
