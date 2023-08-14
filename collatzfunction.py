#Collatz's hypothesis
c0 = int(input("insert Number: "))

while c0 != 1:
  if c0 % 2 == 0:
    c0 /= 2
  else:
    c0 = 3 * c0 + 1
  print(c0)
