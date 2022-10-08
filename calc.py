from typing import Union


def add(a: float, b: float) -> Union[float, int]:
    return a + b


def substract(a: float, b: float) -> Union[float, int]:
    """
    To będzie odejmować
    :param a:
    :param b:
    :return:
    """
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: float, b: float) -> float:
    """
    a: pierwsza liczba
    b: druga liczba
    return: wynik dzielenia
    """
    return a / b
