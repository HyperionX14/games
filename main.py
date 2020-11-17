import random
num1 = random.randint(1,15)
for i in range(10):
  int(num1)
  num2 = input(f"guess where the seal is, you have {10-i} guesses\n >>")
  num2 = int(num2)
  if num1 == num2:
    print("you caught the seal")
    break 
  else:
    print("you didnt catch the seal, try again")
print("the seal was", num1)