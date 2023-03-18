# Custom L1 Distance layer module
# WHY DO WE NEED THIS: its needed to load the custom model

# Import dependencies
import tensorflow as tf
from tensorflow.python.keras.layers import Layer


class L1Dist(Layer):

    # Init method - inheritance
    def __init__(self, **kwargs):
        super().__init__()

    # Magic happens here - similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)
