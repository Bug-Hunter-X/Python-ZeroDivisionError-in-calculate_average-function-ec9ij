def calculate_average(numbers):
    if not numbers: 
        return 0  # Handle empty list to avoid ZeroDivisionError
    return sum(numbers) / len(numbers)

#The improved function explicitly checks if the input list is empty. If it is, the function returns 0, preventing the `ZeroDivisionError`. Otherwise, it proceeds with the calculation as before.