import pytest

import copy

from kata_function_fun.reading import Reading
from kata_function_fun.reading_processor import ReadingProcessor


class TestReadingProcessor:
    def build_reading(self, reading_type='environmental'):
        return Reading(reading_type, False, [0], 0)

    def build_reading_in_fahrenheit(self, reading_type='environmental'):
        return Reading(reading_type, False, [0], 32)

    def test_ignore_readings_with_no_data(self):
        given = self.build_reading()
        given.data = []
        assert ReadingProcessor.process_readings([given]) == {}

    def test_ignore_readings_that_are_inactive(self):
        given = self.build_reading()
        given.inactive = True

        assert ReadingProcessor.process_readings([given]) == {}

    def test_environmental_is_grouped(self):
        reading = self.build_reading("environmental")
        given_readings = [reading]
        expected = {
            "environmental": [self.build_reading_in_fahrenheit("environmental")]
        }

        assert ReadingProcessor.process_readings(given_readings) == expected

    def test_asset_is_grouped(self):
        reading = self.build_reading("asset")
        given_readings = [reading]

        expected = {"asset": [self.build_reading_in_fahrenheit("asset")]}

        assert ReadingProcessor.process_readings(given_readings) == expected

    def test_vehicle_is_grouped(self):
        reading = self.build_reading("vehicle")
        given_readings = [reading]
        expected = {"vehicle": [self.build_reading_in_fahrenheit("vehicle")]}

        assert ReadingProcessor.process_readings(given_readings) == expected

    def test_other_types_are_ignored(self):
        reading = self.build_reading("some other type")
        given_readings = [reading]

        assert ReadingProcessor.process_readings(given_readings) == {}

    def test_should_group_multiple_readings(self):
        reading_env = self.build_reading("environmental")
        reading_asset = self.build_reading("asset")
        reading_vehicle = self.build_reading("vehicle")
        given_readings = [reading_env, reading_asset, reading_vehicle]

        expected = {
            "environmental": [self.build_reading_in_fahrenheit("environmental")],
            "asset": [self.build_reading_in_fahrenheit("asset")],
            "vehicle": [self.build_reading_in_fahrenheit("vehicle")]
        }

        assert ReadingProcessor.process_readings(given_readings) == expected

    def test_should_convert_to_fahrenheit(self):
        reading_minus_30_celsius = Reading("environmental", False, [0], -30.0)
        reading_20_celsius = Reading("environmental", False, [0], 20.0)
        given_readings = [reading_minus_30_celsius, reading_20_celsius]

        result = ReadingProcessor.process_readings(given_readings)

        assert result["environmental"][0].temperature == -22.0
        assert result["environmental"][1].temperature == 68.0

    @pytest.mark.skip(reason="will fail as we currently mutate readings")
    def test_should_not_mutate_readings(self):
        given = [self.build_reading()]
        identical_to_given = copy.deepcopy(given)

        ReadingProcessor.process_readings(given)

        assert given == identical_to_given
