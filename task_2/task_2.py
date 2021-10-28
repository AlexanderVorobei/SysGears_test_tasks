#!venv/bin/python
import json
from sorter import include, exclude, sort_by


def get_data(file_path):
    try:
        with open(file=file_path, mode="r") as f:
            try:
                input_data = json.load(f)
                if not input_data["data"] or not input_data["condition"]:
                    raise KeyError
                return input_data
            except json.decoder.JSONDecodeError as e:
                raise e
    except FileNotFoundError as e:
        raise e


def sorter(data: dict):
    result_data = []
    for key, value in data["condition"].items():
        intermediate_data = include.sort(data=data["data"], condition=value) \
            if key == "include" else data["data"]
        intermediate_data = exclude.sort(data=intermediate_data, condition=value) \
            if key == "exclude" else intermediate_data
        result_data = sort_by.sort(data=intermediate_data, condition=value) \
            if key == "sort_by" else intermediate_data
    return result_data


def set_result(file_path, data: list):
    with open(file=file_path, mode="w") as f:
        try:
            f.write(json.dumps({"result": data}))
        except json.decoder.JSONDecodeError as e:
            raise e


if __name__ == "__main__":
    data_files = {
        "data": "task_2/input.json",
        "result": "task_2/output.json"
    }
    set_result(file_path=data_files["result"], data=sorter(data=get_data(data_files["data"])))
