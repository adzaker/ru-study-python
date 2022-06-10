import re
from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_movie_rating(movie: dict) -> float:
            movie_countries_amount = len(movie["country"].split(","))
            if movie["rating_kinopoisk"] and movie_countries_amount > 1:
                return float(movie["rating_kinopoisk"])
            return 0

        def get_average_rating(rating_list: list) -> float:
            all_ratings = 0
            non_zero_rating_amount = 0
            for rating in rating_list:
                if rating:
                    all_ratings += rating
                    non_zero_rating_amount += 1

            return all_ratings / non_zero_rating_amount

        ratings = list(map(get_movie_rating, list_of_movies))
        average_rating = get_average_rating(ratings)
        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def get_movie_names(movie: dict) -> str:
            if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) > rating:
                return movie["name"]
            return ""

        all_names_in_string = "".join(map(get_movie_names, list_of_movies))
        return len(re.findall("и", all_names_in_string))
