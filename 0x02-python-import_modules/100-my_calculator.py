#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    n1 = int(argv[1])
    op = argv[2]
    n3 = int(argv[3])

    if op is "+":
        print("{:d} + {:d} = {:d}".format(n1, n3, add(n1, n3)))
    elif op is "-":
        print("{:d} - {:d} = {:d}".format(n1, n3, add(n1, n3)))
    elif op is "*":
        print("{:d} * {:d} = {:d}".format(n1, n3, add(n1, n3)))
    elif op is "/":
        print("{:d} / {:d} = {:d}".format(n1, n3, add(n1, n3)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
