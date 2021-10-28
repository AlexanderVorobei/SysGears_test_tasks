class Convert:
    def __init__(self, units: dict):
        self.units = units

    def convert(self, value, unit, convert_to):
        try:
            unit_coefficient = self.units[unit]
            convert_to_coefficient = self.units[convert_to]
        except KeyError as e:
            raise e
        value = value * unit_coefficient / convert_to_coefficient
        return {"unit": convert_to, "value": round(value, 2)}

    def update_units(self, unit: dict):
        for key, value in unit.items():
            if not isinstance(value, (int, float)):
                raise ValueError
            self.units.update(unit)
        return True
