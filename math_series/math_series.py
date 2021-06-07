def fibonacci (n):
    if n <=1 :
       return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)




def lucas (n):
      if n == 0  : return 2
      elif n==1 : return 1 
      elif n>1 :
          return lucas(n-1)+lucas(n-2)

def anotherSeries(x,y,z):
    if x==0 : return y
    elif x== 1 : return z 
    else :
        return anotherSeries(x-1 ,y,z)+ anotherSeries(x-2,y,z)

def sum_series (a , b=0 , c=1):
    if b ==0 and  c== 1:
       return fibonacci(a)
        
    elif (b == 2 and c ==1 ):
       return lucas(a)
    else: 
        return anotherSeries(a,b,c)       


