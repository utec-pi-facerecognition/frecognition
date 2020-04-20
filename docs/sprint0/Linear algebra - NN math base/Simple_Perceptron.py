# By José Ignacio Huby Ochoa
# UTEC - CS


# Math branch: Linear algebra

# Perceptron: adjustable linear function (that can solve linear separable problems)
#   Adjustable linear function: set of weights that will gradually change
#   Linear separable: you can divide a set with a line to identify two subsets

class Simple_Perceptron:
    def __init__(self, size, initial_value_generator):
        # f(x, y, z, ...) = ax + by + cz ... + constant

        # [x, y, z, ...]
        self.inputs = [0 for i in range(size)]

        # [a, b, c, ...]
        self.weights = [initial_value_generator() for i in range(size)]

        # constant
        self.constant = initial_value_generator()


    def feed(self, inputs):
        # [x, y, z, ...]
        self.inputs = inputs.copy()

        # [a*x, b*y, c*z, ...]
        mult = [self.weights[i]*self.inputs[i] for i in range(len(self.weights))]

        # a*x + b*y + c*z ...
        w_times_variable_sum = sum(mult)

        # a*x + b*y + c*z ... + constant
        total_sum = w_times_variable_sum + self.constant

        # f(inputs)
        return total_sum

    def tweak(self, error):
        #blame input source by (weight/total_weight). This is useful, if the inputs come from another Perceptron
        total_weights = sum(self.weights)
        responsable_for_the_error = [error*w/total_weights for w in self.weights]

        # tweak weights towards correct direction
        for i in range(len(self.weights)):
            self.weights[i] += self.inputs[i]*error
        self.constant += error

        return responsable_for_the_error

    def get(self):
        return self.weights + [self.constant]
