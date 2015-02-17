import fresh_tomatoes
import movie

"""
Create Movie Objects
Movie data is hard coded here
"""
pulp_fiction = movie.Movie("Pulp Fiction",
                           "(1994)",
                           "What's in the case?",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")

reservoir_dogs = movie.Movie("Reservoir Dogs",
                             "(1992)",
                             "A colorful story about a botched bank heist",
                             "http://ia.media-imdb.com/images/M/MV5BMTQxMTAwMDQ3Nl5BMl5BanBnXkFtZTcwODMwNTgzMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=vayksn4Y93A")

true_romance = movie.Movie("True Romance",
                           "(1993)",
                           "Who says romance is dead?",
                           "http://ia.media-imdb.com/images/M/MV5BMTMxMTM3MDIwM15BMl5BanBnXkFtZTcwMDYyOTUyMg@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=_wNYNDzKpuQ")

the_godfather = movie.Movie("The Godfather",
                            "(1972)",
                           "Every time he tries to get out, they pull him back in",
                           "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=YBrs0wvkPls")

the_princess_bride = movie.Movie("The Princess Bride",
                                 "(1987)",
                                 "Hello. My name is Inigo Montoya. You killed my father. Prepare to die",
                                 "http://ia.media-imdb.com/images/M/MV5BMTkzMDgyNjQwM15BMl5BanBnXkFtZTgwNTg2Mjc1MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                                 "https://www.youtube.com/watch?v=VYgcrny2hRs")

holy_grail = movie.Movie("Monty Python and the Holy Grail",
                         "(1975)",
                         "Supreme executive power derives from a mandate from the masses, not some farcical aquatic ceremony",
                         "http://ia.media-imdb.com/images/M/MV5BMTkzODczMTgwM15BMl5BanBnXkFtZTYwNTAwODI5._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=LG1PlkURjxE")

movies = [pulp_fiction, reservoir_dogs, true_romance, the_godfather, the_princess_bride, holy_grail]
# Generate html page displaying movies
fresh_tomatoes.open_movies_page(movies)
