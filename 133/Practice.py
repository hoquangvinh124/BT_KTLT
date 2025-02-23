import pandas as pd
import matplotlib.pyplot as plt

#1
dat = pd.read_csv('Salary_of_Developer.csv')
print(dat)

#2
plt.boxplot(dat)
plt.ylabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

#3
orange_square = dict(markerfacecolor='orange', marker='s')
plt.boxplot(dat, notch=True, flierprops=orange_square, vert=False)
plt.xlabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

