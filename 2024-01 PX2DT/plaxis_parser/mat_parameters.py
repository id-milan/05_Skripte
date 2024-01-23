import re
import os
import json

# todo proveriti da li materijalne karakteristike mogu da se azuriraju u fajlu ili se setuju samo jednom


def parse_mohr_coulomb(tokens):
    """Parse Mohr-Coulomb material parameters."""
    params = [
        "Identification",
        "SoilModel",
        "Colour",
        "gammaUnsat",
        "gammaSat",
        "ERef",
        "nu",
        "cRef",
        "phi",
    ]

    # Initialize an empty dictionary to store parameters and their values
    parsed_params = {}

    # Iterate over each parameter
    for param in params:
        # Check if the parameter is in the tokens list (strip quotes for comparison)
        stripped_tokens = [token.replace('"', "") for token in tokens]
        if param in stripped_tokens:
            # Find the index of the parameter
            param_index = stripped_tokens.index(param)
            # Get the value following the parameter, remove quotes, and store in the dictionary
            param_value = tokens[param_index + 1].replace('"', "")
            parsed_params[param] = param_value

    return parsed_params


def parse_linear_elastic(tokens):
    """Parse Linear Elastic material parameters."""
    params = [
        "Identification",
        "SoilModel",
        "DrainageType",
        "Colour",
        "nu",
        "ERef",
        "gammaUnsat",
    ]

    # Initialize an empty dictionary to store parameters and their values
    parsed_params = {}

    # Iterate over each expected parameter
    for param in params:
        # Check if the parameter is in the tokens list (strip quotes for comparison)
        stripped_tokens = [token.replace('"', "") for token in tokens]
        if param in stripped_tokens:
            # Find the index of the parameter
            param_index = stripped_tokens.index(param)
            # Get the value following the parameter, remove quotes, and store in the dictionary
            param_value = tokens[param_index + 1].replace('"', "")
            parsed_params[param] = param_value

    return parsed_params


def parse_elastic(tokens):
    """Parse Elastic material parameters."""
    params = [
        "Identification",
        "MaterialType",
        "Colour",
        "Gamma",
        "Isotropic",
        "E1",
        "D3d",
        "G12",
    ]

    # Initialize an empty dictionary to store parameters and their values
    parsed_params = {}

    # Iterate over each parameter
    for param in params:
        # Check if the parameter is in the tokens list (strip quotes for comparison)
        stripped_tokens = [token.replace('"', "") for token in tokens]
        if param in stripped_tokens:
            # Find the index of the parameter
            param_index = stripped_tokens.index(param)
            # Get the value following the parameter, remove quotes, and store in the dictionary
            param_value = tokens[param_index + 1].replace('"', "")
            parsed_params[param] = param_value

    return parsed_params


def parse_material_parameters(material_definitions):
    """Parse material definitions from a script."""
    # Initialize a list to store parsed materials
    parsed_materials = []

    # Use regular expression to match quoted strings and words
    token_pattern = re.compile(r"\"[^\"]+\"|\S+")

    # Iterate through each line in the definitions
    for line in material_definitions.strip().split("\n"):
        # Check if the line is a material definition
        if line.startswith("_soilmat") or line.startswith("_platemat"):
            # Extract tokens using the regular expression
            tokens = token_pattern.findall(line)

            # Determine the material model
            model = next(
                (
                    tokens[i + 1].replace('"', "")
                    for i, token in enumerate(tokens)
                    if token.replace('"', "") in ["SoilModel", "MaterialType"]
                ),
                None,
            )

            # Delegate to the appropriate parsing function based on the material model
            if model == "Mohr-Coulomb":
                material_params = parse_mohr_coulomb(tokens)
            elif model == "Linear Elastic":
                material_params = parse_linear_elastic(tokens)
            elif model == "Elastic":
                material_params = parse_elastic(tokens)
            else:
                continue  # Skip if the material model is not recognized

            # Add the extracted material parameters to the list
            parsed_materials.append(material_params)

    return parsed_materials


# Read from file
file_name = "data/primer_5.p3d"
dirname = os.path.dirname(__file__)
parent_dir = os.path.dirname(dirname)
file_path = os.path.join(parent_dir, file_name)


with open(file_path, "r") as file:
    script_content = file.read()

# Parse the material definitions
parsed_materials = parse_material_parameters(script_content)

for material in parsed_materials:
    print(material["Identification"])


def write_material_properties_to_json(parsed_materials, output_file):
    """
    Write parsed material properties to a JSON file.

    :param parsed_materials: List of dictionaries containing parsed material properties.
    :param output_file: Path to the output JSON file.
    """
    with open(output_file, "w") as file:
        json.dump(parsed_materials, file, indent=4)


# Define the output file path
output_json = "output/material_properties.json"
parent_dir = os.path.dirname(dirname)
output_json_file_path = os.path.join(parent_dir, output_json)

# Write the parsed material properties to the JSON file
write_material_properties_to_json(parsed_materials, output_json_file_path)
