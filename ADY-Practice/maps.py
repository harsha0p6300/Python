#sample
# def square(num):
#     return num **2
# numbers=[1,2,3,4,5]
# result=map(square,numbers)
# print(list(result))

# 1. Use map() to convert the list of names into uppercase.
l=["harsha","anudeep","rakesh"]
x=lambda x:x.upper()
print(list(map(x,l)))

# 2.Use map() to calculate the square root of numbers in a list
import math
sq=[4,16,25,625]
print(list(map(lambda s:math.sqrt(s),sq)))

# 3.Given prices list, use map() to add 18% GST to each value. 
price=[250,300,510,881,973]
print(list(map(lambda d:d*1.18,price)))

#4. Use map() to extract the first character from each word in the list.
names=["Apple","Mango", "Banana", "Guava","pineapple"]
print(list(map(lambda x:x[0],names)))

# 5.. Convert list of temperatures from Fahrenheit to Celsius using map() 
fah = [32, 68, 77, 104, 122]
print(list(map(lambda x:(x-32)*5/9,fah)))