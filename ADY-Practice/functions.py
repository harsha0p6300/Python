#1. Write a function that accepts a list of numbers and returns the largest number. 
def large(list):
    my_list=max(list)
    print(my_list)

large([2,4,5,8])

# 2. Write a function that takes a sentence and returns the number of vowels in it. 
def vowel(word):
    count=0
    vowels="aeiouAEIOU"
    for char in word:
        if char in vowels:
            count+=1
    return count
user=str(input("Enter some word: "))
print(vowel(user))

#3. Write a function with two arguments: principal and rate, and return simple interest.

def interest(p, r, t):
    s_i = (p*t*r/100)
    return s_i

principal = int(input("enter the Amount: "))
inter = int(input("enter the rate of interest: "))
time = int(input("enter the duration: "))

print(f"The interest that you get for the amount{principal} and interest of {inter}% on the {time} years is {interest(principal, inter, time)} rupees")

#4 Write a function that accepts student marks and returns grade (A/B/C/Fail). 

def student(marks):
    if marks>90:
        return "You Got the 'A' grade"
    elif marks>75:
        return "You Got the 'B' grade"
    elif marks>=35:
        return "You Got the 'C' grade"
    else:
        return "Sorry you Failed...!"
print(student(16))

# 5/Write a function that takes a number and returns whether it is prime or not.

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(prime(7))
   