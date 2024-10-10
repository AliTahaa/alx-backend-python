#!/usr/bin/env python3
""" duck type an iterable object """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ length of element """
    return [(i, len(i)) for i in lst]
