import media
import fresh_tomatoes

"""Dedicated to creating instances, or the individual movies, from the Movie Class 
contained in the media file"""

#Creates the variable for the movie "Her"
her = media.Movies("Her",
                   "A lonely writer develops an unlikely relationship with an operating system"
                   " designed to meet his every need.",
                   "http://www.impawards.com/2013/posters/her_ver2.jpg",
                   "https://www.youtube.com/watch?v=Ai1G85FypxQ")

#Creates the variable for the movie "Eternal Sunshine of the Spotless Mind"
eternal_sunshine = media.Movies("Eternal Sunshine of the Spotless Mind",
                                "When their relationship turns sour, a couple undergoes a procedure"
                                " to have each other erased from their memories. But it is only through"
                                " the process of loss that they discover what they had to begin with.",
                                "https://cinephilefix.files.wordpress.com/2012/12/600full-eternal-sunshine-of-the-spotless-mind-poster.jpg",
                                "https://www.youtube.com/watch?v=GBEke6JixyE")

#Creates the variable for the movie "Fight Club"
fight_club = media.Movies("Fight Club",
                          "An insomniac office worker, looking for a way to change his life,"
                          " crosses paths with a devil-may-care soap maker, forming an underground"
                          " fight club that evolves into something much, much more.",
                          "http://screencrush.com/files/2013/10/fightclub1.jpg",
                          "https://www.youtube.com/watch?v=zvtUrjfnSnA")

#Creates the variable for the movie "A Beautiful Mind"
beautiful_mind = media.Movies("A Beautiful Mind",
                              "After John Nash, a brilliant but asocial mathematician,"
                              " accepts secret work in cryptography,"
                              " his life takes a turn for the nightmarish.",
                              "https://s-media-cache-ak0.pinimg.com/736x/24/9a/51/249a515ec7cf9dc7376cbbb211e95aba.jpg",
                              "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

#Creates the variable for the movie "WALL-E"
wall_e = media.Movies("WALL-E",
                      "In the distant future, a small waste-collecting"
                      " robot inadvertently embarks on a space journey that will"
                      " ultimately decide the fate of mankind.",
                      "https://s-media-cache-ak0.pinimg.com/originals/4d/8a/d2/4d8ad26d4e1aee5fcb720becda182bf0.jpg",
                      "https://www.youtube.com/watch?v=NPW3mvAN0Rc")

#Creates the variable for the movie "Nick and Norah's Infinite Playlist"
infinite_playlist = media.Movies("Nick and Norah's Infinite Playlist",
                                 "High school student Nick O'Leary,"
                                 " member of the Queercore band The Jerk Offs,"
                                 " meets college-bound Norah Silverberg when she"
                                 " asks him to be her boyfriend for five minutes.",
                                 "https://posterspy.com/wp-content/uploads/2015/04/Nick-and-Norahs-Infinite-Playlist.jpg",
                                 "https://www.youtube.com/watch?v=sR4iKRfUwOs")

#Creates the variable for the movie "Despicable Me"
desp_me = media.Movies("Despicable Me",
                       "When a criminal mastermind uses a trio of orphan girls"
                       " as pawns for a grand scheme, he finds their love is"
                       " profoundly changing him for the better.",
                       "https://s-media-cache-ak0.pinimg.com/236x/22/d4/f8/22d4f80552440d65cbb2120e73f1c996.jpg",
                       "https://www.youtube.com/watch?v=fdrR3NbPARs")

#Creates the variable for the movie "Ratatouille"
rat = media.Movies("Ratatouille",
                   "A rat who can cook makes an unusual alliance"
                   " with a young kitchen worker at a famous restaurant.",
                   "https://s-media-cache-ak0.pinimg.com/564x/5c/c9/de/5cc9de71d1c598a82103b1d66dab0cfd.jpg",
                   "https://www.youtube.com/watch?v=jwLKPDJqldw")

#Creates the variable for the movie "Definitely, Maybe"
def_maybe = media.Movies("Definitely, Maybe",
                         "A political consultant tries to explain his impending divorce"
                         " and past relationships to his 11-year-old daughter.",
                         "https://s-media-cache-ak0.pinimg.com/736x/5c/4e/b7/5c4eb7cc7d46be0360a2a04ec76de73e.jpg",
                         "https://www.youtube.com/watch?v=GkPbF_FJuho")

#Create an array of the movie variables
movies = [her, eternal_sunshine, fight_club,
          beautiful_mind, wall_e, infinite_playlist,
          desp_me, rat, def_maybe]

#Open url of movies with a fresh_tomatoes function
fresh_tomatoes.open_movies_page(movies)


#print(media.Movies.__module__)