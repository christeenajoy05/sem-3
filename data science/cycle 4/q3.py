# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn import metrics
print("Register No: SJC22MCA-2020 \nName: Christeena Joy \nBatch: S3 MCA \n**************************\n")
# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Naive Bayes models
gnb = GaussianNB()
bnb = BernoulliNB()
mnb = MultinomialNB()

# Fit the models on the training set
gnb.fit(X_train, y_train)
bnb.fit(X_train, y_train)
mnb.fit(X_train, y_train)

# Make predictions on the test set
y_pred_gnb = gnb.predict(X_test)
y_pred_bnb = bnb.predict(X_test)
y_pred_mnb = mnb.predict(X_test)

# Calculate accuracy
accuracy_gnb = metrics.accuracy_score(y_test, y_pred_gnb)
accuracy_bnb = metrics.accuracy_score(y_test, y_pred_bnb)
accuracy_mnb = metrics.accuracy_score(y_test, y_pred_mnb)

# Display accuracy
print(f"Gaussian Naive Bayes Accuracy: {accuracy_gnb}")
print(f"Bernoulli Naive Bayes Accuracy: {accuracy_bnb}")
print(f"Multinomial Naive Bayes Accuracy: {accuracy_mnb}")

# Display the number of mislabeled classifications
mislabel_count_gnb = (y_test != y_pred_gnb).sum()
mislabel_count_bnb = (y_test != y_pred_bnb).sum()
mislabel_count_mnb = (y_test != y_pred_mnb).sum()

print(f"\nNumber of Mislabeled Classifications (Gaussian NB): {mislabel_count_gnb}")
print(f"Number of Mislabeled Classifications (Bernoulli NB): {mislabel_count_bnb}")
print(f"Number of Mislabeled Classifications (Multinomial NB): {mislabel_count_mnb}")

# List out the class labels of the mismatching records
mismatch_indices_gnb = [i for i in range(len(y_test)) if y_test[i] != y_pred_gnb[i]]
mismatch_indices_bnb = [i for i in range(len(y_test)) if y_test[i] != y_pred_bnb[i]]
mismatch_indices_mnb = [i for i in range(len(y_test)) if y_test[i] != y_pred_mnb[i]]

print("\nMismatching Class Labels (Gaussian NB):", y_test[mismatch_indices_gnb])
print("Mismatching Class Labels (Bernoulli NB):", y_test[mismatch_indices_bnb])
print("Mismatching Class Labels (Multinomial NB):", y_test[mismatch_indices_mnb])
