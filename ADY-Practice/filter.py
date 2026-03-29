#in python filter() is a build in function used to select only the values that matches a condition that matches a condition from a data
#syntax filter(function,iterable)

#Filter odd numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x: x%2!=0,numbers)
print(list(result))

#syntax filter(function,iterable)

#filter marks greater than 50
num=[24,33,49,56,76,89]
greater=filter(lambda y : y>50,num)
print(greater)


# filter names with more than 4 letters
num = ["Harsha", "anudeep", "Manoj", "Varun", "Harshit","sai"]
result = list(filter(lambda name: len(name) > 4, num))

print(result)

#using normal function with filter()
def even(num):
    return num%2==0
r=[1,2,3,4,5,6,7]
result=list(filter(even,r))
print(result)

# or

def even(num):
    return num % 2 == 0
r = [1, 2, 3, 4, 5, 6, 7]
result = []
for i in r:
    if even(i):
        result.append(i)
print(result)



