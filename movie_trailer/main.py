import movie
import fresh_tomatoes

# Shawshank movie: movie title, poster image and movie trailer
shawshank = movie.Movie(
    "Shawshank Redemption",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

# forest gump movie: movie title, poster image and movie trailer
forest_gump = movie.Movie(
    "Forrest Gump",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=uPIEn0M8su0")

# the theory of Everything movie: movie title, poster image and movie trailer
theory_of_everything = movie.Movie(
    "The Theory of Everything",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/Theory_of_Everything.jpg",
    "https://www.youtube.com/watch?v=Salz7uGp72c")

# Avatar movie: movie title, poster image and movie trailer
avatar = movie.Movie(
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# SAW 2004 movie: movie title, poster image and movie trailer
saw = movie.Movie(
    "Saw",
    "https://upload.wikimedia.org/wikipedia/en/5/56/Saw_official_poster.jpg",
    "https://www.youtube.com/watch?v=S-1QgOMQ-ls")

# the mist movie: movie title, poster image and movie trailer
mist = movie.Movie(
    "The Mist",
    "https://upload.wikimedia.org/wikipedia/en/a/a1/The_Mist_poster.jpg",
    "https://www.youtube.com/watch?v=LhCKXJNGzN8")

# set of movies to create the view list
movies = [
    shawshank,
    forest_gump,
    theory_of_everything,
    avatar,
    saw,
    mist]

# open the browser with the list of movies into HTML view
fresh_tomatoes.open_movies_page(movies)
