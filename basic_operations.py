
import tensorflow as tf  
from __future__ import print_function

# constant --------------------------------------------------------------------
a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
	print("a = 2, b = 3")
	print("Addition with constants: %i" % sess.run(a + b))
	print("Multiplication with constants: %i" % sess.run(a * b))

# variable --------------------------------------------------------------------
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)

with tf.Session() as sess:
	print("Addition with variables: %i" % sess.run(add, feed_dict = {a: 2, b: 3}))
	print("Multiplication with variables: %i" % sess.run(mul, feed_dict = {a: 2, b: 3}))

# matrix ----------------------------------------------------------------------
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
	result = sess.run(product)
	print(result)

