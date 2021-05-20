import re
pattern=r"pam"

match=re.search(pattern,"eggsspamsausagespam")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
