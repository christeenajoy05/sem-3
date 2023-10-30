import pandas as pd

# Read the 'iris' data set from a CSV file
iris_data = pd.read_csv('iris.csv')

# i) Display Shape of the data set
print("i) Shape of the data set:")
print(iris_data.shape)

# ii) First 5 and last five rows of data set (head and tail)
print("\nii) First 5 rows of the data set:")
print(iris_data.head())

print("\nLast 5 rows of the data set:")
print(iris_data.tail())

# iii) Size of the dataset
print("\niii) Size of the dataset:")
print(iris_data.size)

# iv) No. of samples available for each variety
print("\niv) Number of samples available for each variety:")
print(iris_data['variety'].value_counts())

# v) Description of the data set (use describe)
print("\nv) Description of the data set:")
print(iris_data.describe())
