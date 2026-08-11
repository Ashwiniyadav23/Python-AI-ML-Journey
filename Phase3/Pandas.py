# 1. DataFrames — the core data structure

import pandas as pd

data = {
    "name": ["Ashwini", "Raj", "Aisha"],
    "age": [19, 22, 20],
    "score": [88, 45, 72]
}

df = pd.DataFrame(data)
print(df.head())        # first 5 rows (useful for huge datasets)
print(df.shape)         # (3, 3) → 3 rows, 3 columns
print(df.columns)       # column names
print(df.info())        # data types, missing values, memory usage
print(df.describe())    # quick statistics: mean, std, min, max, etc. for numeric columns
print(df)



# 2. Cleaning — fixing messy real-world data

df_clean = df.drop_duplicates()
df["age"] = df["age"].astype(int)     # force a column to be integers
df = df.rename(columns={"score": "test_score"})



# 3. Merging — combining data from multiple tables

students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Ashwini", "Raj", "Aisha"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "score": [88, 45, 72]
})

merged = pd.merge(students, scores, on="student_id")
print(merged)


# 4. GroupBy — summarizing data by category

data = {
    "department": ["Sales", "Sales", "IT", "IT", "HR"],
    "salary": [50000, 55000, 70000, 72000, 45000]
}

df = pd.DataFrame(data)

avg_salary = df.groupby("department")["salary"].mean()
print(avg_salary)




# 5. Pivot Tables — reshaping data into a summary grid


data = {
    "student": ["Ashwini", "Ashwini", "Raj", "Raj"],
    "subject": ["Math", "Science", "Math", "Science"],
    "score": [90, 85, 60, 70]
}

df = pd.DataFrame(data)

pivot = df.pivot_table(values="score", index="student", columns="subject")
print(pivot)



# 6. Handling Missing Data


data = {
    "name": ["Ashwini", "Raj", "Aisha"],
    "score": [88, None, 72]
}

df = pd.DataFrame(data)

print(df.isnull())          # shows True/False for each cell — is it missing?
print(df.isnull().sum())    # counts missing values per column