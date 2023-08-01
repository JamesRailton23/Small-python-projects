# calculator
import random
import math


def calculator(value1, operator, value2):
    try:
        match operator:
            case "+":
                return value1 + value2
            case "-":
                return value1 - value2
            case "*":
                return value1 * value2
            case "/":
                return value1 / value2
            case "//":
                return value1 // value2
            case "%":
                return value1 % value2
            case "sqrt":
                return math.sqrt(value1 + value2)
            case "pow":
                return math.pow(value1, value2)
            case "random number":
                return random.randint(value1, value2)
            case _:
                print("error occurred")
    except Exception as e:
        print(e)
    except ZeroDivisionError:
        print("you cannot divide by zero")

value1 = int(input("Insert value 1: "))
operator = input("insert mathematical operation: ")
value2 = int(input("Insert value 2: "))
print("{0}{1}{2}={3}".format(value1, operator, value2, calculator(value1=value1, operator=operator, value2=value2)))
