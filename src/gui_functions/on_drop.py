from src.algorithm.algorithm import RankingAlgorithm
import networkx as nx
from src.exceptions import InvalidData
from src.pandasinterfaces.csv_to_json_interface import csv_to_json
from src.pandasinterfaces.output_csv import output_csv
from src.predefiend import projects, capacities, demands

def onDrop(inputPath, folder_path):

    # Preferences
    prefs = csv_to_json(projects, inputPath)

    # Directed graph that stores the nodes
    G = nx.DiGraph()

    test = RankingAlgorithm(prefs, capacities, G, projects, demands)
    try:
        test.validate_data()
    except InvalidData as e:
        print(f"Caught an exception: {e}")
        
    test.execute()
    test.print_results()
    projList = test.return_results_as_List()
    output_csv(projList, inputPath, folder_path)
