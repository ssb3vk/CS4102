#include<iostream>
#include<ctime>
#include<fstream>
#include"ClosestPair.cpp"

int main(int argc, char** argv) {
    string fileName = "test1.txt";
    ifstream inFile;
    inFile.open(fileName.c_str());

    vector<string> lines;
    string line;

    if (inFile.is_open()) {
        while (!inFile.eof()) {
            getline(inFile, line);
            lines.push_back(line);
        }
        inFile.close(); // CLose input file
			
        // Call method and print the result
        time_t start = time(NULL);
        ClosestPair cp; 
        vector<double> res = cp.compute(lines);
        cout << res.at(0) << ", " << res.at(1) << "\n";
        time_t end = time(NULL);
        cout << "time: " << (end - start) << "\n";
    }
    else { //Error message
        cerr << "Error opening file " << fileName << endl;
    }
}

