from picosdk.discover import find_all_units, find_unit

scope = find_unit()
print(scope.info)
scope.close()
