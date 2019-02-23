from threading import Thread,current_thread
def fun1():
    elements1=['aba','abb','abbbbbba','sd']
    for el in elements1:
     k=len(el)
     if(k>2):
        print(el)
def fun2():
    elements2 = ['aba', 'abb', 'abbbbbba','ss']
    for el1 in elements2:
     if el1[0]==el1[len(el1)-1]:
       print(el1)
t1=Thread(target=fun1)
t2=Thread(target=fun2)
print(current_thread().getName())
t1.start()
t2.start()