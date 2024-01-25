# Python program to convert two lists into a dictionary.

list2=["Siddhesh","Atharva","Aniket","Vinayak","Mayur"]
list1=[67,60,27,63,29]
print("Keys: "+str(list1))
print("Values: "+str(list2))
dict={}
for key in list1:
    for value in list2:
        dict[key]=value
        list2.remove(value)
        break
print("Resultant Dictionary is: "+str(dict))
