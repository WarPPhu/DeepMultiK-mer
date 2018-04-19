#ifndef CLEANFASTA_H_INCLUDED
#define CLEANFASTA_H_INCLUDED
#include <iostream>
using namespace std;

int cleanFile(char fileName[],char out[],int n_data){
    char *outFile = new char[sizeof(out) + 5];
    strcpy(outFile, "tmp/");
    strcat(outFile, out);

    char *labelFile = new char[sizeof(out) + 15];
    strcpy(labelFile, "tmp/");
    strcat(labelFile, out);
    strcat(labelFile, "_label");

    std::ifstream file(fileName);

    std::ofstream label(labelFile);
    std::ofstream outfile(outFile);


    if(!file) {
       return 0;
    }
    std::string line;
    if (file.is_open()){
        getline(file,line);
        label << line << std::endl;
        while (getline(file,line)&&n_data){
            if(line[0]!='>') outfile <<line ;
            else {
                outfile << std::endl;
                label << line << std::endl;
                n_data--;
            }

        }
    }
    outfile.close();
    printf("%s cleaned\n",out);
    return 1;
}

#endif // CLEANFASTA_H_INCLUDED
