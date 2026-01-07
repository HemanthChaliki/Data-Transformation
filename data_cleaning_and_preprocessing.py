"""
Data Cleaning and Preprocessing Script
Optimized conversion from Jupyter notebook
"""

import re
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


# ============================================================================
# REGULAR EXPRESSION EXERCISES
# ============================================================================

def test_regex_pattern(pattern, strings, use_search=False):
    """
    Test a regex pattern against a list of strings.
    
    Args:
        pattern: Regular expression pattern
        strings: List of strings to test
        use_search: If True, use re.search instead of re.match
    """
    for s in strings:
        if use_search:
            match = re.search(pattern, s)
        else:
            match = re.match(pattern, s)
        
        if match:
            print(f"Match: {s}")
        else:
            print(f"Don't match: {s}")


def exercise_1():
    """Test basic pattern matching."""
    pattern = "bark"
    strings = ['bark', 'baa', 'bellow', 'boom']
    test_regex_pattern(pattern, strings)


def exercise_2():
    """Test pattern with parentheses (literal match)."""
    pattern = "(cat,dog)"
    strings = ['dog', 'cat', 'bellow']
    test_regex_pattern(pattern, strings)


def exercise_3():
    """Test character class pattern."""
    pattern = "[chr]at"
    strings = ['cat', 'hat', 'rat', 'eat', 'mat', 'sat']
    test_regex_pattern(pattern, strings)


def exercise_4():
    """Test word boundary and dot pattern."""
    pattern = r"\w+\."
    strings = ['bear.', 'lion.', 'orca.', 'mouse', 'koala', 'snail']
    test_regex_pattern(pattern, strings)


def exercise_5():
    """Test character range pattern."""
    pattern = r"[c-e][uol][b-k]"
    strings = ['cub', 'dog', 'elk', 'ape', 'cow', 'ewe']
    test_regex_pattern(pattern, strings)


def exercise_6():
    """Test digit and whitespace pattern."""
    pattern = r"\d\s\w+"
    strings = ['5 sloths', '8 llamas', '7 hyenas', 'one bird', 'two owls']
    test_regex_pattern(pattern, strings)


def exercise_7():
    """Test alternation pattern."""
    pattern = r"(puppies|kitty cats) are my favorite!"
    strings = [
        'puppies are my favorite!',
        'kitty cats are my favorite!',
        'deer are my favorite!',
        'otters are my favorite!',
        'hedgehogs are my favorite!'
    ]
    test_regex_pattern(pattern, strings, use_search=True)


def exercise_8():
    """Test quantifier pattern."""
    pattern = r"squea{3,5}k"
    strings = ['squeaaak', 'squeaaaak', 'squeaaaaak', 'squeak', 'squeaak', 'squeaaaaaak']
    test_regex_pattern(pattern, strings, use_search=True)


def exercise_9():
    """Test optional quantifier pattern."""
    pattern = r'\d\sducks? for adoption\?'
    strings = ["1 duck for adoption?", "5 ducks for adoption?", "7 ducks for adoption?"]
    for string in strings:
        if re.match(pattern, string):
            print(f"Match: {string}")
        else:
            print(f"No match: {string}")


def exercise_10():
    """Test one or more quantifier pattern."""
    pattern = r'hoo+t'
    strings_to_match = ["hoot", "hoooooot", "hooooooooooot"]
    strings_not_to_match = ["hot", "hoat", "hoo"]
    
    for string in strings_to_match:
        if re.match(pattern, string):
            print(f"Match: {string}")
    
    for string in strings_not_to_match:
        if not re.match(pattern, string):
            print(f"No match: {string}")


def exercise_11():
    """Test anchor patterns."""
    pattern = r'^penguins are cooler than regular expressions$'
    strings = [
        "penguins are cooler than regular expressions",
        "king penguins are cooler than regular expressions",
        "penguins are cooler than regular expressions!"
    ]
    for string in strings:
        if re.match(pattern, string):
            print(f"Match: {string}")
        else:
            print(f"No match: {string}")


# ============================================================================
# DATA CLEANING AND PREPROCESSING EXERCISES
# ============================================================================

def load_and_explore_dataframes():
    """Load and explore df1.csv and df2.csv."""
    df1 = pd.read_csv("data/df1.csv")
    df2 = pd.read_csv("data/df2.csv")
    
    print("df1 head:")
    print(df1.head())
    print("\ndf2 head:")
    print(df2.head())
    print("\ndf1 info:")
    print(df1.info())
    print("\ndf2 info:")
    print(df2.info())
    print("\ndf1 describe:")
    print(df1.describe())
    print("\ndf2 describe:")
    print(df2.describe())
    print("\ndf1 columns:")
    print(df1.columns)
    print("\ndf2 columns:")
    print(df2.columns)
    
    print("\ndf1 value counts:")
    print(df1['Grocery Item'].value_counts())
    print("\ndf2 value counts:")
    print(df2['Grocery Item'].value_counts())
    
    return df1, df2


def load_student_data():
    """Load and concatenate student exam files."""
    student_files = glob.glob("data/exams*.csv")
    print(f"Found {len(student_files)} student files")
    
    df_list = []
    for filename in student_files:
        data = pd.read_csv(filename)
        df_list.append(data)
    
    students = pd.concat(df_list, ignore_index=True)
    print(f"Combined shape: {students.shape}")
    print(students.head())
    
    return students


def reshape_student_data(students):
    """Reshape student data from wide to long format."""
    students = pd.melt(
        students,
        id_vars=['full_name', 'gender_age', 'grade'],
        value_vars=['fractions', 'probability'],
        var_name='exam',
        value_name='score'
    )
    print(f"Reshaped shape: {students.shape}")
    print(students.head())
    print(f"\nExam value counts:\n{students.exam.value_counts()}")
    return students


