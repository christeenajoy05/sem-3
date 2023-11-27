from nltk import ngrams

print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
sentence='I reside in Bengaluru'
n=3
unigrams=ngrams(sentence.split(),n)
for grams in unigrams:
    print(grams)