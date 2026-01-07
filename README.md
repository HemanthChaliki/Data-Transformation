# Data Transformation

A Python project for data cleaning, preprocessing, and regular expression exercises using pandas and matplotlib.

## Overview

This project demonstrates data transformation techniques including:
- **Regular Expression Exercises**: Pattern matching and text processing examples
- **Student Data Processing**: Cleaning, reshaping, and preprocessing exam data
- **US Census Data Analysis**: Data cleaning and visualization of demographic data

## Features

- Regex pattern matching exercises (11 exercises)
- Data cleaning and preprocessing pipelines
- DataFrame reshaping (wide to long format)
- Missing value handling
- Data type conversions
- Data visualization with matplotlib

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

1. Load and concatenate multiple CSV files
2. Reshape data from wide to long format
3. Remove duplicates
4. Split composite columns (gender_age, full_name)
5. Clean and convert data types (scores, grades)
6. Handle missing values
