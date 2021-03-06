from .adafruit import ADAFRUIT_APIS
from .microbit import MICROBIT_APIS
from .python3 import PYTHON3_APIS
from .pi import PI_APIS
from .shared import SHARED_APIS
from .pygamezero import PYGAMEZERO_APIS
from .esp import ESP_APIS  #新加的

__all__ = ['ADAFRUIT_APIS', 'MICROBIT_APIS', 'ESP_APIS', 'PYTHON3_APIS', 'PI_APIS',
           'SHARED_APIS', 'PYGAMEZERO_APIS', ]

'''
#原来的
__all__ = ['ADAFRUIT_APIS', 'MICROBIT_APIS', 'PYTHON3_APIS', 'PI_APIS',
           'SHARED_APIS', 'PYGAMEZERO_APIS', ]
'''