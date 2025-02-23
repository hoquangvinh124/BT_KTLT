import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Income.csv')
sns.jointplot(x='Income', y='Expenditure', data=df, color='orange')
plt.show()

sns.pairplot(df[['Income','Expenditure']])
plt.show()