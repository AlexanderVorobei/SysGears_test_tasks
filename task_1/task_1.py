#!venv/bin/python
import json
import convertor


def get_data(file_path):
    try:
        with open(file=file_path, mode="r") as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError as e:
                raise e
    except FileNotFoundError as e:
        raise e


def get_units(file_path):
    with open(file=file_path, mode="r") as f:
        try:
            return json.load(f)["units"]
        except json.decoder.JSONDecodeError as e:
            raise e


def set_units(file_path, units: dict):
    with open(file=file_path, mode="w") as f:
        try:
            f.write(json.dumps({"units": units}))
        except json.decoder.JSONDecodeError as e:
            raise e


def set_result(file_path, data: dict):
    with open(file=file_path, mode="w") as f:
        try:
            f.write(json.dumps(data))
        except json.decoder.JSONDecodeError as e:
            raise e


if __name__ == "__main__":
    data_files = {
        "data": "task_1/input.json",
        "units": "task_1/units.json",
        "result": "task_1/output.json"
    }
    convertor = convertor.Convert(get_units(file_path=data_files["units"]))
    data = get_data(file_path=data_files["data"])

    try:
        value = data["distance"]["value"]
        unit = data["distance"]["unit"]
        convert_to = data["convert_to"]
    except KeyError as e:
        raise e
    else:
        set_result(file_path=data_files["result"],
                   data=convertor.convert(value=value, unit=unit, convert_to=convert_to))

    if "units" in data:
        try:
            new_unit = data["units"]["distance"]
        except KeyError as e:
            raise e
        convertor.update_units(unit=new_unit)
        set_units(file_path=data_files["units"], units=convertor.units)
