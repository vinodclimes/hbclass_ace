#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:34:43 2021

@author: vaibhavsaxena
"""

import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt
import cv2

model = keras.models.load_model('densenet169July26.h5')
labels = {'B': 0, 'F': 1}


def predictions(img_path):
    img = plt.imread(img_path)
    img_resized = cv2.resize(img, (224,224))
    img_tf = tf.Variable(img_resized)
    img_tf = tf.expand_dims(img_tf, 0 )
    pred = model.predict(img_tf)
    res = dict((v,k) for k,v in labels.items())
    label_result = res[np.argmax(pred)]
    return label_result