import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import inv
import numpy as np

df = pd.read_csv('/home/macdev/Documents/MIAGE M2 COURS/DATAMINING WITH PYTHON/DATA/Humanité_Inclusion/benefs.csv')

idB = df.dropna()["Beneficiary ID"]
age = df.dropna()["Age"]
genre = df.dropna()["Gender"]
del age[144]
del idB[144]

print(age)
print(genre)

plt.title('Vue par âge de la population étudié')
plt.xlabel('Identifiant')
plt.ylabel('Âge')

plt.scatter(idB,age)
plt.show() 
