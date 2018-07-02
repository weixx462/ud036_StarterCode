import media
import fresh_tomatoes

jurassic_world = media.Movie("Jurassic World: Fallen Kingdom", "Three years after the destruction of the Jurassic World theme park", 
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcR7nb6jKLhuTeSyO2CtELj-KQyYM6PxLwTtnKGCh74KSdJe9XWt",
                            "https://youtu.be/1FJD7jZqZEk")

spider_man = media.Movie("Spider-Man: Into the Spider-Verse", "Spider-Man mentors a teenager from Brooklyn, N.Y., to become the next web-slinging superhero.", 
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcQbehdUfqrxew8nLGtajrYgNSc8m4Il8BUfW4C_AC0ggi8xJVh5",
                            "https://youtu.be/g4Hbz2jLxvQ")

hero = media.Movie("Hero", "In this visually arresting martial arts epic set in ancient China", 
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQSezxbA-bTf9aUKYpL3GM2Z05MelNt-hANkbY9cxmowmYs2PCf",
                            "https://youtu.be/srFhXDZhUZI")

titanic = media.Movie("Titanic", "James Cameron's Titanic is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic", 
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcQhYjUIu2o5v5u3rfJpCq5Cz0Q9WK--XdYxai_N2d0ImohPiIOp",
                            "https://youtu.be/zCy5WQ9S4c0")

movies = [jurassic_world, spider_man, hero, titanic]

fresh_tomatoes.open_movies_page(movies)

