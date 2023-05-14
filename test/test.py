import sys
from os.path import dirname, abspath

# Add the parent directory of test/ to the system path
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

from zync.logger import logger

# Rest of your code


logger("hello!!")
