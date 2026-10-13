
import json
from jsonschema import validate, ValidationError

# Load input data
with open("input.json", "r", encoding="utf-8") as file:
    input_data = json.load(file)

# Load the schema
with open("inputask_schema.json", "r", encoding="utf-8") as file:
    schema = json.load(file)

# Validate the input
try:
    validate(instance=input_data, schema=schema)
    print("SUCCESS: Input JSON matches the schema!")
except ValidationError as error:
    print("VALIDATION FAILED:", error.message)
