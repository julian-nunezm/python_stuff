#python -m pip install --upgrade pip
#pip3 install tensorflow
#pip3 install matplotlib
from __future__ import absolute_import, division, print_function, unicode_literals

#TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist

#Helper libraries
import numpy as np
import matplotlib.pyplot as plt

try:
    print(tf.__version__)

    #fashion_mnist = keras.datasets.fashion_mnist

    #train_images and train_labels are arrays the training set (The data the model uses to learn).
    #test_images and test_lables are arrays which the model is tested against (The test set).
    #Label-Class:
    #[0]-T-shirt/top,[1]-Trouser,[2]-Pullover,[3]-Dress,[4]-Coat,[5]-Sandal,[6]-Shirt,[7]-Sneaker,[8]-Bag,[9]-Ankle boot
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    train_images.shape
except Exception as exc:
    print(f"Error: {str(exc)}")
