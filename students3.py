import pandas as pd

students = pd.read_csv("data/students.csv")
students = students[['full_name', 'gender_age','fractions','probability','grade']]
students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')
students = students.drop_duplicates()