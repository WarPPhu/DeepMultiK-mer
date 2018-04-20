#####################################################################################
#															   
#  Classification of long non-coding RNAs and messenger RNAs by deep learning method
#  Authors: Phurinut Chanhom						   		  
#  Version: 1.0
#  Updated on: April 20, 2018  
#															   
#####################################################################################

import DeepModel as dm
import os
import tensorflow as tf

def predict(data,out_file,type,n_input,n_classes):
    modelSavePath = os.getcwd()+'\\'+type+'_model\model.ckpt'
    
    x = tf.placeholder(tf.float32, [None, n_input])
    y = tf.placeholder(tf.float32, [None, n_classes])
    keep_prob = tf.placeholder(tf.float32)
    
    prediction = dm.Model(x,y,keep_prob,n_input,n_classes)

    correct_pred = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    init = tf.global_variables_initializer()

    saver = tf.train.Saver()

    with tf.Session() as sess:
    
        sess.run(init)
        saver.restore(sess, modelSavePath)
        print("Prediciton Finished!")
    
        pred = sess.run(prediction, feed_dict={x: data,keep_prob : 1})

    thefile = open(out_file, 'w')
    for i in pred:
        if(i[0]<0.5):
            thefile.write("Protein coding\n")
        else:
            thefile.write("Long non coding\n")
