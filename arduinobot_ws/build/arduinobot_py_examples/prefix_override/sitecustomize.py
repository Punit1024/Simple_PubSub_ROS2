import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/projects/arduinobot_ws/install/arduinobot_py_examples'
