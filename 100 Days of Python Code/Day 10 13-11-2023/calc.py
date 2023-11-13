














def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


num1 = int(input("Whats the First number? "))
for operand, operation in operations.items():
    print(operand)
select_operation = input("Select symbol of operation you want to execute: ")
num2 = int(input("What's the Second number? "))
calculation_function = operations[select_operation]
answer = calculation_function(num1, num2)

print(f"{num1} {select_operation} {num2} = {answer}")