movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_high_rated():
  
    movie_name = input("Enter movie name: ")
    for movie in movies:
        if movie["name"] == movie_name:
            return movie["imdb"] > 5.5
    return False

def movies_by_category():
   
    category = input("Enter category: ")
    return [movie for movie in movies if movie["category"] == category]

def average_imdb():
    
    movie_names = input("Enter movie names separated by commas: ").split(", ")
    selected_movies = [movie for movie in movies if movie["name"] in movie_names]
    if not selected_movies:
        return 0
    return sum(movie["imdb"] for movie in selected_movies) / len(selected_movies)

def average_imdb_by_category():

    category = input("Enter category: ")
    category_movies = [movie for movie in movies if movie["category"] == category]
    return average_imdb(category_movies)

def high_rated_movies(movies):
    
    return [movie for movie in movies if is_high_rated(movie)]




print(high_rated_movies(movies))
print("----------------------")
print(is_high_rated())
print("----------------------")
print(movies_by_category())
print("----------------------")
print(average_imdb())
print("----------------------")
print(average_imdb_by_category())