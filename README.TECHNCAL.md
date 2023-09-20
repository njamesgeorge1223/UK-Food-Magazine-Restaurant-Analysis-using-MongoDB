The IPython notebooks, NoSQLSetup.ipynb and NoSQLAnalysis.ipynb, require the following Python scripts with them in the same folder:

NoSQLSetupSubRoutines.py

PyConstants.py

PyFunctions.py

PyLogConstants.py

PyLogFunctions.py

PyLogSubRoutines.py

PySubroutines.py

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, panel, geoviews, geopy, aspose-words, pymongo.

Here are the requisite Terminal commands for installation of these peripheral modules (in this order) (SQLite is already install on macOS:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install panel

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install pymongo

If the folders, Resources, Logs, and Images are not present, the IPython notebook will create them.

To place the IPython notebook in log mode, debug mode, or image mode set the parameter for the appropriate subroutine in cell #2 to True. In debug mode, the program displays the debug information and writes it to a debug file in the Logs folder; the same is true in log mode for log information sent to a log file in the same folder. If the program is in log mode but not debug mode, it displays no debug information, but writes that information to the log file. If the program is in image mode, it writes all the plots to png files and all maps to html files in the Images folder.
