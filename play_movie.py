"""
Movie instances
"""
import movie
import fresh_tomatoes

# Movie model for Top Gun
TOP_GUN = movie.Movie(
    "Top Gun",
    "Top Gun is a 1986 American romantic military action drama film directed \
    by Tony Scott, and produced by Don Simpson and Jerry Bruckheimer, \
    in association with Paramount Pictures.",
    "https://www.youtube.com/watch?v=jqfXXaOisKo",
    "https://cdn.shopify.com/s/files/1/0580/0965/products/72dpi_Marko_Manev-Top_Gun_2_1024x1024.jpg"
)

# Movie model for Silence of the Lambs
LAMBS = movie.Movie(
    "Silence Of The Lambs",
    "The Silence of the Lambs is a 1991 American horror-thriller film \
    directed by Jonathan Demme and starring Jodie Foster, Anthony Hopkins, \
    and Scott Glenn.",
    "https://www.youtube.com/watch?v=QU8jKn7sMwU",
    "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg"
)

# Movie model for Chee and Chong
CHNCHO = movie.Movie(
    "Cheech and Chong",
    "Two stoners unknowingly smuggle a van - made entirely of marijuana - from \
    Mexico to L.A., with incompetent Sgt. Stedenko on their trail.",
    "https://www.youtube.com/watch?v=CWxgfTMLtc0",
    "https://s-media-cache-ak0.pinimg.com/736x/19/a7/26/19a726ab9bf06d65aaf12e04ece2fe5e.jpg"
)

# Movie model How To Train Your Dragon
DRAGON = movie.Movie(
    "How To Train Your Dragon",
    "A Viking breaks all rules and befriends a dragon he is supposed to \
    kill. He decides to call him Toothless. They join forces to put an \
    end to the terror that wreaks havoc in their respective worlds.",
    "https://www.youtube.com/watch?v=I-NDz9Z3qXg",
    "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg"
)

# Movie model The Godfather
GODFATHER = movie.Movie(
    "The Godfather",
    "Don Vito Corleone, head of a mafia family, decides to hand over \
    his empire to his youngest son Michael. However, his decision \
    unintentionally puts the lives of his loved ones in grave danger.",
    "https://www.youtube.com/watch?v=sY1S34973zA",
    "https://www.mugbug.co.uk/media/products/500/hmb.the_godfather.coaster.jpg"
)

# Movie model Neighbors
NEIGHBORS = movie.Movie(
    "Neighbors",
    "Mac and Kelly's peaceful suburban life is offset by a fraternity \
    house next door, which is inhabited by constantly partying college \
    students who refuse to be quiet no matter how hard the couple try.",
    "https://www.youtube.com/watch?v=kL5c2szf3E4",
    "https://www.movie2k-hd.com/wp-content/uploads/2016/05/1-24.jpg")

# List of movies to display
MOVIES = [TOP_GUN, LAMBS, CHNCHO, DRAGON, GODFATHER, NEIGHBORS]

# Opening web browser to show movies page
fresh_tomatoes.open_movies_page(MOVIES)
