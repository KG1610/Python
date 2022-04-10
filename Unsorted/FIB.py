

def fib(sequence, return_option):

    counter = 0
    fib_numbers = []

    while counter < sequence:
        if len(fib_numbers) < 2:
            fib_numbers.append(counter)
        else:
            n1 = counter - 1
            n2 = counter - 2
            fib_numbers.append(fib_numbers[n1] + fib_numbers[n2])

        counter += 1

    if return_option == 1:
        return (f'The Fibbonaci Sequence is: {fib_numbers}')
    elif return_option == 2:
        return (f'The Fibbonaci Number for the {sequence} iteration is: {fib_numbers[-1]}')



fib(5, 2)
