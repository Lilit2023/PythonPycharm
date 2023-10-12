#num = input("Please enter some number:")

# if num == num[::-1]:
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not palindrome")
num1= input("Please enter some number:")
num2 = input("Please enter some number:")
num3 = input("Please enter some number:")
if num1 < num2 < num3 or num3 < num2 < num1:
    print(f"The middle number is {num2}")
elif num2 < num1 < num3 or num3 < num1 < num2:
    print(f"The middle number is {num1}")
else:
    print(f"The middle number is {num3}")
