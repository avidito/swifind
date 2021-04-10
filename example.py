from swifind import Swimmer

# Initiation
plan = 'example.swipl'
sw = Catfish(plan)

# Swimming
sw.swim()

# Unpacking
result = sw.unpack()
print(f"\nResult:\n{json.dumps(result, indent=4)}")
