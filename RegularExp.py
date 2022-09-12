import re
pattern=re.compile("ab")
matcher=pattern.finditer("abaabaa")

for match in matcher:
    print(match.start(),"...",match.end(),match.group())
print()

import re
pattern=re.compile("the")
matcher=pattern.finditer("This is the python class")

for match in matcher:
    print(match.start(),"...",match.end(),match.group())

    print()

import re
matcher=re.finditer("[azc]","a7b@9zc")
for match in matcher:
    print(match.start(),'.....',match.group())

print()
