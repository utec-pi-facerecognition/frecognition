# By Jose Ignacio Huby Ochoa
# UTEC - CS

# NOTICE:   This is not reliable material (made by a noob in the subject).
#           However, if it turns useful, credits are more than welcome.

# Details/explanation on each module

import Simple_FF_Neural_Network as nn
import Simple_Perceptron as n
import Simple_Activation_Function as af

import random



# Linear separable problem

# Goal formula
def secret_formula(x):
    return [3*x[0] - 2*x[1] < 15]

# Create and setup neural network
my_nn = nn.Simple_FF_Neural_Network(n.Simple_Perceptron, af.sigmoid, lambda: random.uniform(1, 2), 2, 1)
my_nn.create_random_dataset(lambda: random.uniform(-100, 100), secret_formula, 100000)

# Train neural network
my_nn.full_train(1)

# Show resultant neural network (all neurons weights)
result = my_nn.get()
print('')
print(result)

# Use neural network
print('')
print(my_nn.use([3, 4]))
print(my_nn.use([54, 7.5]))

# Validate neural network (I did this step manually with the "resultant neural network" printed values)
print('')
print(af.sigmoid(294))
print(af.sigmoid(-6095))





'''
# XOR problem

# XOR formula
def xor(x):
    return [(x[0] and not x[1]) or (not x[0] and x[1])]

# Create XOR neural network
xor_nn = nn.Simple_FF_Neural_Network(n.Simple_Perceptron, af.sigmoid, lambda: random.uniform(1, 2), 2, 2, 1)
xor_dataset = [
    [[0, 0], [0]],
    [[1, 0], [1]],
    [[0, 1], [1]],
    [[1, 1], [0]]
               ]
xor_nn.set_dataset(xor_dataset)

# Train XOR neural network
for i in range(1000):
    xor_nn.full_train(1)

# Use XOR neural network
print(xor_nn.use([0, 1]))
'''
