import re
'''pattern=r"^gr.y$"

if re.match(pattern,"grey"):
    print("Match 1")

if re.match(pattern,"greys"):
    print("Match 2")'''

'''pattern=r"[aeiou]"
if re.search(pattern,"vaishu"):
    print("Match 1")
if re.search(pattern,"rhythm"):
    print("Match2")'''

'''pattern=r"[abc][def]"
if re.search(pattern,"cdhello"):
    print("Match 1")
if re.search(pattern,"abdvillers"):
    print("Match 2")'''

'''pattern=r"[A-Z][a-z][0-9]"
if re.search(pattern,"A9x6L"):
    print("Match 1")
if re.match(pattern,"Aw4"):
    print("Match 2")'''

'''pattern=r"[^A-Z]"
if re.search(pattern,"ATHERC"):
    print("Match 1")
if re.search(pattern,"Al2019X"):
    print("Match 2")'''
#string that starts with egg and follow with zero or more spam
'''pattern=r"egg(spam)*"
if re.match(pattern,"egg"):
    print("Match 1")
if re.match(pattern,"eggsspamsausagespam"):
    print("Match 2")
if re.match(pattern,"spam"):
    print("Match 3")'''
#+ means one or more occurances of
'''pattern=r"g+"
if re.match(pattern,"g"):
    print("Match 1")
if re.match(pattern,"ggggggg"):
    print("Match 2")
if re.match(pattern,"eee"):
    print("Match 3")
else:
    print("No match 3")'''

    #? means zero or one repition
'''pattern=r"ice(-)?cream"
if re.match(pattern,"ice-cream"):
    print("Match 1")
if re.match(pattern,"ice--cream"):
    print("Match 2")
if re.match(pattern,"icecream"):
    print("Match 3")'''
#{} repitition between any x and y
'''pattern=r"9{1,3}$"
if re.match(pattern,"9"):
    print("Match 1")
if re.match(pattern,"99"):
    print("Match 2")
if re.match(pattern,"99999"):
    print("Match 3")
else:
    print("No match 3")'''
#groups
'''pattern=r"egg(spam)*"
if re.match(pattern,"egg"):
    print("Match1")
if re.match(pattern,"eggsspamsausagespam"):
    print("Match2")
if re.match(pattern,"spam"):
    print("Match3")
else:
    print("No match 3")'''
#accessing contents of groups
'''pattern=r"a(bc)(de)(f(g)h)i"
match=re.match(pattern,"abcdefghijklmnop")
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group())'''

'''pattern=r"(?P<first>abc)(?:def)(ghi)"
match=re.match(pattern,"abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())'''
# | means or i.e red|blue means either red or blue
'''pattern=r"gr(a|e)y"
if re.match(pattern,"gray"):
    print("Match 1")
if re.match(pattern,"grey"):
    print("Match 2")
if re.match(pattern,"griy"):
    print("Match 3")'''
#special sequences
'''pattern=r"(.+) \1"
if re.match(pattern,"word word"):
    print("Match 1")
if re.match(pattern,"abc def"):
    print("Match 2")
if re.match(pattern,"?! ?!"):
    print("Match 3")'''

'''pattern=r"(\D+\d)"
if re.match(pattern,"HI this is 12345"):
    print("Match 1")
if re.match(pattern,"2345 2345"):
    print("Match 2")
if re.match(pattern,"! $"):
    print("Match 3")'''

'''pattern=r"\b(cat)\b"
if re.search(pattern,"The cat sat"):
    print("Match1")
if re.search(pattern,"WE S>CAT<TERED"):
    print("Match2")
if re.search(pattern,"We scattered"):
    print("Match3")
if re.search(pattern,"We s<cat>tered"):
    print("Match4")'''

pattern= r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str="Please contact jariwalavaishnavi52@gmail.com or hello.this-python@py.com"
matches=re.findall(pattern,str)
if matches:
    for tuple in matches:
        print(tuple[0]+"@"+tuple[1])
