################################################################################
################################################################################
## Template file for problem 1. You have to fill in the function findNumbers  ##
## defined below. The function takes in an input number and return the list   ##
## of numbers that satisfy the problem statement. Please ensure you return a  ##
## list as the submission will be auto evaluated. We have provided a little   ##
## helper to ensure that the return value is correct.                         ##
##                                                                            ##
## You can run this template file to see the output of your function.         ##
## First replace the TEST_NUMBER with correct number.                         ##
## Then simply run: `python problem1_template.py`                             ##
## You should see the output printed once your program runs.                  ##
##                                                                            ##
## DO NOT CHANGE THE NAME OF THE FUNCTION BELOW. ONLY FILL IN THE LOGIC.      ##
## DONT FORGET TO RETURN THE VALUES AS A LIST                                 ##
## IF YOU MAKE ANY IMPORTS PUT THEM IN THE BODY OF THE FUNCTION               ##
##                                                                            ##
## You are free to write additional helper functions but ensure they are all  ##
## in this file else your submission wont work.                               ##
##                                                                            ##
## Good Luck!                                                                 ##
################################################################################
################################################################################

TEST_NUMBER = 0

def findNumbers(inputNumber):
    ##################################
    ##          FILL ME IN          ##
    ##################################

    prime = []
    A_and_B = []

    #These are my following conclusion for the conversation between Sarah(S), Lisa(L) and Donna(D).
    #Statement 1: L has product which is not unique. May have two or more possibilities. Hence she is confused.
    #Statement 2: S knows that the product is not unique. And also can be a perfect square in the given range. But the product is not 2B, where A=B, but can has value equal to 2B.
    #Statement 3: L is confirmed of the two numbers A and B. This implies the largest number is a square of prime mumber. And the smallest number is one
    #Statement 4: S knows that one of the number is 1. Substracting 1 from the sum gives her the perfect square of a prime number.
    #Statement 5: D is unsure of the numbers. But she has a clue, one of the number is a square of a prime number. And is unsure of the second number. Thus giving her a range of A and B values
    #Statement 6: L knows D is thinking of B to be correct. This implies to L that D has a range of A.
    #Statement 7: D now understands that the smallest number A is 1 and B is the sum of the value she knows with one
 
    for i in range(2,inputNumber):  #List of prime number between 1 to 1000
        c = 0
        for j in range(2,i+1):
            if(i%j == 0):
                c = c + 1
        if(c == 1):
            prime.append(i)
    prime_max = max(prime)
    A_and_B = [1,prime_max] #As a<b. The list is in the form [a,b]
    return A_and_B

def ensureNumbers(returnList):
    for num in returnList:
        if type(num) is int:
            continue
        else:
            print(num, ' is not an integer.')
            raise TypeError('The return value is not a list of integers')
    return returnList

def ensureListOfNumbers(returnList):
    if type(returnList) is list:
        return ensureNumbers(returnList)
    else:
        print('Return value is not a list. Please ensure you return a list.')
        raise TypeError('The return value is not a list')



if __name__ == "__main__":
    TEST_NUMBER = 1000
    print(ensureListOfNumbers(findNumbers(TEST_NUMBER)))
