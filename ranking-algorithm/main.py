from algorithm import RankingAlgorithm
import networkx as nx


#1. Preferences
prefs ={'Tom':['Project1','Project2','Project3'],
       'Dick':['Project2','Project1','Project3'],
       'Harry':['Project3','Project2','Project1']}
#2. Max people for each project
capacities={'Project1':3,'Project2':3,'Project3':3} 

#3. Min people for each project
demands={'Project1': 0 ,'Project2':0,'Project3':2} 

#4. Directed graph that stores the nodes
G = nx.DiGraph()

#5. List of Projects
projects = ['Project1', 'Project2', 'Project3']

G = nx.DiGraph()

test = RankingAlgorithm(prefs, capacities, demands, G, projects)
test.execute()
test.print_results()