from .python3 import PythonMode
from .adafruit import AdafruitMode
from .microbit import MicrobitMode
from .debugger import DebugMode
from .pygamezero import PyGameZeroMode
from .esp import EspMode    #新加的
__all__ = [ 'PythonMode', 'AdafruitMode', 'MicrobitMode', 'DebugMode','EspMode',
           'PyGameZeroMode',  ]

'''
#这里是原来的
__all__ = ['PythonMode', 'AdafruitMode', 'MicrobitMode', 'DebugMode',
           'PyGameZeroMode', ]
'''