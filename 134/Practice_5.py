import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(10)
dat = np.random.normal(12, 2, 400)
sns.displot(dat, kde=True, color='r')
plt.xlabel('Salary')
plt.show()

df = pd.read_csv('Income.csv')
sns.regplot(x='Income', y='Expenditure', data=df)
plt.show()

flights_long = sns.load_dataset('flights')
flights = flights_long.pivot(index='month', columns='year', values='passengers')
sns.heatmap(flights, annot=True, fmt='d', linewidths=.5)
plt.show()
