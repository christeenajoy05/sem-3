import matplotlib.pyplot as plt

# Replace these with your actual data
months = ["Jan", "Feb", "Mar", "Apr", "May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
affordable_segment = [173,153,195,147,120,144,148,109,174,130,172,131]
luxury_segment = [189,189,105,112,173,109,151,197,174,145,177,161]
super_luxury_segment = [185,185,126,134,196,153,112,133,200,145,167,110]

# Create a scatter plot with different colors for each segment
plt.figure(figsize=(10, 6))

# Plot the data for the Affordable segment
plt.scatter(months, affordable_segment, color='pink', label='Affordable', s=100)

# Plot the data for the Luxury segment
plt.scatter(months, luxury_segment, color='yellow', label='Luxury', s=100)

# Plot the data for the Super Luxury segment
plt.scatter(months, super_luxury_segment, color='blue', label='Super Luxury', s=100)

# Set properties for the graph
plt.xlabel('Months of Year', fontsize=18)
plt.ylabel('Sales of Segments')
plt.title('Sales Data', fontsize=18)

# Add legend
plt.legend()

# Show the scatter plot
plt.show()
