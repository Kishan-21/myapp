
Original file is located at
    https://colab.research.google.com/drive/1leNUHYR5Ccxe0Fyr6r_fuVEackTD8k5P
"""

with open("Software1.txt", "a") as f:
  for i in range(1,101):
    if (i%3 ==0 and i%5 == 0):
      print("fizzbuzz", file=f)
    elif (i%3 == 0):
      print("fizz", file=f)
    elif (i%5 == 0):
      print("buzz", file=f)
    else:
      print(i,file=f)

