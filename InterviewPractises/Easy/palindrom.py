"""
Check if string is palindrome (Word is the same both ways)
"""

def palindrom(word):

    if word == word[::-1]:
        print("It is a palindrom")
    else:
        print("Not a palindrom")
    
    
word = "Tauno"
palindrom(word)