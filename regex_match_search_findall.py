import re
pattern=r"spam"

if re.match(pattern,"eggsspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern,"eggsspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern,"eggsspamsausagespam"))
