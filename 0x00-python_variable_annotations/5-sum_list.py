#!/usr/bin/env python3
"""type annotation list module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for(i in input_list):
        sum += i

    return sum
