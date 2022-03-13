import utils
import json
from source_to_dsl import *
from dsl_to_target import *

# read input
# input = utils.readInput("csv_to_airtable.txt")
input = utils.readInput("airtable_to_csv.txt")
source = input["source"]
target = input["target"]

file = input["file"]
api_key = input["api_key"]
base_id = input["base_id"]
table_name = input["table_name"]

# from source to DSL

if source == "csv":
    DSL = csv_to_dsl(file)
elif source == 'airtable':
    DSL = airtable_to_dsl(api_key, base_id, table_name)

# print DSL
print(json.dumps(DSL, indent=4))

# from DSL to source
if target == "airtable":
    dsl_to_airtable(DSL, api_key, base_id, table_name)
elif target == "csv":
    dsl_to_csv(DSL, file)

print("END")