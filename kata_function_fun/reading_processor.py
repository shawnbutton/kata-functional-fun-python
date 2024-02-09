from functools import partial, reduce
from itertools import groupby
from typing import List

from toolz import pipe, compose_left

from kata_function_fun.reading import Reading


def convert_to_fahrenheit(reading):
    reading.temperature = reading.temperature * 1.8 + 32
    return reading


all_to_fahrenheit = partial(map, convert_to_fahrenheit)


def has_data(x):
    return len(x.data) > 0 and not x.inactive


only_with_data = partial(filter, has_data)


def is_allowed_type(reading):
    return reading.type in ['environmental', 'asset', 'vehicle']


only_allowed_types = partial(filter, is_allowed_type)


def group_by_type(accum, reading):
    reading_type = reading.type
    if not reading_type in accum:
        accum[reading_type] = [reading]
    else:
        accum[reading_type].append(reading)
    return accum


def by_type(readings):
    return reduce(group_by_type, readings, {})


class ReadingProcessor:
    def process_readings(self, readings: List[Reading]):
        return compose_left(only_with_data, only_allowed_types, all_to_fahrenheit, by_type)(readings)
