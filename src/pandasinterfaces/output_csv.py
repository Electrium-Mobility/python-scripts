import pandas as pd
from ..functional_methods.check_invalid_project import check_invalid_project


def output_csv(assignedProj):
    df = pd.read_csv('../python-scripts/src/Signup.csv')
    for index, row in df.iterrows():
        if str(row['Name']) != 'nan': #Filtering out the empty rows
            df.loc[index, 'Project (if applicable)'] = str(assignedProj[index])
    df.to_csv("../python-scripts/src/New.csv", index = True)
        