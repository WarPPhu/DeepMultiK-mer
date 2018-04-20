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
import predict_Model as pm

k = [1,2,3,4,5]                     #k-mers
n_input = sum([4**x for x in k])
n_classes = 2
    
def main():
    #default
    predict_file = "tmp/k_mer_predict.csv"     
    out_file = "Predict_Result.csv"
    type = 'Human'

    if(len(sys.argv)>0):
        for i in range(1,len(sys.argv)):
            if(sys.argv[i]=='-p'):
                predict_file = sys.argv[i+1]
            if(sys.argv[i]=='-o'):
                out_file = sys.argv[i+1]
            if(sys.argv[i]=='-t'):
                type = sys.argv[i+1]

    try:
        df1 = pd.read_csv(predict_file, header=None)
        data = np.array(df1.iloc[:,0:n_input].copy())
    except FileNotFoundError:
        print(predict_file +" file not found")
        return

    if len(data[0])!=n_input :
        print("Wrong input file")
        return

    
    pm.predict(data,out_file,type,n_input,n_classes)
        

if __name__ == "__main__":
    main()
