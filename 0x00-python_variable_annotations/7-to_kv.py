#!/usr/bin/env python3
'''string and int/float to tuple'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''to tuple'''
    return (str(k), float(v**2))
