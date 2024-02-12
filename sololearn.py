import json

class Movie:
    def __init__(self):
        self.movies = [
            {"movieName": "Hacksaw Ridge", "rating": 9.77, "genre": "History", "views": 12.000000},
            {"movieName": "Top Gun: Maverick", "rating": 2.1, "genre": "Action", "views": 4.500000},
            {"movieName": "The Last Samurai", "rating": 7.6, "genre": "Drama", "views": 100000},
            {"movieName": "Avengers", "rating": 4.5, "genre": "Fantasy", "views": 1.500000},
        ]

    def sort_by_name(self):
        return sorted(self.movies, key=lambda x: x['movieName'])

    def sort_by_rating(self):
        return sorted(self.movies, key=lambda x: x['rating'], reverse=True)

    def sort_by_genre(self):
        return sorted(self.movies, key=lambda x: x['genre'])

    def sort_by_views(self):
        return sorted(self.movies, key=lambda x: x['views'], reverse=True)

    def get_movies(self, type):
        match type:
            case "by name":
                return self.sort_by_name()
            case "by rating":
                return self.sort_by_rating()
            case "by genre":
                return self.sort_by_genre()
            case "by views":
                return self.sort_by_views()
            case _:
                return "something went wrong"

if __name__ == '__main__':
    option = input('You have the option to sort the movies by "name, rating, genre and views" fill in the option and press enter, example (by name): ')
    mov = Movie()
    print(json.dumps(mov.get_movies(option), indent=2))
