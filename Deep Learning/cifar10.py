import numpy as np
import tensorflow as tf

keras=tf.keras
cifar10=keras.datasets.cifar10
kutils=keras.utils
klayers=keras.layers

from keras.utils  import to_categorical

from keras import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.metrics import Precision,Recall

(train_images,train_labels),(test_images,test_labels)=cifar10.load_data()
