from typing import Tuple, List

LOGGING_FORMAT: str = '%(asctime)-15s %(message)s'
NOTES_FILE: str = 'Notes.txt'
INITIAL_GAP = 0x40
BLOCK_SIZE = 0x100
END_POINTER = 0x36890
FLOAT_FORMAT = '<f'
INT_FORMAT = '<I'
BOOL_FORMAT = '?'
SHORT_FORMAT = '<H'

STRINGS: List[Tuple] = [(0x00, "EffectName", 0x10),
                           ]
SHORTS: List[Tuple] = [(0x10, "ID"),
                       ]
FLOATS: List[Tuple] = [(0x40, "unknownParam40"),
                       ]
FLOATS_WITH_HEX: List[Tuple] = [(0x14, "unknownParam14"),
                                ]
BOOLS: List[Tuple] = [(0x12, "unknownAnimationParam"),
                      ]
HEXS:  List[Tuple] = []