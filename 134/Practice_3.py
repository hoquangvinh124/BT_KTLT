import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Housing.csv')
dat = df.sample(400)
sns.scatterplot(x='housing_median_age',
                y='median_house_value',
                data=dat,
                hue='ocean_proximity',
                size='median_income')
plt.show()


dat = df.sample(1000)
sns.lineplot(x='housing_median_age',
             y='median_house_value',
             data=dat,
             hue='ocean_proximity')
plt.show()


dat = df.sample(500)
sns.catplot(x='ocean_proximity',
            y='median_house_value',
            kind='strip',
            data=dat)
plt.show()
