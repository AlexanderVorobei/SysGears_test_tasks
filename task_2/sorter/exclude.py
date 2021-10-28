def sort(data: list, condition: list):
    sorted_data = data
    for cond in condition:
        for item in sorted_data:
            for key, value in item.items():
                if key in cond and value in cond.values():
                    sorted_data.remove(item)
    return sorted_data
