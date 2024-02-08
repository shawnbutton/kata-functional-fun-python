import pytest

import copy

from kata_function_fun.reading import Reading
from kata_function_fun.reading_processor import ReadingProcessor


class TestReadingProcessor:

    def build_reading(self, reading_type='environmental'):
        return Reading('test data', reading_type, False, [0], 0)

    def build_fahrenheit_reading(self, reading_type='environmental'):
        reading = self.build_reading(reading_type)
        reading.temperature = 32
        return reading

    def test_ignore_readings_with_no_data(self):
        given = self.build_reading()
        given.data = []
        expected = {}
        sut = ReadingProcessor()
        assert sut.process_readings([given]) == expected

    def test_ignore_readings_that_are_inactive(self):
        given = self.build_reading()
        given.inactive = True
        expected = {}
        sut = ReadingProcessor()
        assert sut.process_readings([given]) == expected

    # ... other tests ...

    @pytest.mark.skip(reason="will fail as we currently mutate readings")
    def test_should_not_mutate_readings(self):
        given = [self.build_reading()]
        identical_to_given = copy.deepcopy(given)
        sut = ReadingProcessor()
        sut.process_readings(given)
        assert given == identical_to_given
