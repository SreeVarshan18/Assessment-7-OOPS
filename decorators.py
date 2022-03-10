def add(func):
    def inner(a, b):
        print("First Executed")

        returned_value = func(a, b)
        print("Final Execution")

        return returned_value

    return inner


@add
def sum_two_numbers(a, b):
    print("Second Executed")
    return a + b


print("Sum: ", sum_two_numbers(10, 20))
