

print(','.join(['a', 'b', 'c']))
# (', '.join('"' + item + '"' for item in parameters))
# ["'" + item + "'" for item in parameters]
print(', '.join("'" + item + "'" for item in ['a', 'b', 'c']))