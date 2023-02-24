import re

p = re.compile("^python\s\w+", re.M)

data = """python one
life is too short
python two
you need python
python three"""

m = p.findall(data)

print(m)
