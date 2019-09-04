import tensorflow as tf

x = tf.constant(5.2)
y = tf.Variable([5])

y = tf.Variable([0])
y = y.assign([5])

with tf.Session() as sess:
    initialization = tf.global_variables_initializer()
    print(y.eval())

