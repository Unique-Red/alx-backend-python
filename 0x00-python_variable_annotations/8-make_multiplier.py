#!/usr/bin/env python3
'''functions'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return float * multiplier'''
    def new_function(n: float) -> float:
        '''multiplies the float by mulitiplier'''
        return float(n * multiplier)

    return new_function
