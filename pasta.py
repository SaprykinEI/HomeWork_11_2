from abc import ABC, abstractmethod


# Здесь мы используем паттерн: Абстрактная фабрика для создания компонентов пасты, так как он легко позволяет
# нам создавать различные типы паст меняя лишь компоненты. И экземпляры конкретных классов не будут связаны между собой.
class AbstractPastaFactory:
    @abstractmethod
    def create_pasta(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_filling(self):
        pass

    @abstractmethod
    def create_additions(self):
        pass


# Конкретная фабрика по созданию компонентов Карбонары
class CarbonaraFactory(AbstractPastaFactory):
    def create_pasta(self):
        return 'Спагетти'

    def create_sauce(self):
        return 'Сливочный соус'

    def create_filling(self):
        return 'Бекон'

    def create_additions(self):
        return 'Пармезан'


# Конкретная фабрика для создания компонентов "Болоньезе"
class BologneseFactory(AbstractPastaFactory):
    def create_pasta(self):
        return "Спагетти"

    def create_sauce(self):
        return "Томатный соус"

    def create_filling(self):
        return "Говядина"

    def create_additions(self):
        return "Оливковое масло"


# Конкретная фабрика для создания компонентов пасты "Песто"
class AlioFactory(AbstractPastaFactory):
    def create_pasta(self):
        return "Спагетти"

    def create_sauce(self):
        return "Оливковое масло"

    def create_filling(self):
        return "Перец Чили"

    def create_additions(self):
        return "Чеснок"


class Pasta(ABC):
    @abstractmethod
    def get_pasta_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_additions(self):
        pass



class Carbonara(Pasta):
    def __init__(self, factory: AbstractPastaFactory):
        self.factory = factory

    def get_pasta_type(self):
        return self.factory.create_pasta()

    def get_sauce(self):
        return self.factory.create_sauce()

    def get_additions(self):
        return self.factory.create_additions()

    def get_filling(self):
        return self.factory.create_filling()

    def __str__(self):
        return f'Паста Карбонара ({self.__class__.__name__}) состоит из : {self.get_pasta_type()}, {self.get_sauce()}, {self.get_filling()}, {self.get_additions()}'


# Конкретный класс пасты "Болоньезе"

class Bolognese(Pasta):
    def __init__(self, factory: AbstractPastaFactory):
        self.factory = factory

    def get_pasta_type(self):
        return self.factory.create_pasta()

    def get_sauce(self):
        return self.factory.create_sauce()

    def get_additions(self):
        return self.factory.create_additions()

    def get_filling(self):
        return self.factory.create_filling()

    def __str__(self):
        return f'Паста Болоньезе ({self.__class__.__name__}) состоит из : {self.get_pasta_type()}, {self.get_sauce()}, {self.get_filling()}, {self.get_additions()}'




class Alio(Pasta):
    def __init__(self, factory: AbstractPastaFactory):
        self.factory = factory

    def get_pasta_type(self):
        return self.factory.create_pasta()

    def get_sauce(self):
        return self.factory.create_sauce()

    def get_additions(self):
        return self.factory.create_additions()

    def get_filling(self):
        return self.factory.create_filling()

    def __str__(self):
        return f'Паста Алио ({self.__class__.__name__}) состоит из : {self.get_pasta_type()}, {self.get_sauce()}, {self.get_filling()}, {self.get_additions()}'


def client_code():
    while True:
        pasta_type = int(input('Меню:\n1: "Карбонара"\n2: "Болоньезе"\n3: "Алио"\n4:Выход\nВыберите пасту: '))
        if pasta_type == 1:
            factory = CarbonaraFactory()
            print(Carbonara(factory), end='\n\n')

        elif pasta_type == 2:
            factory = BologneseFactory()
            print(Bolognese(factory), end='\n\n')

        elif pasta_type == 3:
            factory = AlioFactory()
            print(Alio(factory), end='\n\n')
            # return 'Ваша паста готова!!!'
        elif pasta_type == 4:
            print('До свидания!!')
            break
        else:
            raise ValueError("Unknown pasta type")


if __name__ == '__main__':
    client_code()