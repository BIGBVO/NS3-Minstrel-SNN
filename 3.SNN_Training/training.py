#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Mon Mar 15 19:44:29 2021

 

@author: vincentonasis

"""

 

import pandas

import numpy as np

 

from tensorflow import keras

from tensorflow.keras.callbacks import ModelCheckpoint

from sklearn.preprocessing import MinMaxScaler


for i in range(22, 23):
 

    mcs = "mcs"+str(i)
    
    print(mcs)
    
    dataframe = pandas.read_csv(f'Train_Data_New/{mcs}.csv', header=None)
    
    data = dataframe.sample(frac=1)
    
    dataset = data.values
    
    features = dataset[:,0].astype(float)
    
    targets = dataset[:,1].astype(int)
    
    SINR = np.expand_dims(np.log(features),1)
    
    # scaler = MinMaxScaler(feature_range=(1,2))
    # SINR = scaler.fit_transform(SINR)
    
    targets = np.expand_dims(targets,1)
    
    print("SINR.shape:", SINR.shape)
    
    print("targets.shape:", targets.shape)
    
     
    num_val_samples = int(len(SINR) * 0.2)
    
    train_SINRs = SINR[:-num_val_samples]
    
    train_targets = targets[:-num_val_samples]
    
    val_SINRs = SINR[-num_val_samples:]
    
    val_targets = targets[-num_val_samples:]
    
    
    print("Number of training samples:", len(train_SINRs))
    
    print("Number of validation samples:", len(val_SINRs))
    
     
    counts = np.bincount(train_targets[:, 0])
    
    print(
    
        "Number of positive samples in training data: {} ({:.2f}% of total)".format(
    
            counts[1], 100 * float(counts[1]) / len(train_targets)
    
        )
    
    )
    
     
    weight_for_0 = 1.0 / counts[0]
    
    weight_for_1 = 1.0 / counts[1]
    
    
    model = keras.Sequential([
            keras.layers.InputLayer(input_shape=(1,)),
            keras.layers.Dense(64),
            keras.layers.Dense(1, activation="sigmoid")
        ])
    
    model.summary()
    
    metrics = [
    
        keras.metrics.FalseNegatives(name="fn"),
    
        keras.metrics.FalsePositives(name="fp"),
    
        keras.metrics.TrueNegatives(name="tn"),
    
        keras.metrics.TruePositives(name="tp"),
    
        keras.metrics.Precision(name="precision"),
    
        keras.metrics.Recall(name="recall"),
    
        keras.metrics.BinaryAccuracy(name="accuracy")
    
    ]
    
     
    
    class_weight = {0: weight_for_0, 1: weight_for_1}
    
    es = keras.callbacks.EarlyStopping(monitor ='val_accuracy', patience=100) 
    
    checkpoint = ModelCheckpoint(f'Models/{mcs}_model.h5',
    
                                 monitor='val_accuracy',
    
                                 mode='max',
    
                                 verbose=1,
    
                                 save_best_only=True,
    
                                 save_weights_only=False, )
    
    ls = keras.losses.BinaryCrossentropy (from_logits=True, name='binary_crossentropy')
    
    model.compile(
    
        optimizer=keras.optimizers.Adam(1e-4), loss = "binary_crossentropy", metrics=metrics
    )
    
     
    
    #callbacks = [keras.callbacks.ModelCheckpoint(f'Models/{mcs}_model.h5')]
    
     
    
    model.fit(
    
        train_SINRs,
    
        train_targets,
    
        batch_size=64,
    
        epochs=100,
    
        verbose=1,
    
        callbacks=[checkpoint, es],
    
        validation_data=(val_SINRs, val_targets),
    
        class_weight=class_weight,
    
    )
    
     
    
    model.save(f'Models/{mcs}_model.h5')

 

# import matplotlib as plt

 

# plt.pyplot(train_features)

    # from sklearn import preprocessing
    
    # scaler = preprocessing.StandardScaler().fit(train_features)
    
    # train_features = scaler.transform(train_features)
    
     
    
    # mean = np.expand_dims(np.mean(train_SINRs, axis=0),0)
    
    # train_SINRs -= mean
    
    # val_SINRs-= mean
    
     
    # train_features[:,0] -= mean[:,0]
    
    # train_features[:,2] -= mean[:,2]
    
    # val_features[:,0] -= mean[:,0]
    
    # val_features[:,2] -= mean[:,2]
    
     
    
    # train_features
    
     
    
    # std = np.expand_dims(np.std(train_SINRs, axis=0),0)
    
    # train_SINRs/=std
    
    # val_SINRs/= std
    
     
    
    # train_features[:,0] /= std[:,0]
    
    # train_features[:,2] /= std[:,2]
    
    # val_features[:,0] /= std[:,0]
    
    # val_features[:,2] /= std[:,2]
    
     
    
    # mean[:,1] *= 10^2
    
    # train_features[:,1] /= mean[:,1]
    
    # val_features[:,1] /= mean[:,1]
    
     
    
    # with open(f'Record/{mcs}.txt', 'w') as f:
    
    #     for item in mean[0]:
    
    #         f.write("%s \t" % item)
    
    #     f.write("\n")
    
    #     for item in std[0]:
    
    #         f.write("%s \t" % item)
    
    #     f.write("\n")
    