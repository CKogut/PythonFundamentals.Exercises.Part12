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
    A function to create a new dictionary. Keys are integers in a given range, and values are calculated via a lambda
    function

    :param start: start of range
    :param stop: end of range
    :param strategy: lambda function to calculate value
    :return: dictionary
    """
    return {value: strategy(value) for value in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    A function to take in a string and return a set. Only the lower case values will be included and they will be
    returned in upper case

    :param val_in: a string
    :return: a set of the lower case characters in the string, transformed to upper case
    """
    result = {value.upper() for value in val_in if value.islower()}
    return result
