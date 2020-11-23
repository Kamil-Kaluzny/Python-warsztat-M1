#training file

mylist=[]
mytuple=()
mydict={}
# myset = {} deklaracja slownika

str1 = "str1"
str2 = "str2"
str3 = "str3"

int1 = "11"
int2 = "22"
int3 = "33"


mylist = [str1,str2,str3,int1,int2,int3]
print(mylist)
print("list > tuple: ", tuple(mylist))
print("list > set: ", set(mylist))

print()
print(mylist[2])
print(mylist[2:4])

print()
for el in mylist:
    print(el)

print()
for i in range(len(mylist)):
    print(i)

for i, el in enumerate(mylist):
    print(i, el)

mytuple = (str1,str2,str3,int1,int2,int3)
print("\n",mytuple)
print("tuple > list: ", list(mytuple))
print("tuple > set: ", set(mytuple))

print()
print(mytuple[2])
print(mytuple[2:4])

print()
for el in mytuple:
    print(el)

print()
for i in range(len(mytuple)):
    print(i)


mydict = {int1:str1,int2:str2,int3:str3}
print("\n",mydict)
print("dict > list: ", list(mydict))
print("dict > tuple: ", tuple(mydict))
print("dict > set: ", set(mydict))

print()
print(mydict["11"])

print()
for key in mydict:
    print(key)

print()
for key, value in mydict.items():
    print(key)
    print(value)

print()
for key in mydict:
    print(key) #drukowanie kluczy
    for value in mydict[key]:
        print(value) # drukowanie wartosci


print()
for i in range(len(mydict)):
    print(i)



myset = {str1,str2,str3,int1,int2,int3}
print("\n",myset)

'''
while True:
    if input() == "q":
        break
'''