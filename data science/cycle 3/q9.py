import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset (replace 'iris.csv' with your file path)
iris_data = sns.load_dataset("iris")

# Create a displot for the 'sepal_length' column
#sns.displot(data=iris_data, x="sepal_length", kde=True)
#sns.relplot(data=iris_data, x="sepal_length", y="petal_length", hue="species")
sns.histplot(data=iris_data, x="petal_length", bins=10, kde=True)

# Show the displot
plt.show()
