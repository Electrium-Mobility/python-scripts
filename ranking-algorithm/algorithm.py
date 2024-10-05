import networkx as nx


class RankingAlgorithm:
    '''
    What we expect from users to run this algorithm
    1. Preferences 
    2. Max people for each project
    3. Min people for each project
    '''
    def __init__(self, prefs, capacities, demands, graph, projects):
        self.prefs = prefs  
        self.capacities = capacities  
        self.demands = demands  
        self.graph = graph
        self.projects = projects

    def execute(self):
        G = self.graph
        totalApplicants = len(self.prefs)
        minMembers = 0
        for value in self.demands.values():
            minMembers += value

        for project in self.projects:
            G.add_node(project, demand = self.demands[project])
        G.add_node('destination', demand = totalApplicants - minMembers) #need a place to hold all the demands if they are contained inside 
        for person, projectList in self.prefs.items():
            G.add_node(person, demand = -1) #negative means want to send positive demand means to receive
            for index, project in enumerate(projectList):
                cost =  index * 10 #better choice has lower cost
                G.add_edge(person, project, weight = cost, capacity = 1)
        for project, capacity in self.capacities.items():
            G.add_edge(project, 'destination', weight = 0, capacity = capacity - G.nodes[project]['demand'])
    def print_results(self):
        flowDict = nx.min_cost_flow(self.graph)
        for person in self.prefs:
            for project, flow in flowDict[person].items():
                if flow:
                    print (person,'joins',project)