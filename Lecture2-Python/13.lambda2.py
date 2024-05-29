movies = [
    {"title": "Green Book", "year": 2018},
    {"title": "The Shape of Water", "year": 2017},
    {"title": "Moonlight", "year": 2016},
    {"title": "Spotlight", "year": 2015},
    {"title": "Birdman", "year": 2014},
    {"title": "12 Years a Slave", "year": 2013}
]

# def f(movie):
#     return movie["year"]

# movies.sort(key=f)
# print(movies)

movies.sort(key=lambda movie: movie["year"])
print(movies)

# for movie in movies:
#     print("{title} was released in {year}".format(**movie))
