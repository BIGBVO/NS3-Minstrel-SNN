import tensorflow as tf
from tensorflow import keras

import numpy as np
import math

from py_interface import *
from ctypes import *
Init(1234, 4096)

num_MCSs = 26

class mcsFeature(Structure):
    _pack_ = 1
    _fields_ = [
        ('sinr', c_double)
    ]

class mcsPredicted(Structure):
    _pack_ = 1
    _fields_ = [
        ('new_MCS', c_uint32),
    ]

class mcsTarget(Structure):
    _pack_ = 1
    _fields_ = [
        ('target', c_uint8)
    ]

dl = Ns3AIDL(1371, mcsFeature, mcsPredicted, mcsTarget)


mcs_list_4 = [28,27,26,25,24,23,18,17,16,22,15,21,9,14,8,7,20,6,13,5,12,4,19,11,2,10,1,0]
try:
    while True:
        with dl as data:
            print("WAITING FOR DATA")
            if data == None:
                break
            # print('data.feat.wbCqi', data.feat.wbCqi)
            # Deep Learning code there

            #signal = -math.log10((snr/1.98)*(3.83*pow(10,-14)))
            sinr = data.feat.sinr
            sinr_log = np.array([np.log(sinr)])
            mcs_rate = 0;
            f = open("log.txt", "a")
            f.write("==" + str(sinr) + " || " + str(sinr_log) + " ==\n")
            

            print("sinr:", sinr, "sinr_log:", sinr_log)
            for idx_model in mcs_list_4:
                model=keras.models.load_model(f'Models/mcs{idx_model}_model.h5')
                pred = model.predict(sinr_log)
                f.write(str(idx_model) + ": " + str(pred) + "\n")
                if np.round(pred) == 1:
                    mcs_rate = idx_model
                    break
            
            f.close()
            #mcs_index = 0
            #max = 0
            
            #for idx, value in enumerate(prediction[0]):
            #    if (value > max):
            #        max = value
            #        mcs_index = idx

            print("mcs_index= ", mcs_rate)
            data.pred.new_MCS = mcs_rate
            
except KeyboardInterrupt:
    print('Ctrl C')
finally:
    FreeMemory()