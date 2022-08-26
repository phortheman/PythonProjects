"""
This is a very simple quiz program that will take user input and compare it against
the specified answer. It will also normalize the input and produce a percentage score

Author: phortheman
"""
score: int = 0
questionCount: int = 0

import re

def main():
    print( "This is a quick quiz game!" )

    player = input("Enter player name: " )

    question( "What is the name of the hero in The Legend of Zelda", "Link" )
    question( "How many bits are in a byte", "8" )
    question( "What is the capital of the United States?", "Washington DC" )
    question( "How many meters are in a kilometer", "1000" )

    finalScore = score/questionCount

    print( f"{player} scored: {finalScore:.2%}" )

def question( question: str, answer: str ):
    global questionCount
    global score

    questionCount += 1

    print( f"{question}{'?' if not question.endswith( '?' ) else ''}")

    playerAnswer = input( "Answer: " )
    if not playerAnswer.isalnum(): # Only accept alphanumeric values
        playerAnswer = re.sub( r"[^\w\s]", "", playerAnswer)

    if playerAnswer.lower() == answer.lower():
        score += 1

if __name__ == '__main__':
    main()