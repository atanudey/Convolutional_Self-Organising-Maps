#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:26:52 2017

@author: ayanava
"""

import numpy as np
import csv
import matplotlib.pyplot as plt

row = 0
col = 0

l = []
final = []


with open('mnist_test_10.csv', 'r') as csv_file:
    for data in csv.reader(csv_file):
        arr=np.zeros((24*24,25), dtype='int')
        # The first column is the label
        label = data[0]

        # The rest of columns are pixels
        pixels = data[1:]

        # Make those columns into a array of 8-bits pixels
        # This array will be of 1D with length 784
        # The pixel intensity values are integers from 0 to 255
        pixels = np.array(pixels, dtype='int64')
        print (pixels[0]).dtype
        # Reshape the array into 28 x 28 array (2-dimensional array)
        pixels = pixels.reshape((28, 28))
        
        ### Implementing the "np.take"
        counter = 0
        while(row<24):
            col=0
            while(col<24):
                for i in range (0, 5):
                    
                    l= list(range(col,col+5))
                
                #l=([row:row+5, col:col+5]).tolist()
                '''
                for i in range(0,5):
                    for j in range(0,5):
                                              
                        arr[counter,i+j]= l[i][j]
                        
                print np.max(arr)
                '''
                print l
                del l[:]
                col=col+1
                counter = counter+1
                    
                
            row=row+1        
        
        
        
        
        # Plot
        '''
        counter = 0
        row=0
        while(row<24):
            col=0
            while(col<24):
                l=(pixels[row:row+5, col:col+5]).tolist()
                #print len(l)
                for i in range(0,5):
                    for j in range(0,5):
                        #final.append(l[i][j])
                        
                        arr[counter,i+j]= l[i][j]
                        
                #print "DONE"
                #print arr[counter]
                print np.max(arr)
                del l[:]
                col=col+1
                counter = counter+1
               
            row=row+1
        print (np.array(l)).size
        
        print arr[566]
        #plt.title('Label is {label}'.format(label=label))
        #plt.imshow(arr, cmap='gray')
        #plt.show()
        print np.max(arr)
        np.save('arr.npy', arr)
        break
        '''