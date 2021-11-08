from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

# img = image.load_img('training/tesla/t1.png')
# plt.imshow(img)
# plt.show()
#
# print(cv2.imread('training/tesla/t1.png'))
# print(cv2.imread('training/tesla/t1.png').shape)  # (168, 299, 3)

# 훈련 및 검증 데이터 만들기
train = ImageDataGenerator(rescale=1 / 255)
validation = ImageDataGenerator(rescale=1 / 255)

train_dataset = train.flow_from_directory('Training/',
                                          target_size=(200, 200),
                                          batch_size=3,
                                          class_mode='binary')
validation_dataset = train.flow_from_directory('Validation/',
                                               target_size=(200, 200),
                                               batch_size=3,
                                               class_mode='binary')

print(train_dataset.class_indices)  # {'Porshe': 0, 'Tesla': 1}
print(train_dataset.classes)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
    tf.keras.layers.MaxPool2D(2, 2),
    #
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    #
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D(2, 2),
    ##
    tf.keras.layers.Flatten(),
    ##
    tf.keras.layers.Dense(512, activation='relu'),
    ##
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['accuracy'])

model_fit = model.fit(train_dataset,
                      steps_per_epoch=3,
                      epochs=30,
                      validation_data=validation_dataset)


dir_path = 'classification'
for i in os.listdir(dir_path):
    print(i)
    img = image.load_img(dir_path + '/' + i, target_size=(200, 200))
    plt.imshow(img)
    plt.show()

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    val = model.predict(images)
    if val == 0:
        print('Porsche')
    else:
        print('Tesla')
