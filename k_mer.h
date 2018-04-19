#ifndef K_MER_H_INCLUDED
#define K_MER_H_INCLUDED

#include <math.h>
using namespace std;
int index(int k,std::string r){
    int index =0;

    if(k>0){
        std::string r1 = r.substr(0,1);
        if(r1=="A"||r1=="a") index = index+0*pow(4,k-1);
        else if(r1=="T"||r1=="t") index = index+1*pow(4,k-1);
        else if(r1=="C"||r1=="c") index = index+2*pow(4,k-1);
        else if(r1=="G"||r1=="g") index = index+3*pow(4,k-1);
    }
    if(k>1){
        std::string r2 = r.substr(1,1);
        if(r2=="A"||r2=="a") index = index+0*pow(4,k-2);
        else if(r2=="T"||r2=="t") index = index+1*pow(4,k-2);
        else if(r2=="C"||r2=="c") index = index+2*pow(4,k-2);
        else if(r2=="G"||r2=="g") index = index+3*pow(4,k-2);
    }
    if(k>2){
        std::string r3 = r.substr(2,1);
        if(r3=="A"||r3=="a") index = index+0*pow(4,k-3);
        else if(r3=="T"||r3=="t") index = index+1*pow(4,k-3);
        else if(r3=="C"||r3=="c") index = index+2*pow(4,k-3);
        else if(r3=="G"||r3=="g") index = index+3*pow(4,k-3);
    }
    if(k>3){
        std::string r4 = r.substr(3,1);
        if(r4=="A"||r4=="a") index = index+0*pow(4,k-4);
        else if(r4=="T"||r4=="t") index = index+1*pow(4,k-4);
        else if(r4=="C"||r4=="c") index = index+2*pow(4,k-4);
        else if(r4=="G"||r4=="g") index = index+3*pow(4,k-4);
    }
    if(k>4){
        std::string r5 = r.substr(4,1);
        if(r5=="A"||r5=="a") index = index+0*pow(4,k-5);
        else if(r5=="T"||r5=="t") index = index+1*pow(4,k-5);
        else if(r5=="C"||r5=="c") index = index+2*pow(4,k-5);
        else if(r5=="G"||r5=="g") index = index+3*pow(4,k-5);
    }
    return index;
}

int k_mer(int k,char fileName[]){
    double mer1[4];
    double mer2[16];
    double mer3[64];
    double mer4[256];
    double mer5[1024];

    double wk,sk;
    int ki;

    char *inFile = new char[sizeof(fileName) + 15];
    strcpy(inFile, "tmp/");
    strcat(inFile, fileName);

    char *outFile = new char[sizeof(fileName) + 15];
    strcpy(outFile, "tmp/k_mer_");
    strcat(outFile, fileName);

    std::string line;
    std::ifstream myfile(inFile);
    std::ofstream out(outFile);

    if (myfile.is_open())
    {
        while (getline(myfile,line) ){
            for(int i =0;i<4;i++) {
                mer1[i]=0;
            }
            for(int i =0;i<16;i++){
                mer2[i]=0;
            }
            for(int i =0;i<64;i++){
                mer3[i]=0;
            }
            for(int i =0;i<256;i++) {
                mer4[i]=0;
            }
            for(int i =0;i<1024;i++) {
                mer5[i]=0;
            }
            if(k>0){
                ki = 1;
                for(int i =0;i<line.length()-ki+1;i++){
                    std::string r = line.substr(i,ki);
                    mer1[index(ki,r)] = mer1[index(ki,r)]+1;
                }
                wk = 1/(pow(4,5-ki));
                sk = line.length()-ki+1;
                for(int i =0;i<4;i++){
                    mer1[i] = mer1[i]*wk/sk*100;
                    out<<mer1[i]<<",";
                }
            }
            if(k>1){
                ki = 2;
                for(int i =0;i<line.length()-ki+1;i++){
                    std::string r = line.substr(i,ki);
                    mer2[index(ki,r)] = mer2[index(ki,r)]+1;
                }
                wk = 1/(pow(4,5-ki));
                sk = line.length()-ki+1;
                for(int i =0;i<16;i++){
                    mer2[i] = mer2[i]*wk/sk*100;
                    out<<mer2[i]<<",";
                }
            }
            if(k>2){
                ki = 3;
                for(int i =0;i<line.length()-ki+1;i++){
                    std::string r = line.substr(i,ki);
                    mer3[index(ki,r)] = mer3[index(ki,r)]+1;
                }
                wk = 1/(pow(4,5-ki));
                sk = line.length()-ki+1;
                for(int i =0;i<64;i++){
                    mer3[i] = mer3[i]*wk/sk*100;
                    out<<mer3[i]<<",";
                }
            }
            if(k>3){
                ki = 4;
                for(int i =0;i<line.length()-ki+1;i++){
                    std::string r = line.substr(i,ki);
                    mer4[index(ki,r)] = mer4[index(ki,r)]+1;
                }
                wk = 1/(pow(4,5-ki));
                sk = line.length()-ki+1;
                for(int i =0;i<256;i++){
                    mer4[i] = mer4[i]*wk/sk*100;
                    out<<mer4[i]<<",";
                }
            }
            if(k>4){
                ki = 5;
                for(int i =0;i<line.length()-ki+1;i++){
                    std::string r = line.substr(i,ki);
                    mer5[index(ki,r)] = mer5[index(ki,r)]+1;
                }
                wk = 1/(pow(4,5-ki));
                sk = line.length()-ki+1;
                for(int i =0;i<1024;i++){
                    mer5[i] = mer5[i]*wk/sk*100;
                    out<<mer5[i]<<",";
                }
            }
            if(fileName[0]=='l'){
                out<<"1,0";
            }else if(fileName[1]=='c'){
                out<<"0,1";
            }else if(fileName[1]=='r'){
                out<<"-1,-1";
            }
            out<<endl;

        }

    }
    out.close();
    myfile.close();
}


#endif // K_MER_H_INCLUDED
