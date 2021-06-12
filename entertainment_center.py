#https://classroom.udacity.com/courses/ud036
import media
import fresh_tomatoes

iron_man = media.Movie("Iron man",
                        "A super hero play boy with a cool iron suit",
                        "https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg",
                        "https://youtu.be/8ugaeA-nMTc")

# print(toy_story.storyline)

avengers_Endgame = media.Movie("Avengers: Endgame",
                     "A group of super heros fight with the big purple alian with golden gauntlet that can kill lives a half of galaxy",
                     "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg",
                     "https://youtu.be/TcMBFSGVi1c")

# print(Avengers_Endgame.storyline)
# Avengers_Endgame.show_trailer()

captain_america = media.Movie("Captain America: The First Avenger", 
                             "A super soldier who fight for people and the country",
                             "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                             "https://youtu.be/JerVrbLldXw")

wall_e = media.Movie("WALL-E",
                          "A scaverger robot in love with a high-tech robot",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg/220px-WALL-Eposter.jpg",
                          "https://youtu.be/CZ1CATNbXg0")

coco = media.Movie("Coco",
                                "The boy who goes to the ghost realm",
                                "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                                "https://youtu.be/Ga6RYejo6Hk")

charlie_and_the_chocolate_factory = media.Movie("Charlie and the chocolate factory",
                           "The mistery chocolate factory",
                           r"https://upload.wikimedia.org/wikipedia/en/1/17/Charlie_and_the_Chocolate_Factory_%28film%29.png",
                           "https://youtu.be/OFVGCUIXJls")   

movies = [iron_man, avengers_Endgame, captain_america, wall_e, coco, charlie_and_the_chocolate_factory]
fresh_tomatoes.open_movies_page(movies)