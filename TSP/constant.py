from enum import Enum

class INPUT_TYPE(Enum):
    JSON = '.json'
    CSV = '.csv'

INPUT = INPUT_TYPE.JSON

print INPUT_TYPE.JSON.name
print INPUT_TYPE.JSON.value