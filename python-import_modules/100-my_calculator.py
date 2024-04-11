#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    args = len(argv) - 1
    operators = ['+',' -', '*', '/']
    res = 0
    if args == 3:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res))
        elif argv[2] == '-':
            res = sub(a,b)
            print("{} - {} = {}".format(a, b, res))
        elif argv[2] == '*':
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res))
        elif argv[2] == '/':
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
