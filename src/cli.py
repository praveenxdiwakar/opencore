# cli.py - simple command-line interface

import argparse
from core import greet, calculate_sum, calculate_product

def main():
    parser = argparse.ArgumentParser(description="Open-Core CLI")
    parser.add_argument("--greet", type=str, help="Greet a user")
    parser.add_argument("--sum", nargs=2, type=int, help="Calculate sum of two numbers")
    parser.add_argument("--product", nargs=2, type=int, help="Calculate product of two numbers")
    
    args = parser.parse_args()
    
    if args.greet:
        print(greet(args.greet))
    if args.sum:
        print(f"Sum: {calculate_sum(args.sum[0], args.sum[1])}")
    if args.product:
        print(f"Product: {calculate_product(args.product[0], args.product[1])}")

if __name__ == "__main__":
    main()
