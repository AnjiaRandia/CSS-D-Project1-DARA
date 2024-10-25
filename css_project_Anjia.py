#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:11:11 2024

DARA PROJECT OPTION 1: IMDB Data
"""

import pandas as pd

df = pd.read_csv('/home/astrostudent1/DARA2024/movie_dataset.csv')
print(df.info())

# removing the spaces from the column names
df['Revenue_Millions'] = df["Revenue (Millions)"]
df['Runtime_mins'] = df["Runtime (Minutes)"]
df.drop(columns=["Revenue (Millions)","Runtime (Minutes)"], inplace=True)
print(df.info())

# removing duplicated if there are
df.drop_duplicates(inplace=True)


print("--------------------------------------------------------------------\n")

# Dealing with the nans 
# replacing metascore's nans into median value
print("min metascore: ", df["Metascore"].min())
print("max metascore: ", df["Metascore"].max())
print("mean metascore: ", df["Metascore"].median())

meta = df["Metascore"].mean()
df["Metascore"].fillna(meta, inplace=True)

# rreplacing revenue nans into mean value

print("min revenue: ", df["Revenue_Millions"].min())
print("max revenue: ", df["Revenue_Millions"].max())
print("mean revenue: ", df["Revenue_Millions"].mean())
print("\n")

revenue = df["Revenue_Millions"].mean()
df["Revenue_Millions"].fillna(revenue, inplace=True)

print(df.info())

print("----------------------------------------------------------------------------\n\n")






"""
THE PROJECT STARTS HERE

"""
# Highest rated movie
max_rating = df["Rating"].max()
highest_rated = df[df["Rating"] == max_rating]
print("The highest rated movie is:\n",highest_rated["Title"])

# Average revenue of all
avg_revenue = df["Revenue_Millions"].mean()

print("\nThe average revenue of all movies is: \n", avg_revenue," Millions")

# Average revenue of 2015 to 2017
t = df[df["Year"] >= 2015]
t = t[t["Year"]<=2017]

avg_revenue_2015 =  t["Revenue_Millions"].mean()
print("\nThe average revenue of the movies from 2015 to 2017 is:\n", avg_revenue_2015," Millions")

# numbers of movies released in 2016
num_2016 = df[df["Year"]==2016]["Year"].count()
print("\nThe number of movies reseased in 2016:\n",num_2016)

# number of movies directed by Christopher Nolan
nolan = df[df["Director"] == "Christopher Nolan"]

print("\nThe number of movies directed by Christopher Nolan:\n", nolan["Director"].count())

# number of movies with rating of at least 8.0
rating_8 = df[df["Rating"] >= 8.0]["Rating"].count()

print("\nThe number of movies with rating of at least 8.0:\n", rating_8)

# medium ratings of movies directed by Christopher Nolan
print("\nmedian rating of movies directed by Christopher Nolan:\n", nolan["Rating"].median())

# year with the highest average rating
Year_average_rating = df.groupby("Year")["Rating"].mean()#.idxmax()
highest_average = Year_average_rating[Year_average_rating == Year_average_rating.max()]

print("\nThe year with the highest average is:\n",highest_average)

# the percentage increase in number of movies made between 2006 and 2016
year_count = df.groupby("Year")["Title"].count()
percentage = (year_count[2016] - year_count[2006]) / year_count[2006]

# the most common actor in all the movies
df_replaced = df["Actors"].str.replace(', ',';')
df_replaced = df_replaced.str.replace(',',';')

df_replaced = pd.DataFrame(df_replaced)
df_replaced = df_replaced["Actors"].str.split(";").explode()

name_counts = df_replaced.value_counts()
most_actor = name_counts[name_counts == name_counts.max()]

print("\nThe most common actor in all the movies:\n",most_actor)

# unique genres are there in the datase

df_genre = df["Genre"].str.split(",").explode()

genre_counts = df_genre.value_counts().count()

print("\nThe number of genres:\n",genre_counts)



print("\n----------------------------------------------------------------------------\n\n")










