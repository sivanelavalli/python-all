from django.shortcuts import render
from functools import *
def studentdetails(request):
    d1 = {
        101:{"name":"A","class":10,"marks":[65,95,85,50,45,99]},
        102:{"name":"B","class":10,"marks":[55,85,45,90,46,90]},
        103:{"name":"C","class":10,"marks":[15,75,45,80,56,80]},
        104:{"name":"D","class":10,"marks":[85,65,55,70,66,70]},
        105:{"name":"E","class":10,"marks":[65,55,65,60,76,60]}}
    for x,y in d1.items():
          res=d1[x]
          res2=res['marks']
          res3=reduce(lambda fs,sd:fs+sd,res2)

          res = d1[102]
          res2 = res['marks']
          res4 = reduce(lambda fs, sd: fs + sd, res2)

          res = d1[103]
          res2 = res['marks']
          res5 = reduce(lambda fs, sd: fs + sd, res2)

          res = d1[104]
          res2 = res['marks']
          res6 = reduce(lambda fs, sd: fs + sd, res2)

          res = d1[105]
          res2 = res['marks']
          res7 = reduce(lambda fs, sd: fs + sd, res2)

          d1 = {
               101:{"name":"A","class":10,"marks":[65,95,85,50,45,99],"total":res3},
               102:{"name":"B","class":10,"marks":[55,85,45,90,46,90],"total":res4},
               103:{"name":"C","class":10,"marks":[15,75,45,80,56,80],"total":res5},
               104:{"name":"D","class":10,"marks":[85,65,55,70,66,70],"total":res6},
               105:{"name":"E","class":10,"marks":[65,55,65,60,76,60],"total":res7},
               }
          return render(request, "index.html", {"data": d1})

