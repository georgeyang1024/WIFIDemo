#coding=utf-8
from LMDB import LMDB
import matplotlib.pyplot as plt
import numpy as np 

'''
���ܣ�������ʵЧ��

'''
#read the sample data
Train_loc1 = open('loc1.txt');

#��ȡָ�����ݿ�
lmdb = LMDB('LMDB_std')

walk = []

while True:
    #���ж�ȡ
    wifiEntry = Train_loc1.readline()
    #ȥ���ո���߻��з�
    wifiEntry = wifiEntry.strip()
    if not wifiEntry or len(wifiEntry) < 10: 
        break;
    location = lmdb.nn_location(wifiEntry)
    walk.append(location)
Train_loc1.close()  
print(walk)   


