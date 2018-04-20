#####################################################################################
#															   
#  Classification of long non-coding RNAs and messenger RNAs by deep learning method
#  Authors: Phurinut Chanhom						   		  
#  Version: 1.0
#  Updated on: April 20, 2018  
#															   
#####################################################################################

from __future__ import print_function
import sys,csv
import numpy as np
import pandas as pd
import train_Model as tm

k = [1,2,3,4,5]                     #k-mers
n_input = sum([4**x for x in k])
n_classes = 2

parameter = {
    'learning_rate': 0.0001,
    'batch_size': 10,
    'training_epochs': 200,
    'dropout_keep': 0.5,
    'display_step': 10,
    'log_step': 10,
}

def main():
    #default
    type = 'Human'
    train_file = "Train.csv"
    test_file = "Test.csv"
    
    if(len(sys.argv)>0):
        for i in range(1,len(sys.argv)):
            if(sys.argv[i]=='-t'):
                type = sys.argv[i+1]
            if(sys.argv[i]=='-tr'):
                train_file = sys.argv[i+1]
            if(sys.argv[i]=='-te'):
                test_file = sys.argv[i+1]
    
    try:
        df1 = pd.read_csv(train_file, header=None)
        train_data = np.array(df1.iloc[:,0:n_input].copy())
        train_label = np.array(df1.iloc[:,n_input:n_input+n_classes].copy())

        df1 = pd.read_csv(test_file, header=None)
        test_data = np.array(df1.iloc[:,0:n_input].copy())
        test_label = np.array(df1.iloc[:,n_input:n_input+n_classes].copy())
    except FileNotFoundError:
        print("File not found")
        return

    if len(test_label[0])!=2 or len(test_label[0])!=2 :
        print("Wrong input file")
        return

    tm.train(train_data,train_label,test_data,test_label,type,n_input,n_classes,parameter)


if __name__ == "__main__":
    main()
