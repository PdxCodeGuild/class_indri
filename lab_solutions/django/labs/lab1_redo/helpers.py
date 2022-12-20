
def unit_converter(input_distance: int | float, input_unit: str):
    units = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0254
    }

    try:
        output = units[input_unit] * input_distance
    except TypeError:
        raise Exception(f"Invalid distance: {input_distance}. Must be float or integer.")
    except KeyError:
        raise Exception(f"Invalid unit: {input_unit}")

    return output
