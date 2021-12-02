import tensorflow as tf
import tensorflow.keras as tfk

indices = [5, 4, 3, 2, 1, 0]
oneHot = tf.one_hot(indices, len(indices))
print(oneHot)