import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Define the CSV file to store fitness data
DATA_FILE = "fitness_data.csv"

# Initialize DataFrame columns
columns = ['Date', 'Activity', 'Steps', 'Duration (min)', 'Distance (km)', 'Calories Burned']

# Load existing data if file exists
if os.path.exists(DATA_FILE):
    fitness_data = pd.read_csv(DATA_FILE)
else:
    fitness_data = pd.DataFrame(columns=columns)

# Function to save data
def save_data():
    fitness_data.to_csv(DATA_FILE, index=False)

# Function to add a workout
def add_workout(activity, steps, duration, distance, calories_burned):
    global fitness_data
    date_today = datetime.now().strftime("%Y-%m-%d")
    workout_data = {
        'Date': date_today,
        'Activity': activity,
        'Steps': steps,
        'Duration (min)': duration,
        'Distance (km)': distance,
        'Calories Burned': calories_burned
    }
    # Append new workout data
    new_row = pd.DataFrame([workout_data])
    fitness_data = pd.concat([fitness_data, new_row], ignore_index=True)
    save_data()  # Save to CSV
    print("Workout added successfully!")

# Function to visualize fitness progress
def visualize_progress():
    global fitness_data
    if fitness_data.empty:
        print("No data to visualize!")
        return

    # Convert 'Calories Burned' to float for plotting
    fitness_data['Calories Burned'] = fitness_data['Calories Burned'].astype(float)
    
    plt.figure(figsize=(10, 6))
    plt.plot(fitness_data['Date'], fitness_data['Calories Burned'], marker='o', linestyle='-', color='b')
    plt.title("Calories Burned Over Time")
    plt.xlabel("Date")
    plt.ylabel("Calories Burned")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to calculate total stats
def calculate_totals():
    global fitness_data
    if fitness_data.empty:
        print("No data to calculate totals!")
        return

    total_steps = fitness_data['Steps'].sum()
    total_distance = fitness_data['Distance (km)'].sum()
    total_calories = fitness_data['Calories Burned'].sum()
    total_duration = fitness_data['Duration (min)'].sum()

    print(f"\nTotal Steps: {total_steps}")
    print(f"Total Distance: {total_distance} km")
    print(f"Total Calories Burned: {total_calories}")
    print(f"Total Workout Duration: {total_duration} minutes")

# Main function
def main():
    while True:
        print("\nPersonal Fitness Tracker")
        print("1. Add a Workout")
        print("2. Visualize Progress")
        print("3. Calculate Total Stats")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            activity = input("Enter Activity (e.g., Walking, Running): ")
            steps = int(input("Enter the number of steps: "))
            duration = int(input("Enter the workout duration in minutes: "))
            distance = float(input("Enter the distance in km: "))
            calories_burned = float(input("Enter the calories burned: "))
            add_workout(activity, steps, duration, distance, calories_burned)
        
        elif choice == "2":
            visualize_progress()

        elif choice == "3":
            calculate_totals()

        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the tracker
if __name__ == "__main__":
    main()
