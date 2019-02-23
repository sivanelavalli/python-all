import pickle
from item import *

print("For serialization code")
pickle_out=open("F:\Django11\programs\siva1.txt","wb")
pickle.dump(pobj,pickle_out)
pickle_out.close()

print("for Deserialization code")
pickle_in=open("F:\Django11\programs\siva1.txt","rb")
store=pickle.load(pickle_in)
print(store)