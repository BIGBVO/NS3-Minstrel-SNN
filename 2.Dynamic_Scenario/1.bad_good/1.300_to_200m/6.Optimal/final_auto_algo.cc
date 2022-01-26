#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int main() {
	uint32_t seed = 5;
	string result_path = "./Result/Optimal/Optimal_300_200_m_";
	while(seed < 8){
		std::cout << "Trying out running" << std::endl;
			string final_result_path;
			string sd = std::to_string(seed);
			//final_result_path = result_path + sd + ".txt";
			final_result_path = result_path + sd + ".txt";
			string fix_command = "./waf --run 'rca --simulationTime=110 --resultPath='" + final_result_path + "' --seed=" + sd;
			for (int i = 0; i < 3; i++){
				if (i == 0){
					string mcs = "MCS1_";
					for (int j = 0; j < 10; j++){
						outfile.open(result_path, std::ios_base::app);
						outfile << "\n";
						outfile.close();
						string DataMode = mcs + std::to_string(j);
						string command = fix_command + " --DataMode='" + DataMode + "' '";
						system(command.c_str());
					}
				}

				else if (i == 1){
					string mcs = "MCS2_";
					for (int j = 0; j < 9; j++){
						outfile.open(result_path, std::ios_base::app);
						outfile << "\n";
						outfile.close();
						string DataMode = mcs + std::to_string(j);
						string command = fix_command + " --DataMode='" + DataMode + "' '";
						system(command.c_str());
					}
				}

				else if (i == 2){
					string mcs = "MCS4_";
					for (int j = 0; j < 10; j++){
						outfile.open(result_path, std::ios_base::app);
						outfile << "\n";
						outfile.close();
						string DataMode = mcs + std::to_string(j);
						string command = fix_command + " --DataMode='" + DataMode + "' '";
						system(command.c_str());
					}
				}
			}
			seed = seed + 1;
	}
}