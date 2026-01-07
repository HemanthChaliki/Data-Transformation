# Data Transformation

This Python project focuses on data cleaning, preprocessing, and transformation using real-world datasets. It showcases practical applications of regular expressions, pandas-based data manipulation, and data visualization with matplotlib.

## Overview

The project demonstrates essential data transformation techniques, including:
**Regular Expression Practice**
Hands-on exercises for pattern matching, text extraction, and string manipulation.
**Student Exam Data Processing**
Cleaning, restructuring, and preparing student performance data for analysis.
**US Census Data Analysis**
Cleaning demographic datasets and generating visual insights.

## KeyFeatures

- 11 regular expression exercises for text processing
- End-to-end data cleaning and preprocessing workflows
- Data reshaping (wide-to-long format conversion)
- Handling missing and inconsistent values
- Data type standardization and conversion
- Exploratory data visualization using matplotlib

## Requirements

```bash
pandas
numpy
matplotlib
```

## Usage

Run the main script:
```bash
python data_cleaning_and_preprocessing.py
```

Or import specific functions:
```python
from data_cleaning_and_preprocessing import load_student_data, clean_score_column
```

## Project Structure

- `data_cleaning_and_preprocessing.py` - Main optimized Python script
- `data/` - CSV data files (df1.csv, df2.csv, exams*.csv, states*.csv)
- `students*.py` - Intermediate processed student data files

## Data Processing Pipeline

1. Load and merge multiple CSV files
2. Transform data from wide to long format
3. Remove duplicate records
4. Split composite columns (e.g., gender_age, full_name)
5. Clean and standardize numerical and categorical fields (scores, grades)
6. Handle missing values and data inconsistencies

6. Handle missing values
