#!/usr/bin/env python3

import sys

def fizz_buzz(n):
    """Generates the FizzBuzz sequence up to n."""
    results = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else::
            results = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else::
        print("The argument must be an integer.")
        sys.exit(1)

    results = fizz_buzz(n)

    for result in results:

        print(result)

if __name__ == "__main__":
    main()
all
