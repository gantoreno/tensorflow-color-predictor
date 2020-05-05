from tensorflow import keras
from tensorflow.keras import layers

import tensorflow as tf
import numpy as np

import pyfiglet
import json
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

try:
    print('Attemtting to load tensorflow model...')

    model = tf.keras.models.load_model('models/predictor')
except:
    print('Unable to load model, training and generation started...')

    with open('data/train.json') as data:
        train_colors = json.load(data)['colors']

    x_train = []
    y_train = []

    for pair in train_colors:
        background = pair['background']
        foreground = pair['foreground']

        color_x = [background['r'], background['g'], background['b']]
        color_y = [foreground['b'], foreground['w']]

        color_x = [channel / 255 for channel in color_x]
        color_y = [color / 255 for color in color_y]

        x_train.append(np.array(color_x))
        y_train.append(np.array(color_y))

    x_train = np.array(x_train)
    y_train = np.array(y_train)

    model = tf.keras.Sequential()

    model.add(layers.Input(3))
    model.add(layers.Dense(3, activation='sigmoid'))
    model.add(layers.Dense(2, activation='sigmoid'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, batch_size=4, epochs=20)
    
    model.save('models/predictor')

def predict_color():
    print(pyfiglet.figlet_format("Color Predictor", font="slant"))
    
    labels = ['black', 'white']
    
    print("Hey there! Give me an RGB color and I'll find out the best foreground for it")

    r = input('Red value   -> ')
    g = input('Green value -> ')
    b = input('Blue value  -> ')

    r = int(r) / 255
    g = int(g) / 255
    b = int(b) / 255

    channels = np.array([r, g, b])
    data = np.array([channels])

    prediction = model.predict(data)[0]
    color_index = np.argmax(prediction)
    confidence = float(prediction[color_index] * 100)


    print(f'I think foreground color must be {labels[color_index]}!')
    print(f'I\'m {confidence}% sure :)')

if __name__ == '__main__':      
    predict_color()

