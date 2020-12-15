from decimal import *
getcontext().prec = 66
π = Decimal(3)
a = Decimal(2)
try:
  while True:
    π += 4 / (a * (a+ Decimal(1) ) * (a+ Decimal(2) ))
    a += Decimal(2)
    π -= 4 / (a * (a+Decimal(1)) * (a+Decimal(2)))
    a += Decimal(2)
    print(a, π, sep="\n")
except KeyboardInterrupt:
  print("Result:", a, π, sep="\n")