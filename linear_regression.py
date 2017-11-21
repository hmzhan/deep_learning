
import numpy
import tensorflow as tf 
import matplotlib.pyplot as plt 
from __future__ import print_function

rng = numpy.random

# parameters ------------------------------------------------------------------
learning_rate = 0.01
training_epochs = 1000
display_step = 50

# training data ---------------------------------------------------------------
X_train = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
Y_train = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])

n_samples = X_train.shape[0]

X = tf.placeholder("float")
Y = tf.placeholder("float")

W = tf.Variable(rng.randn(), name = "weight")
b = tf.Variable(rng.randn(), name = "bias")

# construct a linear model
pred = tf.add(tf.multiply(X, W), b)
# mean squared error
cost = tf.reduce_sum(tf.pow(pred - Y, 2))/(2 * n_samples)

# gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
# initialize the variables
init = tf.global_variables_initializer()

# start training --------------------------------------------------------------
with tf.Session() as sess:
	