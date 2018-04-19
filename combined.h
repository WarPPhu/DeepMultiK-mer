#ifndef COMBINED_H_INCLUDED
#define COMBINED_H_INCLUDED
#include<iostream>
using namespace std;
int genFile(int n_train,int n_test){
    string line1;
    string line2;
    bool out = 1;
    ifstream myfile1("tmp/k_mer_lnc");
    ifstream myfile2("tmp/k_mer_pc");

    ofstream out1("Training.csv");
    ofstream out2("Testing.csv");

    int sum = n_train+n_test;

    if (myfile1.is_open()&&myfile2.is_open())
    {
        while (1){
                out = 0;
            if(getline(myfile1,line1)){
                if(n_train) {
                    out1<<line1<<endl;
                    n_train--;
                }
                else if(!n_train&&n_test){
                    out2<<line1<<endl;
                    n_test--;
                }
                out = 1;
            }
            if(getline(myfile2,line2)){
                if(n_train){
                    out1<<line2<<endl;
                    n_train--;
                }
                else if(!n_train&&+n_test){
                    out2<<line2<<endl;
                    n_test--;
                }
                out = 1;
            }
            if(!out) break;
        }

        if(n_train) printf("Warning miss %d train line\n",n_train);
        if(n_test) printf("Warning miss %d test line\n",n_test);

        out1.close();
        myfile1.close();
        out2.close();
        myfile2.close();
    }

}

#endif // COMBINED_H_INCLUDED
