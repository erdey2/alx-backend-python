#!/usr/bin/env python3
"""type annotation list module """


def sum_list(input_list: list) -> float:
    sum: float = 0
    for(i in input_list):
        sum += i

    return sum
