from functools import partial
from itertools import groupby
from typing import List

from kata_function_fun.reading import Reading


def convert_to_fahrenheit(reading):
    reading.temperature = reading.temperature * 1.8 + 32
    return reading


def has_data(x):
    return len(x.data) > 0 and not x.inactive


only_with_data = partial(filter, has_data)

all_to_fahrenheit = partial(map, convert_to_fahrenheit)

def by_type(reading):
    return reading.type


class ReadingProcessor:
    def process_readings(self, readings: List[Reading]):
        with_data = only_with_data(readings)

        readings_in_fahrenheit = all_to_fahrenheit(with_data)

        grouped = {}

        data = sorted(readings_in_fahrenheit, key=lambda r: r.type)
        for readingType, reading in groupby(data, lambda r: r.type):
            if readingType in ['environmental', 'asset', 'vehicle']:
                grouped[readingType] = list(reading)

        return grouped

    def filter_has_data(self):
        return partial(filter, has_data)
