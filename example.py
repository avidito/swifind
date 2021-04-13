from swifind import Swimmer

# Initiation
plan = 'example.swipl'
sw = Catfish()
sw.prepare(plan)

# Swimming
sw.swim()

# Unpacking
result = sw.unpack()
print(f"\nResult:\n{json.dumps(result, indent=4)}")
