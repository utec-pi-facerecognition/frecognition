import math

def sigmoid(x):
  if x < 0:
    return 1 - 1/(1 + math.exp(x))
  else:
    return 1/(1 + math.exp(-x))
