import matplotlib.pyplot as plt

# Replace these with your actual data
modes_of_transport = ["Walking", "Cycling", "Car", "Bus", "Train"]
frequency = [29,15,35,18,3]

# Create a bar graph
plt.figure(figsize=(8, 6))

plt.bar(modes_of_transport, frequency, width=0.1, color='green')

# Set properties for the graph
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')

# Show the bar graph
plt.show()
