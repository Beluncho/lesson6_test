import math


def my_filter(iterable, function):
    """
    Возвращает итератор из тех элементов, для которых function возвращает истину.
    :param iterable: входаня последовательность
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    result = []
    for item in iterable:
        if function(item):
            result.append(item)

    print(result)

    return result
    pass


def my_map(function, iterator):
    """
    Итератор, получившийся после применения к каждому элементу последовательности функции function.

    :param function: функция
    :param iterator: входаня последовательность
    :return: новая последовательность
    """
    result = list(map(function, iterator))

    print(result)

    return result
    pass


def my_sorted(numbers):
    """

    :param numbers: не последовательный список
    :return: отсортированный список
    """

    result = sorted(numbers)

    print(result)

    return result
    pass


def my_square_circle(radius):
    """

    :param radius: радиус круга
    :return: площадь круга
    """
    square = math.pi * radius ** 2

    print(square)

    return square
    pass


def my_sqrt(number):
    """

    :param number: число
    :return: квадратный корень числа
    """
    result = math.sqrt(number ** 2)

    print(result)

    return result
    pass


def exponentiation(number, degree):
    """
    Возведение числа в степень
    :param number: число
    :param degree: степень
    :return: число в сепени
    """
    result = math.pow(number, degree)

    print(result)

    return result
    pass


def pythagoras(leg1, leg2):
    """

    :param leg1: катет1
    :param leg2: катет2
    :return: гипотенуза
    """
    hypotenuse = math.hypot(leg1, leg2)

    print(hypotenuse)

    return hypotenuse
    pass


pythagoras(15, 25)
