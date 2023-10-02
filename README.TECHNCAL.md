# **UK Food Magazine Restaurant Analysis using MongoDB**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, pymongo, MongoDB.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

python3 -m pip install pymongo

https://www.mongodb.com/docs/v6.0/tutorial/install-mongodb-on-os-x/ \
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

----

### **Usage:**

----

The IPython notebooks, NoSQLSetup.ipynb and NoSQLAnalysis.ipynb, require the following Python scripts with them in the same folder:

NoSQLSetupSubRoutines.py

NoSQLAnalysisFunctions.py

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

If the folders, Resources, Logs, and Images are not present, an IPython notebook will create them.  The Resources folder holds the input file for the IPython Notebook, NoSQLSetup.ipynb; the Logs folder contains debug and log files from testing the IPython Notebooks; and the Images folder has the PNG image files of the IPython Notebooks' tables and plots.

To place the IPython notebook in log mode, debug mode, or image mode set the parameter for the appropriate subroutine in coding cell #2 to True. In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in log mode for log information sent to a log file. If the program is in log mode but not debug mode, it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes all DataFrames, hvplot maps, and matplotlib plots to png files in the Images folder.

----

### **Resource Summary:**

----

#### Source code

NoSQLSetup.ipynb, NoSQLAnalysis.ipynb

#### Input files

establishments.json

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, MongoDB, Numpy, Pandas, PyMongo, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./NoSQLAnalysis.ipynb](./NoSQLAnalysis.ipynb)

|&rarr; [./NoSQLAnalysisFunctions.py](./NoSQLAnalysisFunctions.py)

|&rarr; [./NoSQLSetup.ipynb](./NoSQLSetup.ipynb)

|&rarr; [./NoSQLSetUpSubRoutines.py](./NoSQLSetUpSubRoutines.py)

|&rarr; [./PyConstants.py](./PyConstants.py)

|&rarr; [./PyFunctions.py](./PyFunctions.py)

|&rarr; [./PyLogConstants.py](./PyLogConstants.py)

|&rarr; [./PyLogFunctions.py](./PyLogFunctions.py)

|&rarr; [./PyLogSubRoutines.py](./PyLogSubRoutines.py)

|&rarr; [./PySubRoutines.py](./PySubRoutines.py)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./Table-Of-Contents-UFMRAUM.md](./Table-Of-Contents-UFMRAUM.md)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/NoSQLAnalysisFigure211WorstHygieneEstablishments.png](./Images/NoSQLAnalysisFigure211WorstHygieneEstablishments.png)
  
  &emsp; |&rarr; [./Images/NoSQLAnalysisFigure212WorstHygieneEstablishmentsCloseUp.png](./Images/NoSQLAnalysisFigure212WorstHygieneEstablishmentsCloseUp.png)
  
  &emsp; |&rarr; [./Images/NoSQLAnalysisFigure221HighRatingValueLondon.png](./Images/NoSQLAnalysisFigure221HighRatingValueLondon.png)
  
  &emsp; |&rarr; [./Images/NoSQLAnalysisFigure222HighRatingValueLondonCloseUp.png](./Images/NoSQLAnalysisFigure222HighRatingValueLondonCloseUp.png)

  &emsp; |&rarr; [./Images/NoSQLAnalysisFigure232HighestRatingBestHygieneCloseUp.png](./Images/NoSQLAnalysisFigure232HighestRatingBestHygieneCloseUp.png)

  &emsp; |&rarr; [./Images/NoSQLAnalysisTable21WorstHygieneEstablishments.png](./Images/NoSQLAnalysisTable21WorstHygieneEstablishments.png)

  &emsp; |&rarr; [./Images/NoSQLAnalysisTable22HighRatingValueLondonEstablishments.png](./Images/NoSQLAnalysisTable22HighRatingValueLondonEstablishments.png)

  &emsp; |&rarr; [./Images/NoSQLAnalysisTable23HighestRatingBestHygieneEstablishments.png](./Images/NoSQLAnalysisTable23HighestRatingBestHygieneEstablishments.png)

  &emsp; |&rarr; [./Images/NoSQLAnalysisTable24LocalAuthoritieswithNumberofEstablishmentswithHighestHygieneScore.png](./Images/NoSQLAnalysisTable24LocalAuthoritieswithNumberofEstablishmentswithHighestHygieneScore.png)

  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20231001NoSQLAnalysisDebug.txt](./Logs/20231001NoSQLAnalysisDebug.txt)

  &emsp; |&rarr; [./Logs/20231001NoSQLAnalysisLog.txt](./Logs/20231001NoSQLAnalysisLog.txt)

  &emsp; |&rarr; [./Logs/20231001NoSQLSetupDebug.txt](./Logs/20231001NoSQLSetupDebug.txt)

  &emsp; |&rarr; [./Logs/20231001NoSQLSetupLog.txt](./Logs/20231001NoSQLSetupLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/establishments.json](./Resources/establishments.json)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[MongoDB Documentation](https://www.mongodb.com/docs/)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
