import re


def camel_case_to_snake_case(input_str: str) -> str:
    """
    Convert camel case to snake case
    :param input_str: Camel case input string
    :return: snake case
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()