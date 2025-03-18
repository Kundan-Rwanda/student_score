# Generate Large Student Dataset

## Overview
This repository contains a Python script that generates a large dataset of student scores and saves it as a CSV file. The dataset is generated in chunks to efficiently handle memory usage while writing a large number of records.

## Features
- Generates a dataset with **30 million** student records (adjustable as needed).
- Saves the data in chunks to optimize performance and memory usage.
- Includes fields such as student ID, name, assignments, practicals, midterm, and final exam scores.
- Introduces some missing values randomly for realistic data simulation.

## File Structure
- `generate_large_dataset.py` - Python script to generate the dataset.
- `generate_large_dataset.ipynb` - Jupyter Notebook Python script to generate the dataset. 
- `large_student_scores.csv` - Generated CSV file (1GB+ in size, based on 30Millions records).

## How to Run the Script
### Prerequisites
Ensure you have Python installed with the following libraries:
- `pandas`
- `numpy`

### Execution Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. install required dependencies:
   ```sh
   pip install pandas numpy

3. Run the script:
   ```sh
   python generate_large_dataset.py


4. The dataset large_student_scores.csv will be created in the same directory.

# Student Performance Dataset

## Dataset Structure

The generated CSV file contains the following columns:

| Column Name           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **No**                | Record number (1 to N)                                                      |
| **Regno**             | Unique student registration number                                           |
| **Names**             | Student name (e.g., Student1234567)                                          |
| **Assign1/10**        | Assignment 1 score (random 7, 8, 9 or null)                                 |
| **Assign2/10**        | Assignment 2 score (random 7, 8, 9 or null)                                 |
| **Practical/10**      | Practical score (random 4, 5, 6 or null)                                    |
| **MidTerm Exam/30**   | Midterm exam score (random 10-30 or null)                                   |
| **Final Exam/40**     | Final exam score (random 20-40 or null)                                     |

## Performance Considerations

- The script writes data in chunks of 100,000 records to reduce memory usage.
- Appending to the file prevents memory overload when handling large datasets.

## License

Open Source: Please down the script and modified as per your requirement.

## Author

Developed by Kundan Kumar


