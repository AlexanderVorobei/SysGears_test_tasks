from operator import itemgetter


def sort(data: list, condition: list):
    sorted_data = []
    for cond in condition:
        sorted_data = sorted(data, key=itemgetter(cond))
    return sorted_data

