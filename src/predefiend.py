from src.algorithm.algorithm import RankingAlgorithm
import networkx as nx
from src.exceptions import InvalidData
from src.pandasinterfaces.csv_to_json_interface import csv_to_json
from src.pandasinterfaces.output_csv import output_csv

'''
This script contains predefined values that are subject to change
'''

#1. List of Projects
projects = ['Electric Longtail Conversion Kit', 'Onewheel', 'Electric Road Bike', 'Gokart', 'Electric Sofa',
            'Custom ESC', 'Custom Remote Control', 'Battery Management System', 'Other']


#2. Max people for each project
capacities={'Electric Longtail Conversion Kit': 10,'Onewheel':10,'Electric Road Bike':10, 'Gokart': 10,
            'Electric Sofa':10, 'Custom ESC': 10, 'Custom Remote Control': 10, 'Battery Management System':10, 
            'Other': 10 } 

#3. Min people for each project
demands={'Electric Longtail Conversion Kit': 4,'Onewheel': 4,'Electric Road Bike':4, 'Gokart': 4,
            'Electric Sofa': 4, 'Custom ESC': 4, 'Custom Remote Control': 0, 'Battery Management System':4, 
            'Other': 4} 