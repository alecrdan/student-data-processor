# Student Performance Analysis

This Python script processes student data from a CSV file to analyze academic performance trends among computer science students. It filters the dataset, maps key academic metrics to a standardized scale, and calculates a **Student Performance Score (SPS)** based on GPA, attendance, and preparation levels.

## Features
- Reads student data from a CSV file.
- Filters out female students for analysis.
- Maps GPA values to a performance scale using interpolation.
- Computes a **Student Performance Score (SPS)** based on weighted academic factors.
- Outputs a sorted list of SPS scores.

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Install Dependencies
Clone the repository and install the required dependencies:
```bash
pip install numpy pandas
```

## Usage
1. Place your student dataset in `data/data.csv`.
2. Run the script:
```bash
python main.py
```
3. The processed dataset is saved as `data/comp_sci_student_data.csv`.
4. The computed **SPS scores** are printed in the console.

## File Structure
```
.
├── data/
│   ├── data.csv  # Raw dataset
│   ├── comp_sci_student_data.csv  # Processed data
├── main.py  # Main script
├── data.py  # Contains category mappings
└── README.md  # Project documentation
```

## Functions Overview
### `parse_data()`
- Reads and processes the dataset.
- Filters out female students.
- Selects relevant columns and saves a cleaned dataset.

### `get_gpa_value(gpa, gpa_dict)`
- Interpolates GPA scores based on predefined mappings.

### `getSPS(df)`
- Computes and normalizes the **Student Performance Score (SPS)**.

## Example Output
```
CSV file saved successfully as: data/comp_sci_student_data.csv
[6.75, 7.23, 7.89, 8.12, 8.94]
```

## License
This project is licensed under the MIT License.

## Author
[Alec Daniels](https://github.com/alecrdan)

