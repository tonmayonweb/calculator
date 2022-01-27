###########################
from art import logo
print(logo)
from replit import clear
#add
def add(n1,n2):
  return n1+n2

#subtract
def subtract(n1,n2):
  if n1>n2:
    return n1-n2
  elif n2>n1:
    return n2-n1

#multiply
def multiply(n1,n2):
  return n1*n2


#devide
def devide(n1,n2):
  return n1/n2

oparation ={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":devide
}

def calculator():
  num1 = float(input("What is your first number "))
  oparation_continue = True
  while oparation_continue:
    
    for symboll in oparation:
      print(symboll)

    oparation_symboll = input("Pick an oparation from the above : ")

    num2 = float(input("What is your second number "))

    calculation_function = oparation[oparation_symboll]

    value = calculation_function(num1,num2)
    print(f"{num1} {oparation_symboll} {num2} = {value}")

    oparation_continue = input(f"Do you want to continiue with the answer {value}\n type 'y' to continue and type\n 'n' to calculate with a new number\n")
    if oparation_continue=="y":
      num1=value
      clear()
    else:
      oparation_continue = False
      calculator()
      clear()

calculator()














