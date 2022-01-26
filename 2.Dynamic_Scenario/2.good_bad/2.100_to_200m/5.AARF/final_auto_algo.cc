#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main() {
	uint32_t seed = 5;
	string result_path = "./Result/AARF/AARF_100_200_m_";
	while(seed < 8){
		std::cout << "Trying out running" << std::endl;
		string final_result_path;
		string sd = std::to_string(seed);
		final_result_path = result_path + sd + ".txt";
		string command = "./waf --run 'rca --simulationTime=110 --resultPath='" + final_result_path + "' --seed=" + sd + " '";
		system(command.c_str());
		seed = seed + 1;
	}
}
