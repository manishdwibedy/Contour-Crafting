from enum import Enum     # for enum34, or the stdlib version

INPUT_TYPES = Enum(JSON='.json', CSV='.csv')

INPUT = INPUT_TYPES.JSON