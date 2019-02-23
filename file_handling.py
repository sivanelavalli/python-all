import re
Wanted=20
with open('config_one.txt') as searchfile:
 for line in searchfile:
  left,sep,right=line.partition('group')
  if sep:
   print(right[:Wanted])
print("---------------------------------------")
X = len("-1 Super awesome figure")
regex = re.compile("group.{%d}" % X)
for line in open("config_one.txt"):
  for m in regex.findall(line):
    print(m)
print("-----------------------------------")
with open('config_one.txt') as searchfile:
    for line in searchfile:
        for line2 in re.finditer('group',line):
            new_line1=line.strip('group.')
            print(line2)
