import random
import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotx
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# Set styles for the plot
plt.style.use ('seaborn-darkgrid')
plt.style.use(matplotx.styles.dufte)

# Getting input for simulation parameters
num_people = int(input("Enter the number of people: "))
initial_money = int(input("Enter the initial amount of money per person: "))
num_transactions = int(input("Enter the number of transactions: "))
num_top_people = int(input("Enter the number of top people to track: "))
num_bottom_people = int(input("Enter the number of bottom people to track: "))

# Initialize the money distribution and history tracking
people = [initial_money] * num_people
history = [[] for _ in range(num_people)]

# Function to plot money distribution as a bar chart
def plot_money_distribution(people, title) :
    plt.figure(figsize=(10,6))

    min_money = min(people)
    max_money = max(people)

    # Normalize the money distribution for color scaling
    if max_money == min_money :
        normalized_money = [1] * len(people)
        colors = 'skyblue'

    else:
        normalized_money = [(p - min_money) / (max_money - min_money) for p in people]
        colors = plt.cm.Blues(normalized_money)

    # Plot the bar chart
    plt.bar(range(len(people)), people, color= colors, edgecolor= 'black')

    # Add colorbar if money is not uniformly distributed
    if max_money != min_money :
        sm = plt.cm.ScalarMappable(cmap="Blues", norm= plt.Normalize(vmin= min_money, vmax= max_money))
        sm. set_array([])
        cbar = plt.colorbar(sm)
        cbar.set_label('Amount of Money')

    # Set x-ticks for people
    xticks = list(range(0, len(people), 5)) + [len(people) - 1]
    plt.gca().xaxis.set_major_locator(plt.FixedLocator(xticks))
    plt.xticks(xticks, labels=[str(i + 1) for i in xticks])

    # Add plot titles and labels
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Members', fontsize=12)
    plt.ylabel('Money', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Simulation loop for money exchange
for transition in range(num_transactions):
    for i in range (num_people):
        history[i].append(people[i])    # Record the current money for each person

    # Find people with money to exchange
    active_people = [i for i in range(num_people) if people[i] > 0]

    if len(active_people) < 2:
        print(f'just {len(active_people)} people remained. simulation stopped!')
        break

    # Randomly select a giver and a receiver
    giver = random.choice(active_people)
    receiver = random.choice(active_people)

    # Ensure giver and receiver are not the same
    while giver == receiver :
        receiver = random.choice(active_people)

    # Transfer money if the giver has money
    if people[giver] > 0:
        people[giver] -= 1
        people[receiver] += 1

# Plot the initial and final distributions of money
plot_money_distribution([initial_money] * num_people, 'Primary distribution of money')
plot_money_distribution(people, 'Final distribution of money after simulation')

# Get the indices of top and bottom people based on final money
top_indices = np.argsort(people)[-num_top_people:]
bottom_indices = np.argsort(people)[:num_bottom_people]

# Plot the money history for top and bottom people
plt.figure(figsize=(10,8))

top_colors = {}   # To store colors of top people

for i in top_indices:
    line, = plt.plot(history[i], label=f'Top Person {i + 1}', alpha=0.8, linewidth=1)
    top_colors[i] = line.get_color() 

for i in bottom_indices:
    plt.plot(history[i], label=f'Bottom Person {i + 1}', alpha=0.8, linewidth=1, linestyle='dashed')

# Add title, labels, and grid
plt.title(f'Money Changes Over Transactions for Top {num_top_people} and Bottom {num_bottom_people} People', fontsize=16, fontweight='bold')
plt.xlabel('Number of Transactions', fontsize=12)
plt.ylabel('Amount of Money', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
matplotx.line_labels()
plt.show()

# Find the person with the most money at the end of the simulation
max_money = max(people)
person_with_max_money = people.index(max_money)

# Get the color of the top person for animation
top_person_color = top_colors.get(person_with_max_money)

# Create a figure for the animation
fig = plt.figure(figsize=(10,8))
axis = plt.axes(xlim=(0, num_transactions), ylim=(0, max(people) +50))
line, = axis.plot([], [], lw=2, color=top_person_color)
xdata, ydata = [], []

# Initialize the plot for animation
def init():
    line.set_data([], [])
    return line,

# Initialize text for labels
label = axis.text(0, max(people) + 20, '', fontsize=12, fontweight='bold')

# Update the plot for each frame of the animation
def animate(i):
    x = list(range(i + 1))  # Transaction numbers up to the current frame
    y = history[person_with_max_money][:i + 1]  # Money changes for the person
    line.set_data(x, y)   # Update the plot with new data
    
    # Update the label text
    label.set_text(f'Top Individual: {person_with_max_money + 1}, Money: {y[-1]}')  # Update label with current money
    label.set_position((i, max(y) + 5))  # Adjust the position of the label based on the current data
    
    return line, label,

# Create the animation for the money changes over transactions
anim = animation.FuncAnimation(
    fig,  # The figure object for the animation
    animate,  # The function to call to update the frame
    init_func=init,  # Initialization function (sets up the plot)
    frames=range(0, num_transactions, max(1, num_transactions // 100)),  # Frames to animate over
    interval=1,  # Time between frames in milliseconds
    blit=True  # Only update parts of the plot that have changed
)

line.set_label(f'Top Individual')  # Ensure the line has a label
plt.legend()

# Save the animation as an MP4 file
anim.save('money_change_animation.mp4', writer='ffmpeg', fps=30)

# Save the animation as an gif file
anim.save('money_change_animation.gif', writer=PillowWriter(fps=30))

# Add titles and labels for the animation plot
plt.title('Change in Money Over Transactions for the Top Individual', fontsize=16, fontweight='bold')
plt.xlabel('Number of Transactions', fontsize=12)
plt.ylabel('Amount of Money', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6, linewidth= 1)
plt.show()

# Plot histogram of final money distribution among people
plt.figure(figsize=(10,6))
plt.hist(people, bins=20, color='skyblue', edgecolor='black')
plt.title('Money Distribution Histogram', fontsize=16, fontweight='bold')
plt.xlabel('Amount of Money', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Identify and print the person with the most money
max_money = max(people)
person_with_max_money = people.index(max_money) + 1   # 1-based indexing for easier readability
print(f'Person number {person_with_max_money} has the most money: {max_money}')

# Calculate the number of people who were removed (those with no money)
removed_people = num_people - len([p for p in people if p > 0])
print(f'Number of people removed: {removed_people}')

# Find and print the people who lost all their money
people_with_zero_money = [i + 1 for i, money in enumerate(people) if money == 0]

if people_with_zero_money:
    print(f'People who lost all their money: {people_with_zero_money}')
else:
    print('No one lost all their money.')

# Calculate and print key statistics of the final money distribution
mean_money = np.mean(people)   # Calculate the average amount of money
median_money = np.median(people)    # Calculate the median amount of money
std_dev_money = np.std(people)    # Calculate the standard deviation of the money distribution

print(f'Average money per person: {mean_money:.2f}')
print(f'Median money per person: {median_money:.2f}')
print(f'Standard deviation of money: {std_dev_money:.2f}')

# Save the final results to a CSV file
with open('simulation_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Person', 'Final Money'])
    for i, money in enumerate(people):
        writer.writerow([i + 1, money])