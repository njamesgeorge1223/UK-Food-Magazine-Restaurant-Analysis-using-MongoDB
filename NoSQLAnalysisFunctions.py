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
 #      ReturnReorderedColumnsNoSQLDataFrame
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  09/20/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyLogSubRoutines as log_subroutine

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
 #  09/20/2023          Initial Development                         N. James George
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


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnGeocodeCoordinates
 #
 #  Function Description:
 #      This function returns the latitude and longitude from a geocode Dictionary.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          inputDictionary
 #                          The parameter is the input Dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnGeocodeCoordinates \
        (inputDictionary):
    
    try:
        
        latitudeFloat \
            = inputDictionary['latitude']
    
        longitudeFloat \
            = inputDictionary['longitude']
    
        return latitudeFloat, longitudeFloat
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnGeocodeCoordinates, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to extract latitude and longitude ' 
                 + 'from a Dictionary.')
    
        return \
            None


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnScores
 #
 #  Function Description:
 #      This function returns the hygiene, structural, and confidence scores
 #      from a scores Dictionary.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          inputDictionary
 #                          The parameter is the input Dictionary.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnScores \
        (inputDictionary):
    
    try:
        
        hygieneScoreInteger \
            = inputDictionary['Hygiene']
        
        structuralScoreInteger \
            = inputDictionary['Structural']
        
        confidenceInManagementScoreInteger \
            = inputDictionary['ConfidenceInManagement']
        
        return \
            hygieneScoreInteger, \
            structuralScoreInteger, \
            confidenceInManagementScoreInteger
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnScores, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to extract scores ' 
                 + 'from a Dictionary.')
    
        return \
            None


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnMarkerSize
 #
 #  Function Description:
 #      This function returns a Series of marker sizes from the product of the input Series
 #      and a multiplicative factor parameter.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeries
 #                          The parameter is the input Dictionary.
 #  Float
 #          factorFloat
 #                          The parameter is the multiplicative factor.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMarkerSize \
        (inputSeries,
         factorFloat):
    
    try:
       
        return \
            inputSeries * factorFloat
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnMarkerSize, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a Series of marker sizes.')
    
        return \
            None


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnLocationsDataFrame
 #
 #  Function Description:
 #      This function returns a DataFrame for map display by processing 
 #      an input DataFrame.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputSeries
 #                          The parameter is the input Dictionary.
 #  String
 #          markerSizeColumnNameString
 #                          The parameter is the column name for calculating 
 #                          the marker size.
 #  Float
 #          factorFloat
 #                          The parameter is the multiplicative factor.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/20/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnLocationsDataFrame \
        (inputDataFrame,
         markerSizeColumnNameString,
         factorFloat \
            = 5):
    
    try:
        
        tempDataFrame \
            = inputDataFrame.copy()


        tempDataFrame \
            [['Latitude', 'Longitude']] \
                = inputDataFrame \
                    ['geocode'] \
                        .apply \
                            (lambda x: pd.Series(ReturnGeocodeCoordinates(x)))

        tempDataFrame \
            [['Hygiene', 'Structural', 'ConfidenceInManagement']] \
                = inputDataFrame \
                    ['scores'] \
                        .apply \
                            (lambda x: pd.Series(ReturnScores(x)))

        tempDataFrame \
            ['MarkerSize'] \
                = tempDataFrame \
                    [markerSizeColumnNameString] \
                        .apply \
                            (lambda x: pd.Series(ReturnMarkerSize(x, factorFloat)))

        dropColumnsStringList \
            = ['_id',
               'ChangesByServerID',
               'FHRSID',
               'LocalAuthorityBusinessID',
               'BusinessTypeID',
               'Phone',
               'Distance',
               'RatingKey',
               'RightToReply',
               'SchemeType',
               'geocode',
               'scores',
               'LocalAuthorityCode',
               'LocalAuthorityWebSite',
               'meta',
               'LocalAuthorityEmailAddress',
               'links']

        tempDataFrame \
            .drop \
                (dropColumnsStringList, 
                 axis = 1, 
                 inplace = True)
        
        return \
            tempDataFrame
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnLocationsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a Series of marker sizes.')
    
        return \
            None

