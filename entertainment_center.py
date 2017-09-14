import media
import fresh_tomatoes

# Objects of the Class Movie for 6 different movies.
# Each Object contains 4 values
# Title, Short Description, Poster URL and Trailer URL.

it = media.Movie('IT',
                 'A group of bullied kids band together when a shapeshifting'
				 'demon, taking the appearance of clown,'
				 'begins hunting children.',
                 'https://images-na.ssl-images-amazon.com/images/M/MV5BOTE0NWEyNDYtYWI5MC00MWY0LTg1NDctZjAwMjkyMWJiNzk1XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg',  # NOQA
                 'https://www.youtube.com/watch?v=FnCdOQsX5kc')

inception = media.Movie('Inception',
                        'A thief, who steals corporate secrets through use of'
						'dream-sharing technology, is given the inverse task'
						'of planting an idea into the mind of a CEO.',
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg',  # NOQA
                        'https://www.youtube.com/watch?v=zp_YGmAoht0')

bvs = media.Movie('Batman VS Superman : Dawn of Justice',
                  'Fearing that the actions of Superman are left unchecked,'
				  'Batman takes on the Man of Steel, while the world wrestles'
				  'with what kind of a hero it really needs.',
                  'https://images-na.ssl-images-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg',  # NOQA
                  'https://www.youtube.com/watch?v=bha24P9uw-E')

primer = media.Movie('Primer',
                     "Four friends/fledgling entrepreneurs, knowing that"
					 "there's something bigger and more innovative than"
					 "the differenterror-checking devices they've built,"
					 "wrestle over their new invention.",
                     'https://images-na.ssl-images-amazon.com/images/M/MV5BNjc3OWVjMTItYjc0Yi00NmFlLTk2YTgtYmU0MzcxMjBkNTYxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg',  # NOQA
                     'https://www.youtube.com/watch?v=3nj5MMURCm8')

js21 = media.Movie('21 Jump Street',
                   'A pair of underachieving cops are sent back to a local'
				   'high school to blend in and bring down a'
				   'synthetic drug ring.',
                   'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3NzQ3OTg3NF5BMl5BanBnXkFtZTcwMjk5OTcxNw@@._V1_QL50_.jpg',  # NOQA
                   'https://www.youtube.com/watch?v=RLoKtb4c4W0')

gethard = media.Movie('Get Hard',
                      'When millionaire James King is jailed for fraud and'
					  'bound for San Quentin, he turns to Darnell Lewis to'
					  'prep him to go behind bars.',
                      'http://t3.gstatic.com/images?q=tbn:ANd9GcTjHKnkJIervPeDr4hMJJUnouG18n4zCYyyoNrNK0iujBxNDbqo',  # NOQA
                      'https://www.youtube.com/watch?v=lEqrpuU9fYI')

# Array/List to hold all the Movie objects

movies_list = [
    it,
    inception,
    bvs,
    primer,
    js21,
    gethard,
]

# open_movies_page is a method imported from fresh_tomatoes.py which takes in a
# single argument which is a list of Movie objects and create
# an html page with the list of movies

fresh_tomatoes.open_movies_page(movies_list)
