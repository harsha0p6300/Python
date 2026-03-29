#1. Use lambda to sort a list of tuples based on the second value. 
l=[(1, 5), (3, 2), (2, 8), (4, 1)]
print(sorted(l,key=lambda x:x[1]))


# 2. Write a lambda function to calculate the area of the rectangle. 
x=lambda a,b:a*b
length=int(input("Enter the length: "))
width=int(input("Enter the width: "))
print(f"The Area of the rectangle is {x(length,width)}")

# 3.Use lambda to find the last digit of a number
digit=lambda x:x%10
print(digit(1345))

# 4. Write lambda to check if a string length is greater than 5. 
length=lambda x:len(x)>5
print(length("harsha"))

#5. Use lambda to return a minimum of three numbers.
minimum=lambda a,b,c:min(a,b,c)
print(minimum(10,20,30))

