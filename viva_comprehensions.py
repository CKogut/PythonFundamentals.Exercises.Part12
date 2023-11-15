from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 1
    EVEN = 0


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    A function to return either only the even or odd numbers in a range

    :param start: Start of range
    :param stop: End of range
    :param parity: EVEN or ODD
    :return: list
    """
    return [value for value in range(start, stop) if value % 2 == parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    result = {value: strategy for value in range(start, stop)}
    return result


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    pass
