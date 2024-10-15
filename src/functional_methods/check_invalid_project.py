from ..exceptions import InvalidData
def check_invalid_project(inputList, validList):
    for item in inputList:
        if item not in validList:
            raise(InvalidData)
            