import pytest
import networkx as nx
from source.exceptions import InvalidData
from source.algorithm.algorithm import RankingAlgorithm

@pytest.fixture
def test_graph():
    return nx.DiGraph()

@pytest.fixture
def valid_project_setup():
    prefs = {
        "Alice": ["Project1", "Project2"],
        "Bob": ["Project2", "Project1"],
        "Carol": ["Project1", "Project2"],
        "Dave": ["Project2", "Project1"],
        "Eve": ["Project1", "Project2"]
    }
    capacities = {"Project1": 3, "Project2": 2}
    demands = {"Project1": 2, "Project2": 2}
    projects = ["Project1", "Project2"]
    return prefs, capacities, demands, projects

@pytest.mark.parametrize("prefs,capacities,demands,projects", [
    (None, {"Project1": 3, "Project2": 2}, {"Project1": 2, "Project2": 2}, ["Project1", "Project2"]),
    ({"Alice": ["Project1", "Project2"]}, None, {"Project1": 2, "Project2": 2}, ["Project1", "Project2"]),
    ({"Alice": ["Project1", "Project2"]}, {"Project1": 3, "Project2": 2}, {"Project1": 2, "Project2": 2}, None)
])
def test_missing_data_raises_invalid_data(test_graph, prefs, capacities, demands, projects):
    with pytest.raises(InvalidData):
        alg = RankingAlgorithm(prefs, capacities, test_graph, projects, demands)
        alg.validate_data()

def test_algorithm_correctness(test_graph, valid_project_setup):
    prefs, capacities, demands, projects = valid_project_setup
    alg = RankingAlgorithm(prefs, capacities, test_graph, projects, demands)
    alg.validate_data()
    alg.execute()
    flow_dict = nx.min_cost_flow(test_graph)
    assert flow_dict["Alice"]["Project1"] == 1
    assert flow_dict["Bob"]["Project2"] == 1
    assert flow_dict["Carol"]["Project1"] == 1
    assert flow_dict["Dave"]["Project2"] == 1
    assert flow_dict["Eve"]["Project1"] == 1

@pytest.mark.raises
def test_overcapacity_scenario(test_graph, valid_project_setup):
    prefs, capacities, demands, projects = valid_project_setup
    capacities.update({"Project1": 5})  # More capacity than needed
    alg = RankingAlgorithm(prefs, capacities, test_graph, projects, demands)
    alg.validate_data()
    alg.execute()
    flow_dict = nx.min_cost_flow(test_graph)
    # Ensuring the destination node is handling excess correctly
    assert sum(flow_dict[proj]["destination"] for proj in projects) == len(prefs) - sum(demands.values())

# @pytest.mark.raises
# def test_undercapacity_scenario(test_graph, valid_project_setup):
#     prefs, capacities, demands, projects = valid_project_setup
#     demands.update({"Project1": 4})  # More demand than capacity
#     with pytest.raises(InvalidData):
#         alg = RankingAlgorithm(prefs, capacities, test_graph, projects, demands)
#         alg.validate_data()

# @pytest.mark.raises
# def test_invalid_preferences_scenario(test_graph, valid_project_setup):
#     prefs, capacities, demands, projects = valid_project_setup
#     prefs.update({"Alice": ["Project3"]})  # Invalid project preference
#     with pytest.raises(KeyError):
#         alg = RankingAlgorithm(prefs, capacities, test_graph, projects, demands)
#         alg.execute()

# # New test for default demands
# def test_default_demands(test_graph, valid_project_setup):
#     prefs, capacities, _, projects = valid_project_setup  # No demands provided
#     alg = RankingAlgorithm(prefs, capacities, test_graph, projects)
#     alg.validate_data()
#     alg.execute()
#     flow_dict = nx.min_cost_flow(test_graph)
#     # Check if the flow meets the calculated default demands (assuming calc_default_num function is working correctly)
#     expected_demands = {project: len(prefs) // len(projects) for project in projects}  # Simple default division
#     assert all(flow_dict[proj]["destination"] == expected_demands[proj] for proj in projects)
