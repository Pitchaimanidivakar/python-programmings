def power(a,exp):
    if(exp==1):
       return(a)
    if(exp!=1):
      return(a*power(a,exp-1))
a=int(input("Enter a: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(a,exp))
