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

    operations: float = []
    testWords: list[str] = []

    testWords = fetchTestWordsFromMIT()
    # testWords = uniqueTestCases()

    for i in testWords:
        tick = time.time()
        bIsPalindrome = checkIfPalindrome( i )
        score += int( bIsPalindrome == True )
        if m_bOutput:
            print( f"'{i}' is {'not ' if not bIsPalindrome else ''}a palindrome")
        toc = time.time()
        operations.append( toc - tick )

    print( f"The average time to peform was {fmean(operations)}")
    print( f"The longest time was {max(operations)}")
    print( f"The shortest time was {min(operations)}")

    print( f"There were {score} palindromes provided out of {len(testWords)} words!" )
    print( f"That means {score/len(testWords):.2%} of the words were palindromes!")


def fetchTestWordsFromMIT() -> list[str]:
    MIT_WORD_LIST = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(MIT_WORD_LIST)
    words = response.content.decode("utf-8").splitlines()
    return words


def uniqueTestCases() -> list[str]:
    words = [ '!!@#$!', '1221', 'A', 'Aa', 'Aaa', 'AAa', 'aaA', 'AAAA', 'aaaa', '', 'ßß', '#2@#2$#@ *' ]
    return words


def checkIfPalindrome( strInput: str ) -> bool:
    # Assuming this is a palindrome at first
    bIsPalindrome: bool = True
    bHasAlNum: bool = False
    
    # Quick check if the string is empty or one character
    if( len(strInput) < 2 ):
        return True

    foldedString = strInput.casefold()
    posL: int = 0
    posR: int = len(strInput) - 1

    while bIsPalindrome:
        if posL > posR:
            break
        if not foldedString[posL].isalnum():
            posL += 1
            continue
        if not foldedString[posR].isalnum():
            posR -= 1
            continue
        bHasAlNum = True
        if foldedString[posR] is not foldedString[posL]:
            bIsPalindrome = False
        else:
            posR -= 1
            posL += 1

    if bHasAlNum:
        return bIsPalindrome
    else: # If there weren't any alpha numberic characters then it isn't a palindrome
        return False

if __name__ == "__main__":
    main()