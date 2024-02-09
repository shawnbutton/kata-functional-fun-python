from functools import partial, reduce
from itertools import groupby
from typing import List

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

by_type = partial(reduce, group_by_type)

class ReadingProcessor:
    def process_readings(self, readings: List[Reading]):
        with_data = only_with_data(readings)

        allowed_types = only_allowed_types(with_data)

        readings_in_fahrenheit = all_to_fahrenheit(allowed_types)

        return by_type(readings_in_fahrenheit, {})
