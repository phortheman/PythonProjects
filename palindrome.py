"""
Simple program that will see if an input string is a palindrome
It will ignore special characters
It will be case insensitive

author: phortheman
"""

import requests
import time
from statistics import fmean

m_bOutput: bool = False

def main():
    score: int = 0

    wordsInput = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(wordsInput)
    WORDS = response.content.decode("utf-8").splitlines()

    operations: float = []

    for i in WORDS:
        tick = time.time()
        score += checkIfPalindrome( i )
        toc = time.time()
        operations.append( toc - tick )

    print( f"The average time to peform was {fmean(operations)}")
    print( f"The longest time was {max(operations)}")
    print( f"The shortest time was {min(operations)}")

    print( f"There were {score} palindromes provided out of {len(WORDS)} words!" )
    print( f"That means {score/len(WORDS):.2%} of the words were palindromes!")


def checkIfPalindrome( strInput: str ) -> int:
    # Assuming this is a palindrome at first
    bIsPalindrome: bool = True
    foldedString = strInput.casefold()
    count = 0
    posL: int = 0
    posR: int = len(strInput) - 1

    while bIsPalindrome:
        if not foldedString[posL].isalnum():
            posL += 1
            continue
        if not foldedString[posR].isalnum():
            posR -= 1
            continue
        if foldedString[posR] is not foldedString[posL]:
            bIsPalindrome = False
        else:
            posR -= 1
            posL += 1
        
        if posL > posR:
            count = 1
            break
    
    if m_bOutput:
        print( f"'{strInput}' is {'not ' if not bIsPalindrome else ''}a palindrome")

    return count

if __name__ == "__main__":
    main()