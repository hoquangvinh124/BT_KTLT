import pandas as pd
import matplotlib.pyplot as plt

#(1) Visualize PVD's Debt over the years (Year, Liabilities)
df = pd.read_csv("PVD_Asset.csv")
plt.bar("Year", "Liabilities", data=df)
plt.xlabel("Year")
plt.ylabel("Liabilities")
plt.title("Nợ của PVD qua các năm")
plt.show()

#(2) Visualization of PVD's Capital over the years (Year, Equity):
plt.barh("Year", "Equity", data=df)
plt.xlabel("Year")
plt.ylabel("Equity")
plt.title("Vốn của PVD qua các năm")
plt.show()

#(3) Visualization of PVD's Assets from 2010-2020 (Year, Liabilities, Equity):
plt.bar('Year', 'Liabilities', data=df, color='orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color='darkgreen', label="Vốn")
plt.title("Tài sản của PVD từ 2010-2020")
plt.xlabel("Năm")
plt.ylabel("Tỷ đồng")
plt.legend()
plt.show()
