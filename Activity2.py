def cube(number):
    return number**3
num=int(input("Enter any number:"))
res=cube(num)

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
    
print(by_three(num))