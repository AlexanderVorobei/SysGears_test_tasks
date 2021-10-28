def sort(data: list, condition: list):
    sorted_data = []
    for cond in condition:
        for item in data:
            for key, value in item.items():
                if key in cond and value in cond.values():
                    sorted_data.append(item)
    return sorted_data
