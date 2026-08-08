
'''
module for math functions
'''

def isPrime (num : int):
    '''
    function to check if a number is prime or not
    input: num (int): the number to check
    output: bool: True if the number is prime, False otherwise
    '''

    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def factorial(num : int):

    '''
    function to calculate the factorial of a number
    input: num (int): the number to calculate the factorial of
    output: int: the factorial of the input number
    '''
    if num == 0:
     return 0
    if num == 1:
     return 1

    return num * factorial(num - 1)