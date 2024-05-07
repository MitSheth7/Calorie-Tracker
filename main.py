from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

# Define a class to track nutrition
class NutritionTracker:
    # Set the goal limits for various nutrients
    CALORIES_GOAL_LIMIT = 3000 
    PROTEIN_GOAL = 180
    FAT_GOAL = 80 
    CARBS_GOAL = 300

    # Define a dataclass to represent food
    @dataclass
    class Food:
        name: str
        calories: int
        protein: int
        fat: int
        carbs: int

    # Initialize the tracker with an empty list of foods for the day
    def __init__(self):
        self.today = []

    # Method to add a new food to the tracker
    def add_food(self):
        print("Adding a new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protein = int(input("Protein: "))
        fats = int(input("Fats: "))
        carbs = int(input("Carbs: "))
        food = self.Food(name, calories, protein, fats, carbs)
        self.today.append(food)
        print("Successfully Added!")

    # Method to visualize the data
    def visualize_data(self):
        # Calculate the sum of each nutrient
        calorie_sum = sum(food.calories for food in self.today)
        protein_sum = sum(food.protein for food in self.today)
        fats_sum = sum(food.fat for food in self.today)
        carbs_sum = sum(food.carbs for food in self.today)

        # Create subplots for the visualizations
        fig, axs = plt.subplots(2,2)

        # Create a pie chart for macronutrients distribution
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%1.1f%%")
        axs[0, 0].set_title("Macronutrients Distribution")

        # Create a bar chart for macronutrients distribution
        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [self.PROTEIN_GOAL, self.FAT_GOAL, self.CARBS_GOAL], width=0.4)
        axs[0, 1].set_title("Macronutrients Distribution")

        # Create a pie chart for calories goal progress
        axs[1, 0].pie([calorie_sum, self.CALORIES_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
        axs[1, 0].set_title("Calories Goal Progress")

        # Create a line chart for calories goal progress over time
        axs[1, 1].plot(list(range(len(self.today))), np.cumsum([food.calories for food in self.today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(self.today))), [self.CALORIES_GOAL_LIMIT] * len(self.today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 0].set_title("Calories Goal Progress Over Time")

        # Adjust layout and show the plot
        fig.tight_layout()
        plt.show()

    # Method to run the tracker
    def run(self):
        done = False
        while not done:
            print("""
            (1) Add a new food
            (2) Visualize data
            (q) Quit
            """)

            choice = input("Choose an option:")

            if choice == "1":
                self.add_food()
            elif choice == "2":
                self.visualize_data()
            elif choice == "q":
                done = True
            else: 
                print("Invalid Choice!")

# Run the tracker
if __name__ == "__main__":
    NutritionTracker().run()
