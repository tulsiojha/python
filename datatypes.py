

#str

array = "homogenous collection of data type"

text = "hello world"

print(text)
print(type(text))


#complex

x = 1 + 2j

print(x)


#list

coll = [1, 2, 3, 4]

print(coll)


#tuple
coll = (1, 2, 3, 4)

print(coll)


#range

z = range(10)

for item in z:
    print(item)


z = range(5, 10)

for item in z:
    print(item)


print('range step')
z = range(5, 20, 3)

for item in z:
    print(item)



#dict

#collection of keys and values
dictionary = {
    
    "array":"homogenous collection of data type", 
    "age":0,
    "class":123,
    "yes/no":True,
    "abc":[1,2,3,4]
}

print(dictionary['abc'][2])


#bool

yes = True
no = True

print(yes == no)


#set

test = {1,2,3,4}

print(type(test))


#none

testnone = None
testtrue = 1
print(None == testtrue)






