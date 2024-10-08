from dataclasses import dataclass
from venv import logger


@dataclass
class Reading:

    timestamp: float
    adc: int
    def voltage(self):
        return 1.653 * self.adc + 0.456



class OldReading:
    """Storage for a single voltage"""
    def __init__(self, timestamp, adc):
        self.timestamp = timestamp
        self.adc = adc
    
    def voltage(self):
        'Convert ADC counts into voltage (in V)'
        return 1.653 * self.adc + 0.456
    
    def __str__(self):
        return f'Reading at {self.timestamp} s: {self.adc} ADC counts ({self.voltage()})'


class VoltageData:
    """Interface to a set of votage readings"""

    def __init__(self, file_path):
        logger.info(f'Reading voltage data from (file_path)...')
        with open(file_path) as input_file:
            #self._lines = input_file.readlines()
            self._readings = [self.parse_line(line) for line in input_file.readlines()]
        logger.info(f'Done, {len(self._readings)} values read.')
        self._iterator = iter(self._readings)


    def parse_line(self, line):
        """Parse a single line from a txt file and returns a Reading object"""
        timestamp, adc = line.split()
        timestamp = float(timestamp)
        adc = int(adc)
        return Reading(timestamp, adc)
    

    def __iter__(self):
        return self
    

    def __next__(self):
        #return self.parse_Line(next(self._line_iterator))
        return next(self._iterator)
    
    def __getitem__(self, index):
        return self._readings[index]


if __name__ == '__main__':
    data = VoltageData('voltage_data.txt')
    for reading in data:
        print(reading)

    print('Done')
    print(data[3])