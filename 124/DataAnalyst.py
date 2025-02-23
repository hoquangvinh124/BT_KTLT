import pandas as pd

#Export Employee data to console screen
df = pd.read_csv("employee.csv")
print(df)

#Filter out Employees born in 2001
df["Dob"] = pd.to_datetime(df["Dob"], format="%d/%m/%Y")
df_born_in_2001 = df[(df["Dob"] >= "01/01/2001") & (df["Dob"] <= "31/12/2001")]
print()
print(df_born_in_2001)

#Export Top 3 Employees with oldest age
df_sorted_by_dob = df.sort_values(by="Dob", ascending=True)
print()
print(df_sorted_by_dob.head(3))

#Filter Employees have Tester role
df_filter_role = df[df["Role"] == "Tester"]
print()
print(df_filter_role)

#Count the number of Employees by Role
df_count_number_by_role = df["Role"].value_counts()
print()
print(df_count_number_by_role)