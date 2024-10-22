from src.algorithm.algorithm import RankingAlgorithm
import networkx as nx
from src.exceptions import InvalidData
from src.pandasinterfaces.csv_to_json_interface import csv_to_json
from src.pandasinterfaces.output_csv import output_csv

'''
This script contains predefined values that are subject to change
'''

#1. List of Projects
projects = ['Electric Bike (8-month)', 'Electric Scooter', 'Electric Skateboard', 'Balance Board', 'Electric Motorcycle',
            'Electric Go-Kart', 'Electric Couch', 'Custom Electronics', 'Other']


#2. Max people for each project
capacities={'Electric Bike (8-month)': 130,'Electric Scooter':130,'Electric Skateboard':310, 'Balance Board': 130,
            'Electric Motorcycle':130, 'Electric Go-Kart': 130, 'Electric Couch': 130, 'Custom Electronics':130, 
            'Other': 130 } 

#3. Min people for each project
demands={'Electric Bike (8-month)': 0,'Electric Scooter':0,'Electric Skateboard':0, 'Balance Board': 0,
            'Electric Motorcycle':0, 'Electric Go-Kart': 0, 'Electric Couch': 0, 'Custom Electronics':0, 
            'Other': 0 } 