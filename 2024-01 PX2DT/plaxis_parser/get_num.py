from typing import Optional


def get_id(string: str) -> Optional[str]:
    """
    Parses a string and returns a new string composed of the digits in the original string, incremented by 1.

    Args:
    string (str): The input string to parse.

    Returns:
    Optional[str]: A string representation of the incremented number, or None if no digits are found.
    """
    # Extract digits from the string
    ID = "".join([i for i in string if i.isdigit()])

    # Check if the string contains digits
    if ID:
        # Return the incremented value as a string
        return str(int(ID) + 1)
    else:
        # Return None if no ID are found
        return None


def get_mat(lista_gm: list, id_elementa_gm: int) -> int:
    """
    Determines which material is defined for the element.

    Args:
    lista_gm (list): The list containing material information.
    id_elementa_gm (int): The ID of the element to find the material for.

    Returns:
    int: The index of the material, or -1 if not found.
    """
    for index, material_row in enumerate(lista_gm):
        if id_elementa_gm in material_row:
            return index + 1

    return -1
