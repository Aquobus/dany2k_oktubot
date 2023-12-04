class Person:

    #Класс студента, нужен для быстрого перемещения по его компонентам, не заходя в бд

    """Класс студента"""

    def __init__(self, ID, T_ID, surname, name, last_duty, count_duty):

        #Переменные создаются автоматически при создании класса

        """Функция инициализации"""

        self.id = ID
        self.t_id = T_ID
        self.surname = surname
        self.name = name
        self.last_duty = last_duty
        self.count_duty = count_duty

    def get_person_meta(self):

        """Информационная функция"""

        #Функция для выдачи полной инфы, для корректного отображения и тестирования

        meta = [self.id, self.t_id, self.surname, self.name, self.last_duty, self.count_duty]
        return meta