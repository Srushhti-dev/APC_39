#2.	Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
      
    else:
        return "Odd"
       

n = int(input("Enter number: "))
print(check_even_odd(n))
