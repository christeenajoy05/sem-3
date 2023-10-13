import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]

# Create a subplot with 2 rows and 1 column (two separate graphs)
plt.figure(figsize=(8, 8))

# Subplot 1 - Sales Data for Drinks
plt.subplot(2, 1, 1)

# Plot the sales data for drinks
plt.plot(days, drinks_sales, linestyle='dotted', color='cyan', label='Sales Data1', marker='H', markersize=8, markerfacecolor='magenta', markeredgecolor='black')

# Set properties for the first graph
plt.xlabel('Days of the Week')
plt.ylabel('Sale of Drinks')
plt.title('Sales Data1', loc='right')
plt.grid(color='blue', linestyle='--')

# Add legend
plt.legend()

# Subplot 2 - Sales Data for Food
plt.subplot(2, 1, 2)

# Plot the sales data for food
plt.plot(days, food_sales, linestyle='--', color='yellow', label='Sales Data2', marker='D', markersize=8, markerfacecolor='green', markeredgecolor='red')

# Set properties for the second graph
plt.xlabel('Days of the Week')
plt.ylabel('Sale of Food')
plt.title('Sales Data2', loc='center')
plt.grid(color='blue', linestyle='--')

# Add legend
plt.legend()

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plots
plt.show()
