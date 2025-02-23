import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
sample_datasets = sns.get_dataset_names()
print(sample_datasets)

tips = sns.load_dataset("tips")
print(tips.head())

sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker', style='sex', size='size')
plt.show()

