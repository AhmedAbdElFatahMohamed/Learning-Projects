from calc_art import logo
import os

def add (n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2

operations={
"+":add,
"-":substract,
"*":multiply,
"/":divide
}

def calculator():
    print(logo)
    again=True
    num1=float(input("What's the first number?: "))
    while again:
        for operation in operations:
            print(operation)
        symbol=input("Pick an operation for the line above ")
        num2=float(input("What's the next number?: "))
        function=operations[symbol]
        answer=function(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        another=input(f"type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'e'to exit: ").lower()
        if another =='y':
            num1=answer
            os.system('clear')
        elif another=='n' :
            again=False
            os.system('clear')
            calculator()
        else:
            again=False

calculator()
