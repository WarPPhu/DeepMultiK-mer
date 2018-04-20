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
import pandas as pd
import numpy as np

def train(train_data,train_label,test_data,test_label,type,n_input,n_classes,parameter):
    import matplotlib.pyplot as plt
    
    learning_rate = parameter['learning_rate']
    batch_size = parameter['batch_size']
    training_epochs = parameter['training_epochs']
    dropout_keep = parameter['dropout_keep']
    display_step = parameter['display_step']
    log_step = parameter['log_step']
    
    directory = 'traningLog\\'
    if not os.path.exists(directory):
        os.makedirs(directory)
    modelSavePath = os.getcwd()+'\\'+directory+type+'_model\model.ckpt'
    
    n_train = 10
    
    x = tf.placeholder(tf.float32, [None, n_input])
    y = tf.placeholder(tf.float32, [None, n_classes])
    keep_prob = tf.placeholder(tf.float32)
    
    prediction = dm.Model(x,y,keep_prob,n_input,n_classes)
    
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
    correct_pred = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    
    Trainacc_record = []
    Trainloss_record = []
    Testacc_record = []
    Testloss_record = []
    
    init = tf.global_variables_initializer()

    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(training_epochs):
            total_batch = int(n_train/batch_size)
            for i in range(total_batch):
                batch_x = train_data[batch_size*i:batch_size*(i+1)]
                batch_y = train_label[batch_size*i:batch_size*(i+1)]
                sess.run(optimizer, feed_dict={x: batch_x,y: batch_y,keep_prob : dropout_keep})
                
            if epoch % log_step == 0:
                Trainloss, Trainacc = sess.run([loss, accuracy], feed_dict={x: train_data,y: train_label,keep_prob : 1})
                Trainacc_record.append(Trainacc)
                Trainloss_record.append(Trainloss)
            
                Testloss, Testacc = sess.run([loss, accuracy], feed_dict={x: test_data,y: test_label,keep_prob : 1})
                Testacc_record.append(Testacc)
                Testloss_record.append(Testloss)

            if epoch % display_step == 0:
                print(str(epoch)+"Step success")
                
                Testloss, Testacc = sess.run([loss, accuracy], feed_dict={x: test_data,y: test_label,keep_prob : 1})
                print("Step " + str(epoch) + "\nTraining, Loss= " + \
                      "{:.4f}".format(Trainloss) + ", Training Accuracy= " + \
                      "{:.3f}".format(Trainacc))

                print("Test, Loss= " + \
                      "{:.4f}".format(Testloss) + ", Testing Accuracy= " + \
                      "{:.3f}".format(Testacc))
    
        print("Optimization Finished!")

        save_path = saver.save(sess, modelSavePath)
        print("Model saved in file: %s" % save_path)

    
    
    plt.figure(1)
    plt.title("Training Accuracy", fontsize=14)
    plt.plot(pd.Series(np.ravel(Trainacc_record)), "b", markersize=10, label="Traning Accuracy")
    plt.plot(pd.Series(np.ravel(Testacc_record)), "r", markersize=10, label="Testing Accuracy")
    plt.legend(loc="upper left")
    plt.savefig(directory+type+'_accuracy.png')
    plt.clf()
    plt.close()

    plt.figure(2)
    plt.title("Training Loss", fontsize=14)
    plt.plot(pd.Series(np.ravel(Trainloss_record)), "b", markersize=10, label="Training Loss")
    plt.plot(pd.Series(np.ravel(Testloss_record)), "r", markersize=10, label="Testing Loss")
    plt.legend(loc="upper left")
    plt.savefig(directory+type+'_loss.png')
    plt.clf()
    plt.close()
