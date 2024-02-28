def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

# Test the add_numbers function
if __name__ == "__main__":
    # Test case 1
    result1 = add_numbers(5, 3)
    print("Result of adding 5 and 3:", result1)
    
    # Test case 2
    result2 = add_numbers(-10, 20)
    print("Result of adding -10 and 20:", result2)
    
    # Test case 3
    result3 = add_numbers(7, -2)
    print("Result of adding 7 and -2:", result3)
