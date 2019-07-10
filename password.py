'''
Python 3.7.3

The Python Phonetic Password "Translator"

This script will take in a password, and parse each letter against its
phonetic spelling.  It will then return the password, its length, and
the translation of the password into an easily-communicable string.

Note that lower-case letters are represented by lower-case phonetics,
and UPPER-CASE LETTERS are represented by UPPER-CASE PHONETICS.
'''

# Request password from user
from_user = input("\nEnter the string or password: ")

# Prep the global variable of the output string
output_string = ""

# Get the length of the password, and subtract by 1
hyphens = len(from_user) - 1

# Expecting only characters on standard US keyboards
unrecognized = 0

# The all-important dictionary of numbers, letters and symbols
pass_dict = {
    "a": "alfa",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliett",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "xray",
    "y": "yankee",
    "z": "zulu",
    "A": "ALFA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIETT",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "XRAY",
    "Y": "YANKEE",
    "Z": "ZULU",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
    "!": "Exclamation",
    '"': "Quotation",
    "#": "Octothorpe",
    "$": "Dollar",
    "%": "Percent",
    "&": "Ampersand",
    "'": "Apostrophe",
    "(": "Left Parenthesis",
    ")": "Right Parenthesis",
    "*": "Asterisk",
    "+": "Plus",
    ",": "Comma",
    "-": "Hyphen",
    ".": "Period",
    "/": "Slash",
    "?": "Question",
    ":": "Colon",
    ";": "Semicolon",
    "<": "Less-than",
    ">": "Greater-than",
    "=": "Equals",
    "@": "At",
    "[": "Left Square Bracket",
    "]": "Right Square Bracket",
    "{": "Left Curly Bracket",
    "}": "Right Curly Bracket",
    "^": "Carrot",
    "_": "Underscore",
    "`": "Grave",
    "~": "Tilde",
    "|": "Bar",
    "\\": "Backslash"
}

# Loop through each character in the password
for letter in from_user:
    # Try to lookup each character's value in the dictionary, and add it to the output string
    try:
        output_string = output_string + pass_dict[letter]
    # If the character is not found in the dictionary, insert "UNRECOGNIZED" instead, and flag it
    except KeyError:
        output_string = output_string + "UNRECOGNIZED"
        unrecognized = 1
	# Add hyphens after each value, except the last one
    if hyphens > 0:
        output_string = output_string + " - "
        hyphens = hyphens - 1

# Print all of the outputs
print("\nPassword:")
print(from_user)
print("\nLength:")
print(len(from_user))
print("\nPhonetic Output:")
print(output_string)
if unrecognized == 1:
    print("This password had an unrecognized character!")
print("")
