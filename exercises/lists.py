class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if len(input_list) == 0:
            return input_list

        replaced_list = []
        max_value = max(input_list)
        for number in input_list:
            replaced_value = (number, max_value)[number > 0]
            replaced_list.append(replaced_value)

        return replaced_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        index = 0
        while index < len(input_list):
            if input_list[index] == query:
                return index
            index += 1

        return -1
