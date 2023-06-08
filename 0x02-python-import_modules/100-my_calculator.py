#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length != 3:
        print(" Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    sign = sys.argv[2]
    if sign != '+' and sign != '-' and sign != '*' and sign != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sign == "+":
        value = add(a, b)
    if sign == "-":
        value = sub(a, b)
    if sign == "*":
        value = mul(a, b)
    if sign == "/":
        value = div(a, b)

    print(f"{a} {sign} {b} = {value}")
