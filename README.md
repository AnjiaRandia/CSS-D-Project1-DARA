This repo was created to drop the codes for the CSS Projects, for the  CHPC-DARA Coding School 2024.

"css_project_option1_Anjia.py" is for the CSS-D option 1: IMDB DATA.\
"movie_dataset.csv" contains the data used in "css_project_option1_Anjia.py"

# CSS-D option 1: IMDB DATA.
The goal is to use Pandas in Python to clean and analyze a dataset about a certain number of movies and answer the following questions:
1. What is the highest rated movie in the dataset?
2. What is the average revenue of all movies in the dataset?
3. What is the average revenue of movies from 2015 to 2017 in the dataset?
4. How many movies were released in the year 2016?
5. How many movies were directed by Christopher Nolan?
6. How many movies in the dataset have a rating of at least 8.0?
7. What is the median rating of movies directed by Christopher Nolan?
8. What year has the highest average rating?
9. What is the percentage increase in number of movies made between 2006 and 2016?
10. Find the most common actor in all the movies?
11. How many unique genres are there in the dataset?

## movie_dataset.csv
Contains a dataset about a certain number of movies, with their ranks, title, genres, descriptions, actors, runtime, rating, votes, revenue and metascore.

## css_project_option1_Anjia.py
contains the python code used to answer the above questions.\
### Data Cleaning
- Renamed the "Revenue (Millions)" and "Runtime (Minutes)" to "Revenue_Millions" and "Runtime_mins" for a better reading
- Removed the duplicates in case there are some
- The NANs in the "Revenue_Millions" column were replaced with the mean value to get no errors when calculating the average revenues
- The NANs in the "Metascore" were replaced with the median value

