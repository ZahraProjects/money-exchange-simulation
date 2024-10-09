# money-exchange-simulation
 A Python project simulating a money exchange game. Participants start with an initial amount and randomly give money to each other over a specified number of transactions. The simulation tracks changes in money distribution, visualizes results through charts and animations, and saves the final outcomes in a CSV file.

# Money Exchange Simulation

This project simulates a simple random money exchange game where a fixed number of people start with an initial amount of money and randomly exchange money with each other over a given number of transactions. The simulation tracks the changes in money distribution and visualizes the results through different plots and animations.

## Project Features
- Random money exchange between people.
- Visualizes initial and final money distribution.
- Tracks and plots the money changes of top and bottom individuals.
- Generates an animated GIF showing the money changes over transactions for the top individual.
- Calculates key statistics (average, median, standard deviation) of the final money distribution.
- Saves the final results in a CSV file.

## How It Works
1. **Input Parameters**: 
   The user provides the following input parameters at the start of the simulation:
   - Number of people in the simulation.
   - Initial amount of money per person.
   - Number of transactions to simulate.
   - Number of top and bottom people to track.

2. **Simulation Process**:
   - In each transaction, a random person gives 1 unit of money to another random person.
   - This process repeats for the specified number of transactions.

3. **Visualization**:
   - The project generates several plots:
     - Bar charts showing the initial and final distribution of money.
     - A line chart showing the money changes for the top and bottom individuals over time.
     - An animated GIF visualizing the money changes for the top individual during the simulation.

4. **Statistics**:
   - The project calculates and prints key statistics of the final money distribution:
     - Average amount of money per person.
     - Median amount of money.
     - Standard deviation of the money distribution.

5. **Output**:
   - The final money distribution is saved in a CSV file.
   - An animated GIF of the top individual’s money changes is saved in the project folder.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ZahraProjects/money-exchange-simulation.git
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the simulation by executing the Python script:
   ```bash
   python simulation.py
   ```

## Example Plots
All generated plots and the animated GIF of the top individual’s money changes will be saved in the `charts` folder within the project directory.

## CSV Output
The results of the simulation are saved in a file called `simulation_results.csv` with the following columns:
- **Person**: The ID of each individual.
- **Final Money**: The amount of money each person has at the end of the simulation.

## License
This project is licensed under the MIT License.