import media
import fresh_tomatoes

apollo13 = media.Movie("Apollo 13",
                 "A mission to the Moon goes wrong and turns into 'America's finest moment.'",
                 "http://images.moviepostershop.com/apollo-13-movie-poster-1995-1010327615.jpg",
                 "https://youtu.be/nEl0NsYn1fU?t=51",
                 '''"Apollo 13" never really states its theme, except perhaps in one sentence of narration at the end, but the whole film is suffused with it: The space program was a really extraordinary thing, something to be proud of, and those who went into space were not just "heroes" which is a cliche, but brave and resourceful.''')

# apollo13.show_trailer()

inbruges = media.Movie("In Bruges",
                       "It's just a shame it's in Belgium, really, but then you think that if it wasn't in Belgium, if it were somewhere good, there'd be too many people coming to see it, it'd spoil the whole thing.",
                       "http://www.movieposteraddict.com/wp-content/uploads/2008/01/mpainbrugesposter2b.jpg",
                       "https://www.youtube.com/watch?v=KoE9edjEDCI",
                       "This film debut by the theater writer and director Martin McDonagh is an endlessly surprising, very dark, human comedy, with a plot that cannot be foreseen but only relished. Every once in a while you find a film like this, that seems to happen as it goes along, driven by the peculiarities of the characters.")



movies = [apollo13, inbruges]
fresh_tomatoes.open_movies_page(movies)
