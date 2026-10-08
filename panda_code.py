import pandas as pd
import numpy as np

df =pd.read_csv("day02_usage.csv")
chat=df["Chat"].to_numpy()
video=df["Video"].to_numpy()
study=df["Study"].to_numpy()
games=df["Games"].to_numpy()
print(len(chat),len(video),len(study),len(games))
chat_minutes=chat.sum()
video_minutes=video.sum()
study_minutes=study.sum()
games_minutes=games.sum()
print("Total minutes spent on Chat:",chat_minutes)
print("Total minutes spent on Video:",video_minutes)
print("Total minutes spent on Study:",study_minutes)
print("Total minutes spent on Games:",games_minutes)
avg_chat=chat.mean().round(2)
avg_video=video.mean().round(2)
avg_study=study.mean().round(2)
avg_games=games.mean().round(2)
print(avg_chat,avg_video,avg_study,avg_games)
study_minus_games=study-games
best_day=np.argmax(study_minus_games)
worst_day=np.argmin(study_minus_games)
print("Best day (Study - Games):",best_day)
print("Worst day (Study - Games):",worst_day)
names=["Chat","Video","Study","Games"]
winners=[]

for i in range(len(chat)):
    day_values=[chat[i],video[i],study[i],games[i]]
    best=0
    for j in range(1,4):
        if day_values[j]>day_values[best]:
            best=j
winners.append(names[best])
app_totals=chat+video+study+games
chat_share=(chat/app_totals)*100
video_share=(video/app_totals)*100
study_share=(study/app_totals)*100  
games_share=(games/app_totals)*100
print(chat_share[1])
print(video_share[1])
print(study_share[1])
print(games_share[1])