from itertools import groupby
from typing import List

from kata_function_fun.reading import Reading


def convert_to_fahrenheit(reading):
    reading.temperature = reading.temperature * 1.8 + 32
    return reading


def has_data(x):
    return len(x.data) > 0 and not x.inactive


def by_type(reading):
    return reading.type


class ReadingProcessor:
    def process_readings(self, readings: List[Reading]):
        grouped = {}

        # only process if we received data for reading
        readings_with_data = [x for x in readings if has_data(x)]

        # convert temperature readings to Fahrenheit
        readings_in_fahrenheit = [convert_to_fahrenheit(x) for x in readings_with_data]

        grouped = {}

        data = sorted(readings_in_fahrenheit, key=lambda r: r.type)
        for readingType, reading in groupby(data, lambda r: r.type):
            if readingType in ['environmental', 'asset', 'vehicle']:
                grouped[readingType] = list(reading)

        return grouped
