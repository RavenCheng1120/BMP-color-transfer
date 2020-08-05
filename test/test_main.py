from pathlib import Path
from s4105056005_DCSA_03 import colorTran

def test_demo():
    colorTran('s1.bmp','t1.bmp',1)
    assert Path('./result/tr1.bmp').exists() == True