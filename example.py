import json
from swifind.catfish import Catfish

# Initiation
path = 'example.swipl'
cf = Catfish(path)

# Swimming
cf.swim()

# Retrieve
result = cf.retrieve()
print(f"\nResult:\n{json.dumps(result, indent=4)}")
