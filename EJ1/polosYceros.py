import scipy
from scipy import signal
from scipy import signal.TransferFunction as tf

h = tf

num = [1, 3, 3]
den = [1, 2, 1]

signal.TransferFunction(num, den)