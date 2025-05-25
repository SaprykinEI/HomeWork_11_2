from __future__ import annotations
from abc import abstractmethod, ABC
from typing import Any


class Builder(ABC):
    def __init__(self):
        self.name = None

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def first_action(self) -> None:
        pass

    @abstractmethod
    def second_action(self) -> None:
        pass


class Tiler(Builder):

    def __init__(self) -> None:
        self.reset()
        self.name = 'Плиточник'

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def first_action(self) -> None:
        self._product.add('Подготовка пола')

    def second_action(self) -> None:
        self._product.add("укладка плитки")


class Finisher(Builder):
    def __init__(self) -> None:
        self.reset()
        self.name = 'Отделочник'

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def first_action(self) -> None:
        self._product.add(' нанести шпаклевку')

    def second_action(self) -> None:
        self._product.add("оштукатурить стены")


class Painter(Builder):
    def __init__(self) -> None:
        self.name = 'Маляр'
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        # self.reset()
        return product

    def first_action(self) -> None:
        self._product.add('загрунтовать стену')

    def second_action(self) -> None:
        self._product.add(" покрасить стену")


class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Выполненные работы : {','.join(self.parts)}')


class Director:

    def __init__(self) -> None:
        self._builder = None
        self.name = 'Прораб'

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def make_floors(self) -> None:
        print(f'Полы закончены: {self.name}')

    def level_the_walls(self) -> None:
        print(f'Стены выровнены: {self.name}')

    def turnkey_work(self):
        print(f'Работы под ключ от: {self.builder.name}')
        self.builder.first_action()
        self.builder.second_action()


if __name__ == '__main__':
    print('Работа под ключ: ')
    director = Director()
    tiler = Tiler()
    director.builder = tiler
    director.turnkey_work()
    tiler.product.list_parts()
    painter = Painter()
    director.builder = painter
    director.turnkey_work()
    painter.product.list_parts()

    finisher = Finisher()
    director.builder = finisher
    director.turnkey_work()
    finisher.product.list_parts()
    tiler.first_action()
    tiler.product.list_parts()
    director.level_the_walls()
    director.make_floors()