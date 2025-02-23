import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dat = pd.read_csv('Income.csv')
print(dat)
sns.relplot(x='Income', y='Expenditure', data=dat, kind='scatter')
plt.show()

sns.relplot(x='Income', y='Expenditure', data=dat, kind='line')
plt.show()