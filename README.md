# A collection of very simple Python script to experiment with the language
## Quiz
Script that holds a function that takes a question argument and a answer argument. The question gets a question mark put in if it doesn't have one. The answer from the user gets normalized as a lowercase but also strips out special characters. The test is "Washington D.C." so that both that or "Washington DC" are accepted answers

If the answer is correct then they score gets incremented. At the end the total percentage is provided to the user on how many they got correct.

This was written to play around with the re module

## Rock, Paper, Scissors
Yup, regular good ol' rock, paper, scissors.

This was written to play around with enums in Python. I forced myself to use enums instead of just basic strings to see how to implement then in Python

## Palindrome
This checks to see if a string is a palindrome. It is geared to be as fast as possible and it will skip over non alnum characters. 

I didn't feel like writting out thousands of words to stress test so what I did instead is fetch the [MIT 10000 words list](https://www.mit.edu/~ecprice/wordlist.10000) and loop through those. I came up with very specifc unique cases I wanted to hit but for the performance testing I wanted thousands of words.

I opted for using casefold instead of lower or doing some math around the ord() value of the character because it allows non-ascii characters to be lowercaseable (?). This is tested by the german character 'ß' turning into is lowercase variant 'ss'

This was written to test my ability to write efficient code and also let me learn about the requests module and to play around with timing how long an operation takes

My performance output
```
The average time to peform was 1.0998964309692382e-06
The longest time was 0.00101470947265625
The shortest time was 0.0
```
And there are 89 palindromes in that word list.