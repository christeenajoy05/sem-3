import matplotlib.pyplot as plt

# Data
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]

# Create a subplot with the specified characteristics
plt.figure(figsize=(8, 4))  # Set the figure size
plt.subplot(1, 1, 1)  # Create a single subplot

# Plot the data
plt.plot(years, car_values, color='red', linestyle='-.', label='Car Value')
plt.scatter(years, car_values, color='green', marker='*', s=20, label='Data Points')

# Set axis labels and title
plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title('Value Depreciation', loc='left')

# Show legend
plt.legend()

# Show the plot
plt.show()
