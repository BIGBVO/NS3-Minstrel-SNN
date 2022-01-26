### Minstrel_SNN in IEEE 802.11ah
> alpha version

This repository holds the implementation of Minstrell_SNN for the IEEE 802.11ah (Wi-Fi Halow) protocol in NS-3. This work uses the 802.11ah module in NS-3 deveopled by (https://github.com/imec-idlab/IEEE-802.11ah-ns-3) and the NS3 AI module developed by (https://github.com/hust-diangroup/ns3-ai).

This repository contains 3 modules:
* The stationary scenario module,
* The dynamic scenario module, and
* The SNN training module.

### Installation and usage instructions ###

* Open linux terimanal then:
```
sudo apt-get update
sudo apt-get -y install gcc g++ python
sudo apt-get -y install gcc g++ python python-dev
sudo apt-get -y install qt4-dev-tools libqt4-dev
sudo apt-get -y install mercurial
sudo apt-get -y install bzr
sudo apt-get -y install cmake libc6-dev libc6-dev-i386 g++-multilib
sudo apt-get -y install gdb valgrind
sudo apt-get -y install gsl-bin libgsl2 libgsl2:i386
sudo apt-get -y install flex bison libfl-dev
sudo apt-get -y install tcpdump
sudo apt-get -y install sqlite sqlite3 libsqlite3-dev
sudo apt-get -y install libxml2 libxml2-dev
sudo apt-get -y install libgtk2.0-0 libgtk2.0-dev
sudo apt-get -y install vtun lxc
sudo apt -y install git
sudo apt install python3-pip
pip install keras

git clone https://github.sydney.edu.au/vona0880/NS3_Minstrel_SNN.git
```

* Change into the simulation target directory (1.stationary/2.dynamic).
* Change the target Rate adaptation algorithm (1. Minstrel_SNN, 2. Minstrel_Orig_10, 3. Minstrel_Orig_25, 4.AMRR, 5. AARF, 6.Optimal)
* Configure waf (Note that this need to be done for every scenario and/or rate adaptation):
`CXXFLAGS="-std=c++11" ./waf configure --disable-examples --disable-tests`
* Build:
`./waf`
* If an error occur go to build/ns3/wifi-module.h and comment out [#include "mcs-dl-env.h"] (line 43), otherwise go to next step.
* Compile the simulation by using (this will automatomatically run 3 realisation):
`gcc final_auto_algo.cc -o final_auto_algo`
* If Minstrel_SNN is the target simulation, open a new terminal, go to /scratch/SNN and run:
`python3 AI.py`
* Finally, run the 802.11ah simulation by (The simulation result can be found in the Result folder):
`./final_auto_algo`

  
