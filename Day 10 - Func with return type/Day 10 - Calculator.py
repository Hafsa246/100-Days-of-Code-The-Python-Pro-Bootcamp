from art import logo

def add(n1, n2):
  return (n1+n2)

def sub(n1, n2):
  return (n1-n2)

def div(n1, n2):
  return (n1/n2)

def mul(n1, n2):
  return (n1*n2)

operations = {
  "+": add,
  "-": sub,
  "/": div,
  "*": mul
}
def calculator():
  print(logo)
  game = True
  num1 = float(input("What's the first number? "))

  for i in operations:
      print(i)

  while game:
  
    num2 = float(input("What's the next number? "))
  
    symbol = input("Pick an operation from above: ")
  
    function = operations[symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")
    
    repeat = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ")
  
    if repeat == "n":
      game = False
      calculator()
    else:
      num1 = answer

calculator()