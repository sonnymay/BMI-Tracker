# BMI-Tracker

Welcome to the BMI Tracker project! This simple Python-based tool was created by Sonnymay to help individuals monitor their Body Mass Index (BMI) over time.

## Introduction

The Body Mass Index (BMI) is a simple calculation using a person's height and weight. This project calculates BMI and classifies it into categories such as "Underweight", "Normal weight", "Overweight", and "Obesity" as defined by the World Health Organization. The results, along with the current date, are saved to a CSV file, allowing the user to track changes over time.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository or download the `bmi_tracker.py` script.
2. Run the script using Python and provide your weight (in kilograms) and height (in meters) as inputs to the `track_bmi` function at the bottom of the script.

```python
if __name__ == "__main__":
    track_bmi(70, 1.75)  # replace with your weight and height
```

3. The calculated BMI, its category, and the current date will be saved in a file named `bmi_tracker.csv` in the same directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Author

- Sonnymay


