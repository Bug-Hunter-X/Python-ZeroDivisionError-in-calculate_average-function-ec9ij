def calculate_average(numbers):
    if not numbers: 
        return 0  # Handle empty list to avoid ZeroDivisionError
    return sum(numbers) / len(numbers)

#This function works fine most of the time. However, if the list numbers is empty, the sum of the list will be 0, and division by zero error will occur. This error is difficult to track and debug, since it is only raised in some cases, and not always, depending on the input. 
# A better way to write the function is to handle the case of an empty list explicitly, and return 0 or another appropriate value in that case.