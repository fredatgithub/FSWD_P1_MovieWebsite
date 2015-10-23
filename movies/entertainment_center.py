import media, fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

fifth_element = media.Movie(
    "The Fifth Element",
    "A lady made from aliens saves the world by kissing Bruce Willis",
    "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
    "https://www.youtube.com/watch?v=aB-AUTGqUCU"
)

matrix = media.Movie(
    "The Matrix",
    "A guy learns how to beat up computer programs",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8"
)

pacific_rim = media.Movie(
    "Pacific Rim",
    "Giant robots fight giant monsters",
    "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
    "https://www.youtube.com/watch?v=5guMumPFBag"
)

movies = [toy_story, avatar, fifth_element, matrix, pacific_rim]

fresh_tomatoes.open_movies_page(movies)
