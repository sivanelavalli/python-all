from django.core.paginator import Paginator
objects=['siva','prasad','ram','srinu','sriniv','asarao']
p=Paginator(objects,3)
a=p.count
b=p.num_pages
print(a)
print(b)
