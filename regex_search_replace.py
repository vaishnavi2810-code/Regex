import re
str="My name is Vishwaa. Hi Vishwaa"
pattern=r"Vishwaa"
newstr=re.sub(pattern,"Vaishnavi",str)
print(newstr)
