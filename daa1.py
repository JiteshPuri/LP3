def fibonacci(n):
    if n <= 1:
        return n, 1
    else:
        fib_1, steps_1 = fibonacci(n-1)
        fib_2, steps_2 = fibonacci(n-2)
        return fib_1 + fib_2, steps_1 + steps_2 + 1

def main():
    n = int(input("Enter the Fibonacci number you want to calculate: "))

    if n < 0:
        print("Please enter a non-negative integer.")
        return

    result, steps = fibonacci(n)

    print(f"The {n}-th Fibonacci number is: {result}")
    print(f"Total steps taken: {steps}")

if __name__ == "__main__":
    main()