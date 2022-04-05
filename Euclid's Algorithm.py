#Isiah Williams
#Mr. Burns
#Coding for All
#Euclids Algoritm for find the GCF of two positive integers

a = int(input("Please enter the first number"))
b = int(input("Please enter the second number"))

while a != b:
  if b > a:
    b -= a
  else:
    a -= b
print("The GCF is: " + str(a))
