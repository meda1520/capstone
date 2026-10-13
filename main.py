
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from jsonschema import validate
from aitask import AITask

load_dotenv()

print(f"Project {os.getenv('Project_name')} started")

try:
    with open("input.json", "r", encoding="utf-8") as file:
        data_dict = json.load(file)

    with open("inputask_schema.json", "r", encoding="utf-8") as file:
        schema_dict = json.load(file)

    validate(instance=data_dict, schema=schema_dict)
    print("json validation completed")

    task = AITask(
        data_dict["user"],
        prompt=data_dict["prompt"],
        tasktype=data_dict["task_type"]
    )

    print(task)

    response = task.process()

    open_json = json.dumps(response, indent=4)

    output_object = Path("data")
    output_object.mkdir(parents=True, exist_ok=True)

    output_file = output_object / "output.json"
    output_file.write_text(open_json, encoding="utf-8")

    print(f"{os.getenv('Project_name')} completed")

except FileNotFoundError:
    print("Required file is not available")

except json.JSONDecodeError:
    print("Invalid JSON error")

except Exception as e:
    print(f"Something went wrong: {e}")
