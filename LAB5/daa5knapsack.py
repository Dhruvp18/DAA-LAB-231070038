import csv
import random

# Class to represent an item in the knapsack
class Item:
    def __init__(self, weight, value, shelf_life):
        if weight <= 0:
            raise ValueError(f"Invalid weight: {weight}. Weight of an item cannot be zero or negative.")
        if value < 0:
            raise ValueError(f"Invalid value: {value}. Value of an item cannot be negative.")
        if shelf_life <= 0:
            raise ValueError(f"Invalid shelf life: {shelf_life}. Shelf life must be greater than zero.")
        self.weight = weight
        self.value = value
        self.shelf_life = shelf_life

    # Utility function to calculate the value to weight ratio
    def value_weight_ratio(self):
        return self.value / self.weight

    # Utility function to combine shelf life and value-weight ratio in comparison
    def priority(self):
        return (self.value_weight_ratio(), -self.shelf_life)  # Higher value-weight, lower shelf life prioritized

# Function to implement the fractional knapsack problem
def fractional_knapsack(capacity, items):
    if capacity <= 0:
        raise ValueError("Capacity of the knapsack must be greater than zero.")
    if len(items) == 0:
        raise ValueError("Item list cannot be empty.")

    # Sort items by priority: value-weight ratio (desc) and shelf life (asc)
    items.sort(key=lambda x: x.priority(), reverse=True)

    total_value = 0  # Total value accumulated
    current_weight = 0  # Current weight of the knapsack
    selected_items = []  # List to keep track of selected items

    for item in items:
        if current_weight + item.weight <= capacity:
            # Take the whole item
            current_weight += item.weight
            total_value += item.value
            selected_items.append((item.weight, item.value, item.shelf_life, item.value))  # Store selected item
        else:
            # Take fraction of the item
            remaining_capacity = capacity - current_weight
            fraction = remaining_capacity / item.weight
            fraction_value = item.value * fraction
            total_value += fraction_value
            selected_items.append((remaining_capacity, fraction_value, item.shelf_life, fraction_value))  # Store partial item
            break  # Knapsack is full

    return total_value, selected_items  # Return both total value and selected items

# Function to read items from CSV file
def read_items_from_csv(file_path):
    items = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                try:
                    weight = float(row[0])
                    value = float(row[1])
                    shelf_life = float(row[2])
                    items.append(Item(weight, value, shelf_life))
                except ValueError as e:
                    raise ValueError(f"Invalid data in CSV file: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file {file_path} not found.")

    return items

# Test case runner with error handling
def run_test_case(file_path, capacity):
    try:
        print(f"Processing file: {file_path}")

        # Read items from CSV
        items = read_items_from_csv(file_path)

        # Calculate and print the total knapsack value and selected items
        total_value, selected_items = fractional_knapsack(capacity, items)
        print(f"\nMaximum Knapsack Value: {total_value:.2f}")
        print("Selected Items (Weight, Value, Shelf Life, Value Contribution):")
        for weight, value, shelf_life, value_contribution in selected_items:
            print(f"Weight = {weight}, Value = {value:.2f}, Shelf Life = {shelf_life}, Value Contribution = {value_contribution:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Sample CSV file paths for positive and negative test cases
positive_test_files = ["positive_test_exact_1.csv", "positive_test_exact_2.csv", "positive_test_exact_3.csv"]
negative_test_files = ["negative_test_exact_1.csv", "negative_test_exact_2.csv", "negative_test_exact_3.csv"]

# Sample capacity
capacity = 200  # Knapsack capacity

# Run tests for positive and negative cases
print("Running Positive Test Cases:")
for file in positive_test_files:
    run_test_case(file, capacity)

print("\nRunning Negative Test Cases:")
for file in negative_test_files:
    run_test_case(file, capacity)
