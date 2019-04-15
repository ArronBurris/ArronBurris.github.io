#Working with binary files

import pickle, shelve
print("Pickling lists")
"""
variety = ["sweet","hot","dill"]
shape = ["whole","spear","chip"]
brand = ["Claussen","Heinz","Vlassic"]

#wb = write binary
#rb = read binary
#ab = append binary

f = open("pickles1.dat","wb")
pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()

"""
f = open("pickles1.dat","rb")
variety = pickle.load(f)
test2 = pickle.load(f)
test3 = pickle.load(f)
print(variety)
print(test2)
print(test3)
f.close()


print("\shelving")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet","hot","dill"]
s["shape"] = ["whole","spear","chip"]
s["brand"] = ["Claussen","Heinz","Vlassic"]

s.sync()

print("\nGetting data form the shelf")
print("brand -", s["brand"])
s.close()

#asking for specific part of data
print("\nGetting data form the shelf")
print("brand -", s["brand"][0])
s.close()
