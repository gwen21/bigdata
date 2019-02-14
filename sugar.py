import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IOD_BU_202_FR.csv')

x = df.dropna()["Annee"]
y = df.dropna()["Cout de production au kg du sucre"]

print(x)
print(y)
plt.plot(x, y)
plt.show()
