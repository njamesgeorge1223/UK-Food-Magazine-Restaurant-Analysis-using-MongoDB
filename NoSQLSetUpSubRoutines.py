#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  NoSQLSetupSubRoutines.py
 #
 #  File Description:
 #      This Python script, NoSQLSetupFunctions.py, contains generic Python functions
 #      for completing common tasks in the evaluation of restaurant ratings data.  
 #      Here is the list:
 #
 #      InsertJSONFileIntoMongoDBCollection
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/18/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyLogSubRoutines as log_subroutine

import json


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'NoSQLSetupSubroutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  InsertJSONFileIntoMongoDBCollection
 #
 #  Subroutine Description:
 #      This subroutine reads the data from a JSON file and populates a MongoDB collection
 #      with the information.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  PyMongoCollectionObject
 #          pyMongoCollectionObject
 #                          This parameter is the PyMongoCollectionObject
 #                          for the current collection.
 #  String
 #          filePathString
 #                          This parameter is the file path for the JSON data file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def InsertJSONFileIntoMongoDBCollection \
        (pyMongoCollectionObject,
         filePathString):
        
    try:

        with open(filePathString) as jsonFile:
    
            jsonDataList \
                = json \
                    .load \
                        (jsonFile)

            jsonFile \
                .close()

        if isinstance(jsonDataList, list):
            
            pyMongoCollectionObject \
                .insert_many \
                    (jsonDataList)
            
        else:
            
            pyMongoCollectionObject \
                .insert_one \
                    (jsonDataList)
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The subroutine, InsertJSONFileIntoMongoDBCollection, ' 
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' 
                 + 'cannot insert a JSON file into a Mongo DB database ' 
                 + 'as a Collection.')


# In[ ]:




