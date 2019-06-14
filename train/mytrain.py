#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import warnings
warnings.filterwarnings('ignore')

import keras
keras.backend.clear_session()

# change this property
NOMEROFF_NET_DIR = os.path.abspath('../')
VERSION = "4"
DATASET_NAME = ""
MODE = "cpu"
PATH_TO_DATASET = os.path.join(NOMEROFF_NET_DIR, "datasets/", DATASET_NAME)
RESULT_MODEL_PATH = os.path.join(NOMEROFF_NET_DIR, "models/", 'anpr_ocr_kz_{}-{}.h5'.format(VERSION, MODE))

# FROZEN_MODEL_PATH = os.path.join(NOMEROFF_NET_DIR, "models/", 'anpr_ocr_{}_{}-{}.pb'.format(DATASET_NAME, VERSION, MODE))

sys.path.append(NOMEROFF_NET_DIR)

from NomeroffNet.Base import OCR, convert_keras_to_freeze_pb


# In[2]:


class kz(OCR):
    def __init__(self):
        OCR.__init__(self)
        # only for usage model
        # in train generate automaticly
        self.letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C","D", "E","F","G", "H", "I","J", "K","L", "M","N", "O", "P","Q", "R","S","T","U","V","W","X", "Y", "Z"]
        
        self.EPOCHS = 5


# In[3]:


ocrTextDetector = kz()
model = ocrTextDetector.prepare(PATH_TO_DATASET, aug_count=0)


# In[4]:


# model = ocrTextDetector.load(RESULT_MODEL_PATH)
# RESULT_MODEL_PATH


# In[5]:


model = ocrTextDetector.train(mode=MODE)


# In[6]:


ocrTextDetector.test(verbose=True)


# In[7]:


# Result = "../models/thirdtry.pb"
res = "../models/fifthtry.h5"
# ocrTextDetector.save(Result, verbose=True)
ocrTextDetector.save(res, verbose=True)


# In[29]:





# In[32]:





# In[ ]:




