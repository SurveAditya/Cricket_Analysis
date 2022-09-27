import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from soupsieve import match
import seaborn as sns


match_data = pd.read_csv(r'C:/Users/Aditya/OneDrive/Desktop/IPL Analysis/Match.csv')
ball_data = pd.read_csv(r'C:\Users\Aditya\OneDrive\Desktop\IPL Analysis\Ball.csv')

# First five data from the table
# print(match_data.head())
# print(ball_data.head())

# print(match_data.isnull().sum())
# print(ball_data.isnull().sum())

# print(match_data.shape)
# print(ball_data.shape)

# To inspect the number of columns in the match file
# print(match_data.columns)

# print("Matches played so far:",match_data.shape[0])

# Cities in which the matches are played and only the unique ones
# print('Cities played at:',match_data['city'].unique())

# Total number of teams participated so far
# print("Teams participated:",match_data['team1'].unique())

# Extracting year value from the date column and making a new column named Season
match_data['Season']=pd.DatetimeIndex(match_data['date']).year
# print(match_data['Season'])

# Total number of matches held in each season from 2008 to 2020
match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={"id":"matches"})
# print(match_per_season)

# Visualizing the result obtainded from the matches_per_season table
# sns.countplot(data=match_data, x='Season')
# plt.xticks(rotation=45,fontsize=10)
# plt.yticks(fontsize=10)
# plt.xlabel("Season",fontsize=10)
# plt.ylabel("Count",fontsize=10)
# plt.title("Total matches played in each season",fontsize=10,fontweight="bold")
# plt.show()

# Merging columns from matches dataframe to ball dataframe using a left join, joining using the common column id
season_data = match_data[['id','Season']].merge(ball_data,left_on="id",right_on="id",how="left").drop("id",axis=1)
# print(season_data.head())

# Visualizing total runs scored in each season
# season = season_data.groupby(['Season'])["total_runs"].sum().reset_index()
# p=season.set_index("Season")
# ax=plt.axes()
# ax.set(facecolor="black")
# sns.lineplot(data=p,palette="magma")
# plt.title("Total runs in each season",fontsize=12,fontweight="bold")
# plt.show()

# Visualizing number of tosses won by each teams
# toss=match_data['toss_winner'].value_counts()
# ax=plt.axes()
# ax.set(facecolor='black')
# sns.set(rc={'figure.figsize':(15,10)},style="darkgrid")
# ax.set_title("No of tosses won by each team",fontsize=15,fontweight="bold")
# sns.barplot(y=toss.index,x=toss,orient="h",palette="icefire",saturation=1)
# plt.xlabel('Number of tosses')
# plt.ylabel('Teams')
# plt.show()

# Visualising the toss decision 
# ax=plt.axes()
# ax.set(facecolor="black")
# sns.countplot(x="Season",hue="toss_decision",data=match_data,palette="magma",saturation=1)
# plt.xticks(rotation=90,fontsize=10)
# plt.yticks(fontsize=10)
# plt.xlabel('\n Season',fontsize=15)
# plt.ylabel("Count",fontsize=15)
# plt.title('Toss decision across seasons',fontsize=10,fontweight="bold")
# plt.show()

# The stadium best for winning by wickets =>Eden Garden (higher chances to wins if the team chooses to bat ball)
# print(match_data.venue[match_data.result!='runs'].mode())

# The stadium best for winning by runs =>Feroz Shah Kotla (higher chances to wins if the team chooses to bat first)
# print(match_data.venue[match_data.result!='wickets'].mode())

#For a particular team which stadium is best when they win the toss (Mumbai Indians => Wankhede Stadium(Home-Ground))
# print(match_data.venue[match_data.toss_winner=="Mumbai Indians"][match_data.winner=="Mumbai Indians"].mode())

#The team which has won most number of matches by batting second (Mumbai Indians and Kolkata Knight Riders)
# print(match_data.winner[match_data.result!="runs"].mode())

#The team which has won most number of matches by batting first (Mumbai Indians)
# print(match_data.winner[match_data.result!="wickets"].mode())

# Does winning the toss mean winning the match? (Conclusion=There is a high probability that if you win the toss you win the match)
# toss= match_data["toss_winner"] == match_data["winner"]
# plt.figure(figsize=(10,5))
# sns.countplot(toss)
# plt.show()

# Visualizing, choosing what has the most probability of winning (Conclusion=Field)
# plt.figure(figsize=(12,4))
# sns.countplot(match_data.toss_decision[match_data.toss_winner == match_data.winner])
# plt.show()

#Player Analysis

player = (ball_data["batsman"] == "SK Raina")
df_raina=ball_data[player]
df_raina.head()

# Visualizing in what way was the player dismissed most number of times(Conclusion=Caught Out)
# df_raina["dismissal_kind"].value_counts().plot.pie(autopct="%1.1f%%",shadow=True,rotatelabels=True)
# plt.title("Dismissal Kind",fontweight="bold",fontsize=15)
# plt.show()

#Runs scored by Suresh Raina in 1's 2's 3's 4's and 6's
# def count(df_raina,runs):
#     return len(df_raina[df_raina['batsman_runs']==runs])*runs

# print("Runs scored from Suresh Raina in 1's:",count(df_raina,1))
# print("Runs scored from Suresh Raina in 2's:",count(df_raina,2))
# print("Runs scored from Suresh Raina in 3's:",count(df_raina,3))
# print("Runs scored from Suresh Raina in 4's:",count(df_raina,4))
# print("Runs scored from Suresh Raina in 6's:",count(df_raina,6))

# Match Analysis
#Match won by highest margin (Match won by Mumbai against Delhi on 06-05-2017 and the result margin was 146 runs)
# print(match_data[match_data['result_margin']==match_data['result_margin'].max()])

#Highest number of runs scored by player so far in IPL (Virat Kohli has the highest runs so far)
runs = ball_data.groupby(["batsman"])["batsman_runs"].sum().reset_index()
runs.columns = ["Batsman","runs"]
y=runs.sort_values(by="runs",ascending=False).head(10).reset_index().drop("index",axis=1)


#Visualising top 10 players who have scored highest number of Runs
# ax=plt.axes()
# ax.set(facecolor="black")
# sns.barplot(x=y["Batsman"], y=y["runs"],palette="rocket",saturation=1)
# plt.xticks(rotation=90,fontsize=10)
# plt.yticks(fontsize=10)
# plt.xlabel("\n Player",fontsize=15)
# plt.ylabel("Total Runs",fontsize=15)
# plt.title("Top 10 run scorers in IPL",fontsize=15,fontweight="bold")
# plt.show()

#Visualising players with highest number of Man Of the Match( ABD Villers has the highest number of MOM)
ax=plt.axes()
ax.set(facecolor="black")
match_data.player_of_match.value_counts()[:10].plot(kind="bar")
plt.xlabel("Player",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.title("Highest MOM award winners",fontsize=15,fontweight="bold")
plt.show()