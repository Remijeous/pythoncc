from art import logo

print(logo)

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

def calculator():

    num1 = float(input("Whats the First number? "))
    for operand, operation in operations.items():
        print(operand)
    should_continue = True

    while should_continue:
        select_operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[select_operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {select_operation} {num2} = {answer}")

        if input(f"Type 'y' to continue caculating with {answer}, or type 'n' to exit.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\033c", end="")
            calculator()

