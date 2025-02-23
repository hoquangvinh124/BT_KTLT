import pandas as pd

# 1) Print all data to the console screen
df = pd.read_csv("SampleData_NaN.csv")
print(df)

# 2) Print all data but replace EMPTY (NaN) values with TRUE
df_replace_true = df.fillna(True)
print(df_replace_true)

# 3) Check the number of empty data for the entire DataFrame
empty_count = df.isna().sum().sum()
print(f"\n{empty_count}\n")

#4) Write a command to delete rows containing empty elements
df_dropna = df.dropna()
print(df_dropna)

#5) Enter a value to replace empty cells
user_input = input("Enter a value to replace empty cells: ")
df_fill_user = df.fillna(float(user_input))
print(df_fill_user)

#6) Write a command to fill in replacement values for empty elements using bfill, ffill and interpolate methods
df_bfill = df.bfill()
df_ffill = df.ffill()
df_interp = df.infer_objects().interpolate()

print("Data using bfill:\n", df_bfill, "\n")
print("Data using ffill:\n", df_ffill, "\n")
print("Data using interpolate:\n", df_interp, "\n")
