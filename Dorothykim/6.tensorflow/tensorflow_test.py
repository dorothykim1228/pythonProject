import pandas as pd
import tensorflow as tf
import tensorflow.keras as keras


(mnist_x, mnist_y), _ = tf.keras.datasets.mnist.load_data()
print(mnist_x.shape, mnist_y.shape)

(cifar_x, cifar_y), _ = tf.keras.datasets.cifar10.load_data()
print(cifar_x.shape, cifar_y.shape)

# 1. 과거의 데이터를 준비
# (독립, 종속), _ = tf.keras.datasets.mnist.load_data()
# 독립 = 독립.reshape(60000, 28, 28, 1)
# 종속 = pd.get_dummies((종속)
# print(독립.shape, 종속.shape)

# 모델 구조 만들기
X = tf.keras.layers.Input(shape=[28,28,1])
H = tf.keras.layers.Conv2D(3, kernel_size=5, activation= 'swish')(X) #3개의 필터셋, 커널 사이즈 =5, 3채널의 특징맵
H = tf.keras.layers.Conv2D(6, kernel_size=5, activation= 'swish')(Y)
H = tf.keras.layers.Flatten()(H)
H = tf.keras.layers.Dense(84, activation='swish')(H)
Y = tf.keras.layers.Dense(10, activation='softmax')(H)
model = tf.keras.models.Model(X,Y)
model.compile(loss='scategorical_crosssentropy', metrics='accracy')
