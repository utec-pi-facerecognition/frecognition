# By José Ignacio Huby Ochoa
# UTEC - CS


# Neural Network: set of linked neurons
#   Input handle method
#       None <----
#       Convolution
#       ...
#   Output destination
#       Feed forward: the output of a neuron goes towards all the neurons of the next layer  <----
#       Recurrent: the output of a neuron might go towards a previous neuron (allows loops)
#   Amount of layers
#       Single layer
#       Multiple layer  <-----


class Simple_FF_Neural_Network:
    def __init__(self, neuron_class, activation_function, initial_value_generator, *layers_size):
        self.dataset = []
        self.act = activation_function
        self.input_layer_size = layers_size[0]
        self.layers = []
        for i in range(1, len(layers_size)):
            layer = []
            for j in range(layers_size[i]):
                layer.append(neuron_class(layers_size[i-1], initial_value_generator))
            self.layers.append(layer)

    def set_dataset(self, dataset):
        self.dataset = dataset

    def create_random_dataset(self, random_input_generator, output_formula, dataset_size):
        self.dataset = [[[random_input_generator() for j in range(self.input_layer_size)]] for i in range(dataset_size)]
        for i in range(dataset_size):
            self.dataset[i].append(output_formula(self.dataset[i][0]))

    def use(self, inputs):
        for layer in self.layers:
            layer_outputs = [neuron.feed(inputs) for neuron in layer]
            inputs = layer_outputs
        unactivated_outputs = inputs
        outputs = [self.act(output) for output in unactivated_outputs]
        return outputs

    def feedforward(self, inputs, expected_output):
        outputs = self.use(inputs)
        return [expected_output[i] - outputs[i] for i in range(len(expected_output))]

    def backpropagation(self, error, error_magnitude):
        error_k = [e*error_magnitude for e in error]
        for layer in reversed(self.layers):
            source_layer_error = [layer[i].tweak(error_k[i]) for i in range(len(layer))]
            error_k = [sum(x) for x in zip(*source_layer_error)]

    def train(self, data_index, error_magnitude):
        print(self.dataset[data_index])
        error = self.feedforward(self.dataset[data_index][0], self.dataset[data_index][1])
        print(error)
        self.backpropagation(error, error_magnitude)

    def full_train(self, error_magnitude):
        for i in range(len(self.dataset)):
            self.train(i, error_magnitude)

    def get(self):
        return [[neuron.get() for neuron in layer] for layer in self.layers]
