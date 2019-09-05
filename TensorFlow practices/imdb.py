import tensorflow as tf
from tensorflow import keras

imdb = keras.datasets.imdb

#print(imdb)

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print("Training entries: {}, labels: {}".format(len(train_data), len(data_labels)))
