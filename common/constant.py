from enum import Enum

class INPUT_TYPE(Enum):
    JSON = '.json'
    CSV = '.csv'

INPUT = INPUT_TYPE.CSV

class EDGE_TPYE(Enum):
    DEPOSITION = 0
    ROTATION = 1
    IDLE = 2

DEPOSITION_COST = 5

DEPOSITION_RATIO = -10
ROTATION_COST = 0.1
IDLE_RATIO = 1

FILE_NAME = 'input.json'