#Write your code below this line 👇

#TO 1 take a whole number (n) and determine its factors
#TO DO 2 if that whole number has only 2 factors it is a prime
# factor divides a number exactly 
def factor_checker(n):
  factors = []
  for i in range(1 , n + 1):
   factor = n % i  == 0
   if factor == True:
     factors.append(i)
  return(len(factors))



  # returns factors print(factors)

def prime_checker(number):
  if factor_checker(n) == 2:
    print("It's a prime number.")
  else:
    print("It's a composite number.")



  
# if factor_checker == 2 



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


''''
whole number whose factors are only one and its self, for example 3 the only way we can get 3 by multiplying two numbers is 1 and 3.
'''

