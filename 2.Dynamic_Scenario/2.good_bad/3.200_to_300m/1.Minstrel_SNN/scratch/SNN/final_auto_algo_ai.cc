#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main() {

	uint32_t test = 2;
	while (test > 0){
		string command = "python  AI.py";
		system(command.c_str());
		test = test - 1;
    }

	std::cout<<"" <<std::endl;
	std::cout<<"success"<<std::endl;
}
