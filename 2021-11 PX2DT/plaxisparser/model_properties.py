import json
import re
import os

# todo dodati funkcionalnost da se azurira neki od propertija pojedinacno ako se ponovo pojavljuje komanda _setproperties
# todo dodati funkcionalnost da cita fajl i vrsi iteraciju po linijama, ne da koristi string iz koda


def parse_setproperties(command_string):
    # Regular expression to match quoted strings and numbers
    token_pattern = re.compile(r"\"[^\"]+\"|\S+")
    tokens = token_pattern.findall(command_string)

    # Check if the command starts with '_setproperties'
    if tokens and tokens[0] == "_setproperties":
        # Parse the properties into a dictionary
        properties = {}
        for i in range(1, len(tokens), 2):
            key = tokens[i].replace('"', "")
            value = tokens[i + 1].replace('"', "")

            # Convert numeric values
            if value.replace(".", "", 1).isdigit():
                value = float(value) if "." in value else int(value)
            properties[key] = value

        return properties
    else:
        return None


file_name = "output/parsed_properties.json"
dirname = os.path.dirname(__file__)
parent_dir = os.path.dirname(dirname)
json_file_path = os.path.join(parent_dir, file_name)

command_string = '_setproperties "Title" "Primer 5" "Company" "Jaroslav Cerni Water Institute" "Comments" "" "UnitForce" "kN" "UnitLength" "m" "UnitTime" "day" "WaterWeight" 10 "ReferenceTemperature" 293.15 "LiquidSpecificHeatCapacity" 4181.3 "LiquidThermalConductivity" 0.0006 "LiquidLatentHeat" 334000 "LiquidThermalExpansion" 0.00021 "LiquidTemperature" 293.15 "IceSpecificHeatCapacity" 2108 "IceThermalConductivity" 0.00222 "IceThermalExpansion" 5E-5 "VapourSpecificHeatCapacity" 1930 "VapourThermalConductivity" 2.5E-5 "VapourSpecificGasConstant" 461.5 "UseTemperatureDepWaterPropsTable" False "ModelType" "Full" "ElementType" "10-Noded"'
parsed_properties = parse_setproperties(command_string)

# Writing the parsed data to a JSON file
with open(json_file_path, "w") as json_file:
    json.dump(parsed_properties, json_file, indent=4)
