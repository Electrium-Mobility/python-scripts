import pandas as pd

from src.exceptions import InvalidData
from ..functional_methods.check_invalid_project import check_invalid_project

def csv_to_json(projects):
    df = pd.read_csv('../python-scripts/src/Signup.csv')
    # df = pd.read_csv('Signup.csv')
    prefsDic = {}
    for index, row in df.iterrows():
        # print (str((row['Project(s) you\'re interested in'])))
        if str(row['Name']) != 'nan': #Filtering out the empty rows
            if str(row['Project(s) you\'re interested in']) == 'nan': #if applicants don't enter a valid project, given an default project List
                projList = projects
            else:
                projPref = row['Project(s) you\'re interested in']
                projList = projPref.split(', ')
                # print (projList)
                # print(projects)
                try:
                    check_invalid_project(projList, projects) #Ensuring that the project list has no invalid project name
                except InvalidData as e:
                    projList = projects
            appName =  row['Name']
            prefsDic[appName] = projList
    return prefsDic