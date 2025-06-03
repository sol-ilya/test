import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import calc


def test_addition():
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
