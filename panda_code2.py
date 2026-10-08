import pandas as pd
import numpy as np
df =pd.read_csv("day02_usage.csv")
apps = df[["Chat","Video","Study","Games"]].to_numpy()
print(apps.shape)
print(apps.sum(axis=1))
print(apps.sum(axis=0))
print(apps.max(axis=0),"max")
print(apps.min(axis=0),"min")
winner_position = np.argmax(apps, axis=1)
app_name = np.array(["Chat","Video","Study","Games"])
winner=app_name[winner_position]
print(winner)
app_won , count = np.unique(winner,return_counts=True)
x =np.unique(winner)
print(x)
for app, c in zip(app_won,count):
    print(app,c)

    

