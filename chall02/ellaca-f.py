#!/usr/bin/env python3
import sys
import re

pattern = re.compile("[A-Za-z ]+")

dic = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.", 
    "g":"--.",
    "h":"....", 
    "i":"..",       
    "j":".---", 
    "k":"-.-",
    "l":".-..", 
    "m":"--",         
    "n":"-.",         
    "o":"---",
    "p":".--.", 
    "q":"--.-", 
    "r":".-.",
    "s":"...",
    "t":"-",        
    "u":"..-",
    "v":"...-", 
    "w":".--",
    "x":"-..-", 
    "y":"-.--", 
    "z":"--..",
    " ":" "

}

if len(sys.argv) != 2:
    print("usage: ./xlogin.py <a-zA-Z string>")
elif sys.argv[1] == "":
    print("usage: ./xlogin.py <a-zA-Z string>")
elif pattern.fullmatch(sys.argv[1]) is None:
    print("usage: ./xlogin.py <a-zA-Z string>")
else:
    for c in sys.argv[1]:
        print(dic[c.lower()], end="")
    print()
    