import pandas as pd

#Export all Sales data to the console screen
df = pd.read_excel("Sales.xlsx")
print(df)

#Statistics of the week with the highest Sales_Volume
max_sales_week = df[df['Sales_Volume'] == df['Sales_Volume'].max()]
print()
print(max_sales_week)
print()

#Print the weeks with Sales_Volume from X to Y, with X, Y get from keyboard
X = int(input("Enter X: "))
Y = int(input("Enter Y: "))
filtered_weeks = df[(df['Sales_Volume'] >= X) & (df['Sales_Volume'] <= Y)]
print(filtered_weeks)

#Print the week with the lowest Ads_Cost
min_ads_cost_week = df[df['Ads_Cost'] == df['Ads_Cost'].min()]
print()
print(min_ads_cost_week)
