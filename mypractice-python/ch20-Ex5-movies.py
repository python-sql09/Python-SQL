import json

# Load the dataset
filename = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/movies.json'
with open(filename, 'r') as file:
    movies_data = json.load(file)

# Question 1: How many movies are included in the file?
total_movies = len(movies_data)
print(f"Total number of movies: {total_movies}")

# Question 2: In what year was the movie 'A Separation' made?
a_separation_year = None
for movie in movies_data:
    if movie.get('title') == 'A Separation':
        a_separation_year = movie.get('year')
        break
print(f"The movie 'A Separation' was made in the year: {a_separation_year}")

# Question 3: How many movies has Martin Scorsese directed?
scorsese_movies_count = sum(1 for movie in movies_data if movie.get('director') == 'Martin Scorsese')
print(f"Number of movies directed by Martin Scorsese: {scorsese_movies_count}")

# Additional Questions
# Question 4: What is the average rating of movies in the dataset?
ratings = [movie.get('rating') for movie in movies_data if movie.get('rating') is not None]
average_rating = sum(ratings) / len(ratings) if ratings else 0
print(f"Average rating of movies: {average_rating:.2f}")

# Question 5: What is the highest-grossing movie in the dataset?
highest_grossing_movie = max(movies_data, key=lambda x: x.get('gross', 0))
print(f"Highest-grossing movie: {highest_grossing_movie.get('title')} with gross: ${highest_grossing_movie.get('gross')}")

# Question 6: How many movies were released in each genre?
genre_counts = {}
for movie in movies_data:
    genres = movie.get('genres', [])
    for genre in genres:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
print("Number of movies per genre:")
for genre, count in genre_counts.items():
    print(f"{genre}: {count}")

# Question 7: What is the most common release year for movies in the dataset?
from collections import Counter
release_years = [movie.get('year') for movie in movies_data if movie.get('year') is not None]
most_common_year = Counter(release_years).most_common(1)
print(f"Most common release year: {most_common_year[0][0]} with {most_common_year[0][1]} movies")