import matplotlib.pyplot as plt

# Replace these with your actual data
months = ["Jan", "Feb", "Mar", "Apr", "May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
affordable_segment = [173,153,195,147,120,144,148,109,174,130,172,131]
luxury_segment = [189,189,105,112,173,109,151,197,174,145,177,161]
super_luxury_segment = [185,185,126,134,196,153,112,133,200,145,167,110]

# Create a multiline plot with different colors and line styles
plt.figure(figsize=(10, 6))

# Plot the data for the Affordable segment
plt.plot(months, affordable_segment, label='Affordable', color='red', linestyle='-', marker='o')

# Plot the data for the Luxury segment
plt.plot(months, luxury_segment, label='Luxury', color='green', linestyle='--', marker='s')

# Plot the data for the Super Luxury segment
plt.plot(months, super_luxury_segment, label='Super Luxury', color='blue', linestyle='-.', marker='^')

# Set properties for the graph
plt.xlabel('Months of Year')
plt.ylabel('Sales of Segments')
plt.title('Sales Data')
plt.legend(loc='upper right')

# Show the multiline plot
plt.show()
