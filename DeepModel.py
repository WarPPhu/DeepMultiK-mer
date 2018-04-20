#####################################################################################
#															   
#  Classification of long non-coding RNAs and messenger RNAs by deep learning method
#  Authors: Phurinut Chanhom						   		  
#  Version: 1.0
#  Updated on: April 20, 2018  
#															   
#####################################################################################

from __future__ import print_function

import tensorflow as tf
import csv
import numpy as np
import pandas as pd
import os

n_hidden =[100,100,100,100]

def Model(x,y,keep_prob,n_input,n_classes):
    weights = {
        'h1': tf.Variable(tf.random_normal([n_input, n_hidden[0]])),
        'h2': tf.Variable(tf.random_normal([n_hidden[0], n_hidden[1]])),
        'h3': tf.Variable(tf.random_normal([n_hidden[1], n_hidden[2]])),
        'h4': tf.Variable(tf.random_normal([n_hidden[2], n_hidden[3]])),
        'out': tf.Variable(tf.random_normal([n_hidden[3], n_classes]))
    }
    biases = {
        'b1': tf.Variable(tf.random_normal([n_hidden[0]])),
        'b2': tf.Variable(tf.random_normal([n_hidden[1]])),
        'b3': tf.Variable(tf.random_normal([n_hidden[2]])),
        'b4': tf.Variable(tf.random_normal([n_hidden[3]])),
        'out': tf.Variable(tf.random_normal([n_classes]))
    }

    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.sigmoid(layer_1)
    layer_1 = tf.nn.dropout(layer_1,keep_prob)
    
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.sigmoid(layer_2)
    layer_2 = tf.nn.dropout(layer_2,keep_prob)
    
    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    layer_3 = tf.nn.sigmoid(layer_3)
    layer_3 = tf.nn.dropout(layer_3,keep_prob)
    
    layer_4 = tf.add(tf.matmul(layer_3, weights['h4']), biases['b4'])
    layer_4 = tf.nn.sigmoid(layer_4)
    layer_4 = tf.nn.dropout(layer_4,keep_prob)
    
    out_layer = tf.matmul(layer_4, weights['out']) + biases['out']
    out_layer = tf.nn.softmax(out_layer)
    out_layer = tf.nn.dropout(out_layer,keep_prob)
    
    return out_layer


