import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
files_df = pd.read_csv('2020.csv')
files_df.columns

print("TOP 10 - Highest Countries 2020")
print(files_df.groupby('Country name')['Ladder score'].sum().nlargest(10))
print("----------------------------------------")
print("TOP 10 - Lowest Happyness Countries 2020")
print(files_df.groupby('Country name')['Ladder score'].sum().nsmallest(10))
print("----------------------------------------")
a = float(files_df.groupby('Country name')['Ladder score'].sum().nlargest(1))
b = float(files_df.groupby('Country name')['Ladder score'].sum().nsmallest(1))
p = np.array([a, b])
tolabel = ["Happiest Countries" , "Lowest Happyness Countries" ]
letexplode = [0.1, 0]

plt.pie(p , labels= tolabel ,explode = letexplode , shadow = True)
plt.legend(title = "--- High/Low Ratio ---")
plt.show() 