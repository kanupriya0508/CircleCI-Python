def fibonacci(n):
    """Generate the Fibonacci sequence up to the nth term."""
    fib_sequence = [0, 1]  # Initialize the sequence with the first two terms

    # Generate subsequent terms of the sequence
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence

def main():
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    # Check if the input is valid
    if n <= 0:
        print("Please enter a positive integer.")
        return

    fib_sequence = fibonacci(n)  # Generate the Fibonacci sequence

    # Print the Fibonacci sequence
    print("Fibonacci sequence up to the", n, "term:")
    for term in fib_sequence:
        print(term, end=" ")

if __name__ == "__main__":
    main()
