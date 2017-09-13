import webbrowser

# Class Movie contains 4 instance variables:
# Title, Storyline, Poster and Trailer
# And a method which opens the browser
# and shows the trailer of the movie


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
