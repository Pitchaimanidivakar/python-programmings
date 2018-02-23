a=int(input("Enter number:"))
counts=0
while(a>0):
    counts=counts+1
    a=a//10
print("The number of digits in the number are:",counts)
