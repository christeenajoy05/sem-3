import nltk
from nltk import ngrams
from nltk.corpus import stopwords
nltk.download('punkt')
from nltk.tokenize import sent_tokenize,word_tokenize
print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
text1="The data set given satisfies the requirement for model generation. This is used in Data Science Lab"
print("sentence tokenization")
print(sent_tokenize(text1))

print("")
print("Word tokenization")
print(word_tokenize(text1))
text=word_tokenize(text1)
text2=[word for word in text if word not in stopwords.words('english')]
print("")
print("Removing stop words")
print(text2)
print("")
print("n grams")
unigrams=ngrams(text2,3)
for grams in unigrams:
    print(grams)