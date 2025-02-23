import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Housing.csv')
dat = df.sample(500)
sns.catplot(x='ocean_proximity',
            y='median_house_value',
            hue='ocean_proximity',
            data=dat,
            kind='box')
plt.show()

dat = df.sample(500)
sns.catplot(x='ocean_proximity',
            y='median_house_value',
            data=dat,
            hue='ocean_proximity',
            kind='point')
plt.show()

