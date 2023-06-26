import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.applications.resnet import ResNet50
from keras.preprocessing import image
from keras.applications.resnet import preprocess_input, decode_predictions
import numpy as np
import tensorflow as tf

g1 = tf.Graph()
sess1 = tf.compat.v1.Session(graph=g1)

with sess1.as_default():
    with g1.as_default():
        tf.compat.v1.global_variables_initializer().run()
        model = ResNet50(weights='imagenet')


def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    with sess1.as_default():
        with sess1.graph.as_default():
            preds = model.predict(x)
            predictions = decode_predictions(preds, top=1)[0]
    return (predictions)
