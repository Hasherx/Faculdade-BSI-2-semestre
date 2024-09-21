def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_sequence(limit):
    sequence = []
    i = 0
    while True:
        fib_number = fibonacci(i)
        if fib_number > limit:
            break
        sequence.append(fib_number)
        i += 1
    return sequence

limit = int(input("Digite um número: "))
sequence = fibonacci_sequence(limit)
print("Sequência de Fibonacci até", limit, ":", sequence)
