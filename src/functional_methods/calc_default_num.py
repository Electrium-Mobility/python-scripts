from src.exceptions import InvalidData


def calc_default_num (prefs, projects):
    if prefs is not None and projects is not None:
        total_people = len(prefs)
        total_project = len(projects)
        default_num = (total_people//total_project) - 1
        return default_num
    else:
        raise(InvalidData)