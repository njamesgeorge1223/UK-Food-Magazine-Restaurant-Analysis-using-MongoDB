#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  NoSQLSetupSubRoutines.py
 #
 #  File Description:
 #      This Python script, NoSQLSetupFunctions.py, contains generic Python subroutines
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
 #      This subroutine reads the data from a JSON file and populates a MongoDB 
 #      collection with the information.  It also converts the date and time text
 #      string in the 'RatingDate' fields to a date text string.
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
 #  9/20/2023           Added conversion of 'RatingDate' to date String
 #                                                                  N. James George
 #
 #******************************************************************************************/

def InsertJSONFileIntoMongoDBCollection \
        (pyMongoCollectionObject,
         filePathString):
        
    try:

        with open(filePathString) as jsonFile:
    
            jsonDataObject \
                = json \
                    .load \
                        (jsonFile)

        
            for jsonDictionary in jsonDataObject:
                
                jsonDictionary \
                    ['RatingDate'] \
                        = jsonDictionary \
                            ['RatingDate'] \
                            [0:10]
            
        
        if isinstance(jsonDataObject, list):
            
            pyMongoCollectionObject \
                .insert_many \
                    (jsonDataObject)
            
        else:
            
            pyMongoCollectionObject \
                .insert_one \
                    (jsonDataObject)
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The subroutine, InsertJSONFileIntoMongoDBCollection, ' 
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' 
                 + 'cannot insert a JSON file into a Mongo DB database ' 
                 + 'as a Collection.')


# In[ ]:




