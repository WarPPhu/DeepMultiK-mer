///////////////////////////////////////////////////////////////////////////////////////
//															   
//  Classification of long non-coding RNAs and messenger RNAs by deep learning method
//  Authors: Phurinut Chanhom						   		  
//  Version: 1.0
//  Updated on: April 20, 2018  
//															   
///////////////////////////////////////////////////////////////////////////////////////

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <fstream>
#include <direct.h>
#include "cleanFasta.h"
#include "k_mer.h"
#include "combined.h"
#include <iostream>

int main(int argc,char *argv[]){
    printf("\n");

    //default
    int n_train = 5000;
    int n_test = 5000;
    int n_data;

    char file_name_predict[50]="",file_name_lnc[50]="",file_name_pc[50]="";

    // set value
    if(argc>1){
        for(int i=0;i<argc;i++){
            if(!strcmp(argv[i], "-l")){
                strcpy(file_name_lnc,argv[i+1]);
            }
            if(!strcmp(argv[i], "-p")){
                strcpy(file_name_pc,argv[i+1]);
            }
            if(!strcmp(argv[i], "-pd")){
                strcpy(file_name_predict,argv[i+1]);
            }
            if(!strcmp(argv[i], "-trn")){
                n_train = atoi(argv[i+1]);
            }
            if(!strcmp(argv[i], "-ten")){
                n_test = atoi(argv[i+1]);
            }

        }
    }else{
        strcpy(file_name_predict,"predict.fa");
    }
    n_data = (n_train+n_test)/2;

    mkdir("tmp");

    if(strlen(file_name_lnc)>0) {
        if(!cleanFile(file_name_lnc,"lnc",n_data)){
            printf("LNC file not found\n");
            return 0;
        }else k_mer(5,"lnc");
    }
    if(strlen(file_name_pc)>0) {
        if(!cleanFile(file_name_pc,"pc",n_data)){
            printf("Protein file not found\n");
            return 0;
        }else k_mer(5,"pc");
    }
    if(strlen(file_name_predict)>0) {
        if(!cleanFile(file_name_predict,"predict",50000)){
            printf("Predict file not found\n");
            return 0;
        }else k_mer(5,"predict");
    }

    genFile(n_train,n_test);

}
