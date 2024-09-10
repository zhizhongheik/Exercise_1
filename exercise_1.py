# -*- coding: utf-8 -*-
"""Exercise_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J2k4EweQReQWa9BauYUb4Dt2ROgwSKzQ
"""

import tensorflow as tf
import numpy as np

"""# 1.Create a vector, scalar, matrix and tensor with values of your choosing using tf.constant()."""

vector = tf.constant([5, 4])
vector

scalar = tf.constant(9)
scalar

matrix = tf.constant([[1, 2],
                      [3, 4]])
matrix

tensor = tf.constant([[[1, 2, 3],
                       [4, 5, 6]],
                      [[7, 8, 9],
                       [10, 11, 12]],
                      [[13, 14, 15],
                       [16, 17, 18]]])
tensor

"""# 2.Find the shape, rank and size of the tensors you created in 1."""

print(f"tensor shape: {tensor.shape}")
print(f"tensor rank: {tensor.ndim}")
print(f"tensor size: {tf.size(tensor)}")

"""# 3.Create two tensors containing random values between 0 and 1 with shape [5, 300]."""

random_tensor_1 = tf.random.Generator.from_seed(0.5)
random_tensor_1 = random_tensor_1.normal(shape=(5, 300))
random_tensor_2 = tf.random.Generator.from_seed(0.7)
random_tensor_2 = random_tensor_2.normal(shape=(5, 300))

random_tensor_1, random_tensor_2

"""# 4.Multiply the two tensors you created in 3 using matrix multiplication."""

A = random_tensor_1 @ tf.reshape(random_tensor_2, shape=(300, 5))
print(A)

"""# 5.Multiply the two tensors you created in 3 using dot product."""

tf.tensordot(tf.transpose(random_tensor_1), random_tensor_2, axes=1)

"""# 6.Create a tensor with random values between 0 and 1 with shape [224, 224, 3]."""

random_tensor_3 = tf.random.Generator.from_seed(0.6)
random_tensor_3 = random_tensor_3.normal(shape=([224, 224, 3]))

random_tensor_3

"""# 7.Find the min and max values of the tensor you created in 6."""

print(f"random_tensor_3 min value is: {tf.reduce_min(random_tensor_3)}")
print(f"random_tensor_3 max value is: {tf.reduce_max(random_tensor_3)}")

"""# 8.Created a tensor with random values of shape [1, 224, 224, 3] then squeeze it to change the shape to [224, 224, 3]."""

random_tensor_4 = tf.random.Generator.from_seed(41)
random_tensor_4 = random_tensor_4.normal(shape=([1, 224, 224, 3]))

print(random_tensor_4.shape)

a = tf.reshape(random_tensor_4, shape=([224, 224, 3]))
print(a.shape)

"""# 9.Create a tensor with shape [10] using your own choice of values, then find the index which has the maximum value."""

c = tf.constant([1, 2, 3, 1, 12, 3, 2, 4, 5, 6])
c.shape

print(f"c maximum value is: {tf.reduce_max(c)}")

"""# 10.One-hot encode the tensor you created in 9."""

tf.one_hot(c, depth=4)