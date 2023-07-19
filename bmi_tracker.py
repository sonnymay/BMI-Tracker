import datetime
import csv

# BMI categories
categories = {
    "Underweight": (0, 18.5),
    "Normal weight": (18.5, 25),
    "Overweight": (25, 30),
    "Obesity": (30, float("inf"))
}

def calculate_bmi(weight, height):
    """
    Calculates BMI given weight (kg) and height (m)
    """
    return weight / (height ** 2)

def bmi_category(bmi):
    """
    Determine the category of BMI
    """
    for category, (lower, upper) in categories.items():
        if lower <= bmi < upper:
            return category

def track_bmi(weight, height):
    """
    Track and save BMI given weight and height
    """
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    date = datetime.datetime.now().date()

    # Save to CSV file
    with open("bmi_tracker.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, weight, height, bmi, category])

    print(f"Date: {date}, Weight: {weight}, Height: {height}, BMI: {bmi:.2f}, Category: {category}")

if __name__ == "__main__":
    # Sample input
    track_bmi(70, 1.75) # weight in kg, height in m