def parse_input_to_list(input_data):
    return [line.strip() for line in input_data.split("\n") if line]


def parse_input_to_matrix(input_data, delimeter: str = None):
    if not delimeter:
        return [[char for char in line] for line in input_data.split("\n") if line]
    else:
        return [line.split(delimeter) for line in input_data.split("\n") if line]
