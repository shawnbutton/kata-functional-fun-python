from typing import List

from kata_function_fun.reading import Reading


class ReadingProcessor:
    def process_readings(self, readings):
        grouped = {}
        for reading in readings:
            # only process if we received data for reading
            if len(reading.data) > 0 and not reading.inactive:
                # convert temperature readings to Fahrenheit
                reading.temperature = reading.temperature * 1.8 + 32
                # group by reading type
                if reading.type == 'environmental':
                    if 'environmental' not in grouped:
                        grouped['environmental'] = []
                    grouped['environmental'].append(reading)
                elif reading.type == 'asset':
                    if 'asset' not in grouped:
                        grouped['asset'] = []
                    grouped['asset'].append(reading)
                elif reading.type == 'vehicle':
                    if 'vehicle' not in grouped:
                        grouped['vehicle'] = []
                    grouped['vehicle'].append(reading)
        return grouped

