import os
from collections import OrderedDict
import sys


#Workflow
##selection/selectUserDefinedColumns.py
##cleaning/dropUniqueColumns.py
##cleaning/dropColumnsCriteria.py
##cleaning/dropRowsCriteria.py

'''
Import df
select columnss
drop unique cols
Drop missing value criteria
fill missing values
Convert categoricacl to numerical
feature sclaing - standardize/ normalize
split data - RF
'''
#input location
inputDataset = "/home/rajini/FYP/testcsv/test.csv"

#specify output locatiion
outputLocation = "/home/rajini/FYP/gdelt/"


#GDELT variables
#======================
startingDate = '2019.11.26'
endingDate = '2019.12.02'

datafilesLocation = '/home/mpiuser/Downloads/data/'
#select specific country records
Actor1CountryCode = 'LKA'
Actor2CountryCode = 'LKA'

#read csv to pandas df
#inputDataFrame = pd.read_csv(inputDataset)

'''#######################		SELECTION	####################################'''

#select columns
#if "all" select everything. else give a list ["whatever1", "whatever2"]
selectColumns = ["GLOBALEVENTID","SQLDATE", "Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "Actor1EthnicCode", "Actor2EthnicCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"]
#selectColumns = ["SQLDATE", "Actor1Geo_Type", "Actor1Geo_CountryCode","Actor2Geo_Type", "Actor2Geo_CountryCode", "QuadClass", "GoldsteinScale", "NumMentions", "AvgTone"] #done
#selectColumns = ["SQLDATE"]

#select rows
selectFromRow = OrderedDict()
selectFromRow['Year'] = ["2018", "2019"] #doesnt work


'''#######################		CLEANING	####################################'''

#Run anyway - Drop unique columns #done

#user defined missing values
missingValues = ["n/a", "na", "--"]

#drop columns according to user defined empty value percentage
userDefinedColPercentage = 50 #done

#drop rows according to user defined empty value percentage
userDefinedRowPercentage = 30

#drop duplicate rows - run anyway

#Research how best to fill missing values
#mode for user defined columns
modeColumns = "all" #done


'''#######################		TRANSFORMATION	####################################'''

#Normalize
userDefinedNormalizeColumns = ["AvgTone"]

#Split into rows
#add the new column name as last element of list item
userDefinedColumsToAggregate = [["Actor1Geo_CountryCode", "Actor2Geo_CountryCode", "ActorGeo_CountryCode" ]]


#encoding
userDefinedEncodeColumns = ["Actor1Geo_CountryCode"]
