#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main() {

	uint32_t seed = 5;
	while (seed < 8){
		uint32_t index = 0;
		while (index < 5){
			std::ofstream outfile;
			string RAW_path;
			string result_path;
			if (index == 0){
				RAW_path = "./OptimalRawGroup/RAW/raw0.txt";
				result_path = "./Result/AMRR/1_contentions/";
			} else if (index == 1){
				RAW_path = "./OptimalRawGroup/RAW/raw1.txt";
				result_path = "./Result/AMRR/2_contentions/";
			} else if (index == 2){
				RAW_path = "./OptimalRawGroup/RAW/raw2.txt";
				result_path = "./Result/AMRR/4_contentions/";
			} else if (index == 3){
				RAW_path = "./OptimalRawGroup/RAW/raw3.txt";
				result_path = "./Result/AMRR/8_contentions/";
			}  else if (index == 4){
				RAW_path = "./OptimalRawGroup/RAW/raw4.txt";
				result_path = "./Result/AMRR/16_contentions/";
			} else {
				RAW_path = "./OptimalRawGroup/RawConfig-rca.txt";
				result_path = "./Result/test.txt";
			}

			std::cout << "Trying out running" << std::endl;
			string final_result_path;
			string sd = std::to_string(seed);

			uint16_t rh = 250;
			string rho = std::to_string(rh);

			final_result_path = result_path + rho + "_" + sd + ".txt";
			string command = "./waf --run 'rca --simulationTime=110 --seed=" + sd + " --RAWConfigFile='" + RAW_path + "' --rho='" + rho + "' --resultPath='" + final_result_path + "' '";
			system(command.c_str());
			index = index + 1;
		}			
		seed = seed + 1;
    }
		
}
