"""
Create a dictionary of n people where key is name and value is city
Task1: Display all names
Task2: Display all cities names
Task3: Display student name and city of all students
Task4: Count number of students in each city
"""

def student_details(n):
    student = {}
    
    for i in range(n):
        name = input("Enter name: ")
        city = input("Enter city: ")
        student[name] = city
    
    print("Names:", list(student.keys()))
    print("Cities:", list(student.values()))
    print("Student Details:", student)
    
    city_count = {}
    for city in student.values():
        city_count[city] = city_count.get(city, 0) + 1
    print("City Count:", city_count)

n = int(input("Enter number of students: "))
student_details(n)

#---------------------------------------------------------------------------------------

"""Create a dictionary of n movies
movie - name, year, director, production cost, collection made
movie details:
Display name of movies released before 2020
Print movie that made profit
Print movie directed by a perticular director"""

# def format_currency(value):
#     if value >= 1e7:
#         return f"{value / 1e7:.2f} Cr"
#     elif value >= 1e5:
#         return f"{value / 1e5:.2f} Lakh"
#     elif value >= 1e3:
#         return f"{value / 1e3:.2f} Thousand"
#     else:
#         return f"{value:.2f}" 

# def movie_details(n):
#     movies = {}

#     for i in range(n):
#         name = input("Enter movie name: ")
#         year = int(input("Enter year: "))
#         director = input("Enter director: ")
#         production_cost = float(input("Production cost: "))
#         collection = float(input("Collection made: "))

#         movies[name] = {
#             'year': year,
#             'director': director,
#             'production_cost': format_currency(production_cost),
#             'collection_made': format_currency(collection),
#             'profit': format_currency(collection - production_cost)
#         }

#     print("\nMovies released before 2020:")
#     for name, details in movies.items():
#         if details['year'] < 2020:
#             print(name)

#     print("\nMovies that made profit:")
#     for name, details in movies.items():
#         if collection - production_cost > 0:
#             print(name)

#     director_name = input("\nEnter director name to filter movies: ")
#     print(f"\nMovies directed by {director_name}:")
#     for name, details in movies.items():
#         if details['director'] == director_name:
#             print(name)

# n = int(input("Enter number of movies: "))
# movie_details(n)

# print("\nFinal dictionary of movies:")
# print(movie_details)