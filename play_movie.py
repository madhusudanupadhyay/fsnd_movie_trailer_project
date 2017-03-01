"""
Movie instances
"""
import movie
import fresh_tomatoes

TOP_GUN = movie.Movie(
    "Top Gun",
    "Top Gun is a 1986 American romantic military action drama film directed \
    by Tony Scott, and produced by Don Simpson and Jerry Bruckheimer, \
    in association with Paramount Pictures. The screenplay was written by \
    Jim Cash and Jack Epps, Jr., and was inspired by an article titled \
    Top Guns published in California magazine three years earlier. \
    The film stars Tom Cruise, Kelly McGillis, Val Kilmer, \
    Anthony Edwards, and Tom Skerritt. Cruise plays Lieutenant \
    Pete Maverick Mitchell, a young Naval aviator aboard the aircraft \
    carrier USS Enterprise. He and his Radar Intercept Officer (RIO) \
    Nick Goose Bradshaw (Edwards) are given the chance to train at the \
    Navy's Fighter Weapons School at Miramar in San Diego.",
    "https://www.youtube.com/watch?v=jqfXXaOisKo",
    "https://cdn.shopify.com/s/files/1/0580/0965/products/72dpi_Marko_Manev-Top_Gun_2_1024x1024.jpg"
)

LAMBS = movie.Movie(
    "Silence Of The Lambs",
    "The Silence of the Lambs is a 1991 American horror-thriller film \
    directed by Jonathan Demme and starring Jodie Foster, Anthony Hopkins, \
    and Scott Glenn.[3] Adapted by Ted Tally from the 1988 novel of the same \
    name by Thomas Harris, his second to feature the character of Dr. \
    Hannibal Lecter; a brilliant psychiatrist and cannibalistic serial \
    killer, the film was the second adaptation of a Harris novel featuring \
    Lecter, preceded by the Michael Mann-directed Manhunter in 1986. \
    In the film, Clarice Starling, a young U.S. FBI trainee, seeks the \
    advice of the imprisoned Dr. Lecter to apprehend another serial \
    killer, known only as Buffalo Bill",
    "https://www.youtube.com/watch?v=QU8jKn7sMwU",
    "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg"
)

CHNCHO = movie.Movie(
    "Chee and chong",
    "Movie about two friends on a journey with weed",
    "https://www.youtube.com/watch?v=CWxgfTMLtc0",
    "https://s-media-cache-ak0.pinimg.com/736x/19/a7/26/19a726ab9bf06d65aaf12e04ece2fe5e.jpg"
)

DRAGON = movie.Movie(
    "How To Train Your Dragon",
    "A Viking breaks all rules and befriends a dragon he is supposed to \
    kill. He decides to call him Toothless. They join forces to put an \
    end to the terror that wreaks havoc in their respective worlds.",
    "https://www.youtube.com/watch?v=I-NDz9Z3qXg",
    "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg"
)

GODFATHER = movie.Movie(
    "The Godfather",
    "Don Vito Corleone, head of a mafia family, decides to hand over \
    his empire to his youngest son Michael. However, his decision \
    unintentionally puts the lives of his loved ones in grave danger.",
    "https://www.youtube.com/watch?v=sY1S34973zA",
    "https://www.mugbug.co.uk/media/products/500/hmb.the_godfather.coaster.jpg"
)

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