def remove_duplicates(students):
    """Remove duplicate rows from student data."""
    duplicates = students.duplicated()
    print(f"Duplicate rows: {duplicates.value_counts()}")
    
    students = students.drop_duplicates()
    print(f"After removing duplicates: {students.shape}")
    
    # Verify no duplicates remain
    remaining_duplicates = students.duplicated()
    assert not any(remaining_duplicates), "Duplicates still exist!"
    
    return students


def split_gender_age(students):
    """Split gender_age column into separate gender and age columns."""
    students['gender'] = students['gender_age'].str[0]
    students['age'] = students['gender_age'].str[1:]
    students = students.drop(columns=['gender_age'])
    print(students.head())
    return students


def split_full_name(students):
    """Split full_name into first_name and last_name."""
    name_split = students['full_name'].str.split(' ')
    students['first_name'] = name_split.str.get(0)
    students['last_name'] = name_split.str.get(1)
    print(students.head())
    return students


def clean_score_column(students):
    """Remove percentage signs and convert score to numeric."""
    students['score'] = students['score'].str.replace('%', '', regex=True)
    students['score'] = pd.to_numeric(students['score'], errors='coerce')
    print(f"Sample score value: {students.score.iloc[0]}")
    return students


def clean_grade_column(students):
    """Extract numeric grade from grade column."""
    students['grade'] = students['grade'].str.extract('(\d+)')[0]
    students['grade'] = pd.to_numeric(students['grade'])
    avg_grade = students['grade'].mean()
    print(f"Average grade: {avg_grade:.2f}")
    return students


def handle_missing_scores(students):
    """Fill missing scores with 0 and compare means."""
    score_mean_before = students['score'].mean()
    students['score'] = students['score'].fillna(0)
    score_mean_after = students['score'].mean()
    
    print(f"Mean score before filling: {score_mean_before:.2f}")
    print(f"Mean score after filling: {score_mean_after:.2f}")
    return students


def process_us_census_data():
    """Load and process US census data."""
    files = glob.glob("data/states*.csv")
    df_list = []
    
    for filename in files:
        data = pd.read_csv(filename)
        df_list.append(data)
    
    us_census = pd.concat(df_list, ignore_index=True)
    print(f"Columns: {us_census.columns.tolist()}")
    print(f"\nData types:\n{us_census.dtypes}")
    
    # Clean Income column
    us_census['Income'] = us_census['Income'].str.replace('[\$,]', '', regex=True).astype(float)
    
    # Split GenderPop into Men and Women
    us_census[['Men', 'Women']] = us_census['GenderPop'].str.split('_', expand=True)
    us_census['Men'] = us_census['Men'].str.rstrip('M').astype(float)
    us_census['Women'] = us_census['Women'].str.rstrip('F').astype(float)
    
    # Fill missing Women values
    us_census['Women'] = us_census['Women'].fillna(
        us_census['TotalPop'] - us_census['Men']
    )
    
    # Remove duplicates
    us_census = us_census.drop_duplicates()
    
    # Create scatter plot
    plt.scatter(us_census['Women'], us_census['Income'])
    plt.xlabel('Proportion of Women')
    plt.ylabel('Average Income')
    plt.title('Average Income vs Proportion of Women')
    plt.show()
    
    # Clean percentage columns
    percentage_columns = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
    for col in percentage_columns:
        us_census[col] = us_census[col].str.rstrip('%').astype(float)
    
    # Create histograms
    plt.figure(figsize=(12, 8))
    for idx, col in enumerate(percentage_columns, 1):
        plt.subplot(2, 3, idx)
        plt.hist(us_census[col], bins=20, edgecolor='k')
        plt.title(f'{col} Population (%)')
    
    plt.tight_layout()
    plt.show()
    
    return us_census


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("=" * 70)
    print("REGULAR EXPRESSION EXERCISES")
    print("=" * 70)
    
    # Run regex exercises (commented out by default)
    # Uncomment to run specific exercises
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    # exercise_9()
    # exercise_10()
    # exercise_11()
    
    print("\n" + "=" * 70)
    print("DATA CLEANING AND PREPROCESSING")
    print("=" * 70)
    
    # Load and explore dataframes
    df1, df2 = load_and_explore_dataframes()
    
    # Process student data
    print("\n" + "-" * 70)
    print("Loading student data...")
    students = load_student_data()
    
    print("\n" + "-" * 70)
    print("Reshaping student data...")
    students = reshape_student_data(students)
    
    print("\n" + "-" * 70)
    print("Removing duplicates...")
    students = remove_duplicates(students)
    
    print("\n" + "-" * 70)
    print("Splitting gender_age column...")
    students = split_gender_age(students)
    
    print("\n" + "-" * 70)
    print("Splitting full_name column...")
    students = split_full_name(students)
    
    print("\n" + "-" * 70)
    print("Cleaning score column...")
    students = clean_score_column(students)
    
    print("\n" + "-" * 70)
    print("Cleaning grade column...")
    students = clean_grade_column(students)
    
    print("\n" + "-" * 70)
    print("Handling missing scores...")
    students = handle_missing_scores(students)
    
    print("\n" + "-" * 70)
    print("Final student data shape:", students.shape)
    print("Final student data columns:", students.columns.tolist())
    
    # Process US census data
    print("\n" + "=" * 70)
    print("US CENSUS DATA PROCESSING")
    print("=" * 70)
    us_census = process_us_census_data()
    
    print("\n" + "=" * 70)
    print("PROCESSING COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
