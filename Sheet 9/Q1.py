# Creating the list
movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]

# I
most_favorite_movie = movies[0]
least_favorite_movie = movies[4]
print(f"Most favorite movie (using indexing): {most_favorite_movie}")
print(f"Least favorite movie (using indexing): {least_favorite_movie}")

# II
most_favorite_movie_negative = movies[-len(movies)]
least_favorite_movie_negative = movies[-1]
print(f"Most favorite movie (using negative indexing): {most_favorite_movie_negative}")
print(f"Least favorite movie (using negative indexing): {least_favorite_movie_negative}")

# III
movies.append("Water World")

# IV
print("Updated list of movies:")
print(movies)

# V
total_movies = len(movies)
print(f"Total number of movies in the list: {total_movies}")
