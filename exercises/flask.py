from typing import Union

from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    todo: должен возвращаться юзернейм
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": {"My name is <name>"}}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": {"My name is <new_name>"}}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        database = {}

        @app.route("/user", methods=["POST"])
        def create_user() -> tuple:
            name = request.json.get("name")
            if name:
                database[name] = name
                return {"data": f"User {name} is created!"}, 201
            return {"errors": {"name": "This field is required"}}, 422

        @app.route("/user/<name>", methods=["GET", "DELETE", "PATCH"])
        def user(name: str) -> Union[dict, tuple]:
            if request.method == "GET":
                if database.get(name):
                    return {"data": f"My name is {database[name]}"}, 200
                return "", 404
            if request.method == "PATCH":
                new_name = request.json.get("name")
                database[name] = new_name
                return {"data": f"My name is {new_name}"}, 200
            if request.method == "DELETE":
                database.pop(name)
                return "", 204
            return "", 500
