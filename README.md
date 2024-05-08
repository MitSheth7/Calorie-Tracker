# Calorie-Tracker

This Python application is designed to help you track your daily nutrition intake. It allows you to add foods you've eaten throughout the day and visualize your nutrient consumption in relation to your goals.

## Features

- **Food Data Entry**: You can add a new food item by entering its name, calories, protein, fats, and carbs content.
- **Nutrition Goals**: The application has preset nutrition goals for calories, protein, fats, and carbs. You can modify these goals in the code to suit your personal needs.
- **Data Visualization**: The application provides four types of visualizations:
    - **Macronutrients Distribution (Pie Chart)**: Shows the percentage distribution of proteins, fats, and carbs in your diet.
    - **Macronutrients Distribution (Bar Chart)**: Compares your actual intake of proteins, fats, and carbs with your goals.
    - **Calories Goal Progress (Pie Chart)**: Shows the percentage of your calorie goal that you've consumed and what remains.
    - **Calories Goal Progress Over Time (Line Chart)**: Tracks your cumulative calorie intake over time against your calorie goal.

## Usage

To run the tracker, simply execute the script. You will be presented with a menu to add a new food or visualize your data. Enter the corresponding number to choose an option. Enter 'q' to quit the application.

## Dependencies

This application requires the following Python libraries:
- `dataclasses`
- `numpy`
- `matplotlib.pyplot`

We hope this application helps you in maintaining a healthy diet and achieving your nutrition goals!
