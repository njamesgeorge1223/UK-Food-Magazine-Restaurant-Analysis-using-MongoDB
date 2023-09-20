#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  NoSQLAnalysisFunctions.py
 #
 #  File Description:
 #      This Python script, NoSQLAnalysisFunctions.py, contains generic Python functions
 #      for completing common tasks in the evaluation of restaurant ratings data.  
 #      Here is the list:
 #
 #      InsertJSONFileIntoMongoDBCollection
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/20/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import pandas as pd


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'NoSQLAnalysisFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnReorderedColumnsNoSQLDataFrame
 #
 #  Function Description:
 #      This function receives a NoSQL DataFrame, orders its columns, and returns it 
 #      to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputNoSQLDataFrame
 #                          The parameter is the input DataFrame.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnReorderedColumnsNoSQLDataFrame \
        (inputNoSQLDataFrame):
    
    try:
       
         return \
            inputNoSQLDataFrame \
                [['_id',
                  'FHRSID',
                  'ChangesByServerID',
                  'LocalAuthorityBusinessID',
                  'BusinessName',
                  'BusinessType',
                  'BusinessTypeID',
                  'AddressLine1',
                  'AddressLine2',
                  'AddressLine3',
                  'AddressLine4',
                  'PostCode',
                  'geocode',
                  'Distance',
                  'Phone',
                  'RatingValue',
                  'RatingKey',
                  'RatingDate',
                  'NewRatingPending',
                  'scores',
                  'LocalAuthorityCode',
                  'LocalAuthorityName',
                  'LocalAuthorityWebSite',
                  'LocalAuthorityEmailAddress',
                  'SchemeType',
                  'RightToReply',
                  'meta',
                  'links']]

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnReorderedColumnsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to reorder the columns of a DataFrame.')
    
        return \
            None


# In[ ]:




